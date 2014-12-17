import igraph as ig
import pandas as pd
import numpy as np

# Read the source target weight file and save it as target source and weight file (Because we need the edges ending at the paper which was cited)
"""
df_edges = pd.read_csv("s_t_w.tsv",sep="\t", header=None)
df_edges.columns = ["source","target","weight"]
df_edges[["source","target"]] = df_edges[["source","target"]].astype(int)
df_edges.head().to_csv("T_S_W.tsv",sep="\t",header=None,cols=["target","source","weight"],index=False)
"""

# Read graph from file with format source target weight
g = ig.Graph.Read_Ncol("T_S_W.tsv", names=True, weights=True, directed=True)
pr = g.personalized_pagerank(directed=True,weights="weight")
pr_nw = g.personalized_pagerank(directed=True,weights=None)
ec = g.eigenvector_centrality(weights="weight")
ec_nw = g.eigenvector_centrality(weights=None)
hubs = g.hub_score(weights="weight")
authority = g.authority_score(weights="weight")
# Data frame to store data.
df = pd.DataFrame(g.vs["name"])
df.columns = ["PMID"]
df["ec"] = ec
df["ec_nw"] = ec_nw
df["log_ec"] = np.log10(ec)
df["log_ec_nw"] = np.log10(ec_nw)
df["pr"] = pr
df["pr_nw"] = pr_nw
df["deg"] = g.indegree()
df["hub"] = hubs
df["auth"] = authority

df_pmid = df
df_pmid["PMID"] = df_pmid["PMID"].astype(int)

#df_agg = pd.read_csv("SOURCE_AGG.tsv",sep="\t")
#df_agg.rename(columns={'Source':'PMID'}, inplace=True)
#df_agg[["PMID"]] = df_agg[["PMID"]].astype(int)

# Both data frames should have same index so as to be compatibe with join.
df_pmid = df_pmid.set_index("PMID")
#df_agg = df_agg.set_index("PMID")

# Concatanate columns in dataframes join on PMID
df_all = pd.concat([df_agg, df_pmid], axis=1, join="outer")

# Drop null value rows after join
df_all_nonull = df_all[pd.notnull(df_all['source_year_first'])]
# Covert datatypes to Int for years.
df_all_nonull[["source_year_first","target_year_max","target_year_min"]] = df_all_nonull[["source_year_first","target_year_max","target_year_min"]].astype(int)

df_all_nonull["cite_age"] = df_all_nonull["target_year_max"] - df_all_nonull["source_year_first"]
df_all_nonull["cite_span"] = df_all_nonull["target_year_max"] - df_all_nonull["target_year_min"]
df_all_nonull["avg_cite"] = df_all_nonull["Target_count"]/df_all_nonull["cite_age"]
df_all_nonull["avg_cite_for_span"] = df_all_nonull["Target_count"]/(df_all_nonull["cite_span"]+1)

# Save data to file
df_all_nonull.to_csv("PMID_CENTRALITY.tsv",sep="\t",index_label=["PMID"])

