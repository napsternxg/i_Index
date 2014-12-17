import pandas as pd
import numpy as np

"""
Import the PMID_2000.tsv file containing the columns from Articles table in Format:
  PMID  year  citedby
"""
df = pd.read_csv("PMID_1970_2008.tsv", sep="\t",index_col="PMID")
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
df_pp_weights.to_csv("SOURCE_TARGET_SY_TY_ALL_WEIGHTS.tsv",sep="\t",index=False)
df_pp_weights[["Source","Target","norm_weight"]].to_csv("T_S_W.tsv",sep="\t",header=None,cols=["Target","Source","norm_weight"],index=False)


# Sort the array based on norm_weight
df_w_sorted = df_pp_weights.sort(columns="norm_weight", ascending=False)


# Group by based on various aggregation methods and save to file
df_source_grp = df_pp_weights.groupby("Source").agg({"Target": "count", "source_year": "first", "target_year": {"min": np.min, "max": np.max}, "weight": np.sum, "norm_weight": np.sum})
df_source_grp.to_csv("SOURCE_AGG.tsv", sep="\t",index_label=["Source"], header= ["_".join(k) for k in df_source_grp.columns])


# Done
