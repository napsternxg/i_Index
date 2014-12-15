# coding: utf-8
df_pp_weights1.head()
get_ipython().magic(u'save final_preprocess 0-355')
get_ipython().magic(u'save final_preprocess 60-355')
df_pp_weights.head()
df_pp_weights1.head()
df_pp_weights.head().apply(norm_weight, axis=1)
df_pp_weights.tail()
df_pp_weights1.tail()
0.536136/31
-np.log10(0.536136)
-np.log10(0.536136)/31
df_pp_weights1.head().sort(columns="norm_weight", ascending=False)
df_pp_weights1.head()
df_w_sorted = df_pp_weights1.sort(columns="norm_weight", ascending=False)
df_w_sorted.head()
df_pp_weights = df_pp_weights1
del df_pp_weights1
df_pp_weights.head()
df.head()
df_pp_weights.head().groupby().agg({"Target": "count", "source_year": "first", "target_year": np.min, "target_year": np.max})
df_pp_weights.head().groupby().agg({"Target": "count", "source_year": "first"})
df_pp_weights.head().groupby().agg({"Target": "count"})
df_pp_weights.head().groupby().agg({"Target": np.size})
df_pp_weights.head().groupby("Source").agg({"Target": np.size})
df_pp_weights.head().groupby("Source").agg({"Target": "count", "source_year": "first", "target_year": np.min, "target_year": np.max})
df_pp_weights.head().groupby("Source").agg({"Target": "count", "source_year": "first", "target_year": {"min": np.min, "max": np.max}})
df_pp_weights.head().groupby("Source").agg({"Target": "count", "source_year": "first", "target_year": {"min": np.min, "max": np.max}, "weight": np.sum, "norm_weight": np.sum})
df_source_grp = df_pp_weights.head().groupby("Source").agg({"Target": "count", "source_year": "first", "target_year": {"min": np.min, "max": np.max}, "weight": np.sum, "norm_weight": np.sum})
df_source_grp[("source_year","first")]
df_source_grp[("target_year","min")]
df_source_grp[("target_year","max")]
df_source_grp.to_csv("SOURCE_AGG.tsv", sep="\t",index_labels=["Source"])
df_source_grp.to_csv("SOURCE_AGG.tsv", sep="\t",index_label=["Source"])
df_source_grp.columns
"_".join(("A","B"))
["_".join(k) for k in df_source_grp.columns]
df_source_grp.to_csv("SOURCE_AGG.tsv", sep="\t",index_label=["_".join(k) for k in df_source_grp.columns])
df_source_grp.to_csv("SOURCE_AGG.tsv", sep="\t",index_label=["Source"], columns = ["_".join(k) for k in df_source_grp.columns])
df_source_grp.to_csv("SOURCE_AGG.tsv", sep="\t",index_label=["Source"], column = ["_".join(k) for k in df_source_grp.columns])
df_source_grp.to_csv("SOURCE_AGG.tsv", sep="\t",index_label=["Source"], cols= ["_".join(k) for k in df_source_grp.columns])
df_source_grp.to_csv("SOURCE_AGG.tsv", sep="\t",index_label=["Source"], header= ["_".join(k) for k in df_source_grp.columns])
df_source_grp = df_pp_weights.groupby("Source").agg({"Target": "count", "source_year": "first", "target_year": {"min": np.min, "max": np.max}, "weight": np.sum, "norm_weight": np.sum})
df_source_grp.head()
df_source_grp.count()
df_source_grp.to_csv("SOURCE_AGG.tsv", sep="\t",index_label=["Source"], header= ["_".join(k) for k in df_source_grp.columns])
df_pp_weights.head()