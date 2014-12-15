# coding: utf-8

import igraph as ig
g = ig.Graph.Read_Ncol("s_t_w.tsv", names=True, weights=True, directed=True)
pr = g.personalized_pagerank(directed=True,weights="weight")
pr
pr1 = g.personalized_pagerank(directed=True)
pr1
g = ig.Graph.Read_Ncol("s_t_w.tsv", names=True, weights=True, directed=True)
g.es[0]
g.es[0]["weight"]
pr = g.personalized_pagerank(directed=True,weights="weight")
pr[0]
ec = g.eigenvector_centrality(weights="weight")
ec[0]
ec[0:10]
import pandas as pd
a = range(10)
df = pd.DataFrame(a)
df
df["a2"] = a
df
df = pd.DataFrame()
df["a"] = a
g.vs["name"][0:10]
df = pd.DataFrame(g.vs["name"])
df.head()
df.column
df.columns
df.columns = ["PMID"]
df.head()
df["ec"] = ec
df["pr"] = pr
df.head()
g.degree()[0]
g.degree()[2]
df["deg"] = g.degree()
df.head()
df[df["ec"] > 0].head()
df_pmid = df
df_pmid = df_pmid.set_index("PMID")
df_pmid.head()
df_pmid.count()
df_agg = pd.read_csv("SOURCE_AGG.tsv",sep="\t",index="Source")
df_agg = pd.read_csv("SOURCE_AGG.tsv",sep="\t",index_col="Source")
df_agg.index
df_agg.head()
df_agg.info
df_agg.index.name
df_agg.index.name = "PMID"
df_agg.head()
df_pmid.head)(
df_pmid.head()
df_pmid.index.dtype = "int64"
df_pmid.index.dtype = int64
df_pmid.index.dtype = int
df_pmid.reset_index().head()
df_pmid.head()
df_pmid = df_pmid.reset_index()
df_pmid.head()
df_pmid.dtypes
df_pmid.dtypes = ['int64','float64','float64','int64']
df_pmid["PMID"] = df_pmid["PMID"].astype(int)
df_pmid["PMID"].head()
int('24961199.0')
long('24961199.0')
df_pmid.ix['24961199.0']
df_pmid.ix[24961199.0]
df_pmid.ix[['24961199.0']]
df_pmid.ix[[24961199.0]]
df_pmid.ix[df_pmid["PMID"] == '24961199.0']
df_pmid.ix[df_pmid["PMID"] == 24961199.0]
df = pd.DataFrame(g.vs["name"])
df_pmid.head()
df_pmid["PMID"] = df_pmid["PMID"].astype(float)
df_pmid.head()
df_pmid["PMID"] = df_pmid["PMID"].astype(int)
df_pmid.head()
df = df_pmid.set_index("PMID")
df.head()
df_agg.head()
t1 = df_agg.head()
t2 = df_pmid.head()
t1, t2
t2 = df.head()
t1, t2
pd.concat(t1,t2)
pd.concat([t1,t2],axis=1,join="inner")
pd.concat([t1,t2],axis=1,join="outer")
t1
t2
t2.ix[10473999] = (1,2,3)
pd.Series([1,2,3])
pd.Series([5,6,7])
s = pd.Series([5,6,7])
s.name = 10473999
t2
t2.append(s)
s = pd.Series({"ec":5,"pr":6,"deg":7})
s.name = 10473999
t2.append(s)
pd.concat([t1,t2],axis=1,join="outer")
t1
t1 = t1.reset_index()
t1
t1["PMID"] = t1["PMID"].astype(int)
t1
t1 = t1.set_index("PMID")
t1
pd.concat([t1,t2],axis=1,join="outer")
t2
t2 = t2.append(s)
t2
pd.concat([t1,t2],axis=1,join="outer")
df_pmid.head()
df_pmid.dtypes
df_pmid = df_pmid.set_index("PMID")
df_pmid.head()
df_agg.head()
df_agg = df_agg.reset_index()
df_agg.dtypes
df_agg["PMID"] = df_agg["PMID"].astype(int)
df_agg.head()
df_dty
df_agg.dtypes
df_agg = df_agg.set_index("PMID")
df_all = pd.concat([df_agg, df_pmid], axis=1, join="outer")
df_all.head()
df_pmid.ix[10473999]
df_agg.ix[10473999]
df_all[["source_year_first","target_year_max","target_year_min"]] = df_all[["source_year_first","target_year_max","target_year_min"]].astype(int)
df_all.head()
df_all.head()
df_all[df_all["source_year_first"] = np.NaN]
import numpy as NaN
df_all[df_all["source_year_first"] = np.NaN]
df_all[df_all["source_year_first"] == np.NaN]
import numpy as np
df_all[df_all["source_year_first"] == np.NaN]
df_pmid.count()
df_agg.count()
df_pmid.tail()
df_all.tail()
df_all[df_all["ec"] == np.NaN]
df_all_nonull = df_all[pd.notnull(df_all['source_year_first'])]
df_all_nonull.count()
df_all.count()
df_all_nonull.head()
df_all_nonull[["source_year_first","target_year_max","target_year_min"]] = df_all_nonull[["source_year_first","target_year_max","target_year_min"]].astype(int)
df_all_nonull.head)(
df_all_nonull.head()
df_all_nonull.dtypes
df_all_nonull.to_csv("PMID_CENTRALITY.tsv",sep="\t",index_label=["PMID"])
g