import pandas as pd
import numpy as np

"""
Import the PMID_2000.tsv file containing the columns from Articles table in Format:
  PMID  year  citedby
"""
df = pd.read_csv("PMID_2000.tsv", sep="\t",index_col="PMID")
# Replace all null vals of citedby column with empty string.
df["citedby"] = df["citedby"].fillna("")


# Create empty list to store the source target dicts.
d_list = []
# Iterate through each row of df to extract the source and target. 
# Also include source and target years and prepolulate weights with 0
for i,d in df.iterrows():
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    for c in cites:
        c = int(c)
        if c in df.index:
            c_year = int(df.ix[c,"year"])
            d_dict = {'Source': i, 'Target': c, 'source_year':int(d["year"]),\
                'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
            d_list.append(d_dict)


# Create a Dataframe from the d_list
df_pp = pd.DataFrame(d_list,columns=['Source', 'Target', 'source_year',\
    'target_year', 'weight','norm_weight'])

# Save this table into a file.
df_pp.to_csv("SOURCE_TARGET_SY_TY_W_NW.tsv", sep="\t",index=False)

# Group by using source_year and then target_year and get the counts.
df_yp_grp = df_pp.groupby(["source_year","target_year"])["weight"].count()
df_yp_grp = pd.DataFrame(df_yp_grp)
df_yp_grp.columns = ["counts"]
# Save this data to file.
df_yp_grp.to_csv("YEAR_PAIR_COUNTS.tsv",sep="\t",index_label=["source_year","target_year"])

# Get total citation for each source year.
df_year_tot = df_yp_grp.groupby(level=["source_year"]).sum()


# Function to calculate the probability of a citation from source_year to target_year
def get_prob(r):
    tot = df_year_tot.ix[r.name[0]]
    return r*1.0/tot


# Find the probabilities for all year pairs and save to file.
df_yp_grp[["weight"]] = df_yp_grp[["counts"]].apply(get_prob, axis=1)
df_yp_grp.to_csv("YEAR_PAIR_COUNTS.tsv",sep="\t",index_label=["source_year","target_year"])

# Find the total papers cited by a target paper as this will be used for normalization.
df_target_count = df_pp[["Target"]].groupby("Target").count()
df_target_count.columns = ["total_cited"]

# Function to calculate the normalized weight of each edge using -log(p)/n formula.
def norm_weight(r):
    norm_f = df_target_count.ix[r["Target"],"total_cited"]
    r["weight"] = df_yp_grp.ix[(r["source_year"],r["target_year"]), "weight"]
    r["norm_weight"] = -np.log10(r["weight"])/norm_f
    return r

# Find weights for all edges and save to file
df_pp_weights = df_pp.apply(norm_weight, axis=1)
df_pp_weights[["Source","Target","source_year","target_year"]] = df_pp_weights[["Source","Target","source_year","target_year"]].astype(int)
df_pp_weights.to_csv("SOURCE_TARGET_SY_TY_ALL_WEIGHTS.tsv",sep="\t",index=False)
df_pp_weights[["Source","Target","norm_weight"]].to_csv("T_S_W.tsv",sep="\t",header=None,cols=["Target","Source","norm_weight"],index=False)


# Sort the array based on norm_weight
#df_w_sorted = df_pp_weights.sort(columns="norm_weight", ascending=False)


# Group by based on various aggregation methods and save to file
df_source_grp = df_pp_weights.groupby("Source").agg({"Target": "count", "source_year": "first", "target_year": {"min": np.min, "max": np.max}, "weight": np.sum, "norm_weight": np.sum})
df_source_grp.columns = ["_".join(i) for i in df_source_grp.columns]
df_source_grp.index.name = "PMID"
# Add some more scores to the source aggregator

df_source_grp["cite_age"] = abs(df_source_grp["target_year_max"] - df_source_grp["source_year_first"])
df_source_grp["cite_span"] = abs(df_source_grp["target_year_max"] - df_source_grp["target_year_min"])
df_source_grp["avg_cite"] = df_source_grp["Target_count"]/(df_source_grp["cite_age"]+1)
df_source_grp["avg_cite_for_span"] = df_source_grp["Target_count"]/(df_source_grp["cite_span"]+1)

#df_source_grp.to_csv("SOURCE_AGG_OLD.tsv", sep="\t",index_label=["PMID"])

# Read the scores in given format
#df_source_grp = pd.read_csv("SOURCE_AGG_OLD.tsv",sep="\t")
#df_source_grp.rename(columns={'Source':'PMID'}, inplace=True)
#df_source_grp[["PMID"]] = df_source_grp[["PMID"]].astype(int)
#df_source_grp = df_source_grp.set_index("PMID")


# Start computation of temporal citation score
df_tcs = df_pp_weights
#df_tcs = df_pp.groupby(["Source","target_year"]).agg({"source_year":"first","weight":"count"})
# Total number of citation in each year
df_tcs_tot = pd.DataFrame(df_tcs.groupby("target_year").count()["weight"])
df_tcs_tot.columns = ["total_cites"]
df_tcs_tot["log_cites"] = np.log10(df_tcs_tot["total_cites"])

def w_cites(r):
    tot = df_tcs_tot.ix[r["target_year"],"log_cites"]
    diff_y = abs(r["target_year"] - r["source_year"]) + 1.0
    return r["weight"]*diff_y/tot

# Generate the temporal citatation score
df_tcs["w_cites"] = df_tcs.apply(w_cites,axis=1)
df_tcs.rename(columns={"Source":"PMID"}, inplace=True)
df_tcs["PMID"] = df_tcs["PMID"].astype(int)
#df_tcs.to_csv("SOURCE_AGG_WC.tsv",sep="\t",index_label=["PMID"])

# Aggregate score for each PMID
df_tcs_agg = df_tcs.groupby("PMID").agg({"w_cites":"sum"})
#df_tcs_agg.index.name = "PMID"
# Add these score to the PMID aggregation table.
df_source_grp[["w_cites"]] = df_tcs_agg[["w_cites"]]
df_source_grp.to_csv("SOURCE_AGG.tsv",sep="\t",index_label=["PMID"])
# Done
