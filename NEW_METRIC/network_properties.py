import igraph as ig
import pandas as pd

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
ec = g.eigenvector_centrality(weights="weight")

# Data frame to store data.
df = pd.DataFrame(g.vs["name"])
df.columns = ["PMID"]
df["ec"] = ec
df["pr"] = pr
df["deg"] = g.degree()

df_pmid = df
df_pmid["PMID"] = df_pmid["PMID"].astype(int)

df_agg = pd.read_csv("SOURCE_AGG.tsv",sep="\t")
df_agg.rename(columns={'Source':'PMID'}, inplace=True)
df_agg[["PMID"]] = df_agg[["PMID"]].astype(int)

# Both data frames should have same index so as to be compatibe with join.
df_pmid = df_pmid.set_index("PMID")
df_agg = df_agg.set_index("PMID")

# Concatanate columns in dataframes join on PMID
df_all = pd.concat([df_agg, df_pmid], axis=1, join="outer")

# Drop null value rows after join
df_all_nonull = df_all[pd.notnull(df_all['source_year_first'])]
# Covert datatypes to Int for years.
df_all_nonull[["source_year_first","target_year_max","target_year_min"]] = df_all_nonull[["source_year_first","target_year_max","target_year_min"]].astype(int)
# Save data to file
df_all_nonull.to_csv("PMID_CENTRALITY.tsv",sep="\t",index_label=["PMID"])

