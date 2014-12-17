# coding: utf-8

import pandas as pd
import numpy as np
df = pd.read_csv("PMID_1970_2008.tsv", sep="\t",index_col="PMID")
df.head()
df["citedby"] = df["citedby"].fillna("")
d_list = []
get_ipython().magic(u'paste')
get_ipython().magic(u'cpaste')
d_list = []
df.dtypes
df = df.reset_index()
df.head()
df.dtypes
df = df.set_index("PMID")
d_list
for i,d in df.iterrows():
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    for c in cites:
        if c in df.index:
            c_year = df.ix[c,"year"]
            d_dict = {'Source': i, 'Target': c, 'source_year':d["year"],\
            'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
            d_list.append(d_dict)
            
for i,d in df.head().iterrows():
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    for c in cites:
        if c in df.index:
            c_year = df.ix[c,"year"]
            d_dict = {'Source': i, 'Target': c, 'source_year':d["year"],\
            'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
            d_list.append(d_dict)
            
d_list = []
for i,d in df.head().iterrows():
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    for c in cites:
        if c in df.index:
            c_year = df.ix[c,"year"]
            d_dict = {'Source': i, 'Target': c, 'source_year':d["year"],\
            'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
            d_list.append(d_dict)
            
d_list
df.head(100)
for i,d in df.head(100).iterrows():
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    for c in cites:
        if c in df.index:
            c_year = df.ix[c,"year"]
            d_dict = {'Source': i, 'Target': c, 'source_year':d["year"],\
            'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
            d_list.append(d_dict)
            
d_list
d_list
for i,d in df.head(100).iterrows():
    cites = d["citedby"]
    print "PMID[%s]:%s" %(i,cites)
    if cites == "":
        cites = []
    else:
        cites = cites.split(",")
    for c in cites:
        c = int(c)
        if c in df.index:
            c_year = df.ix[c,"year"]
            d_dict = {'Source': i, 'Target': c, 'source_year':d["year"],'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
            d_list.append(d_dict)
            
d_list
d_list = []
for i,d in df.head(100).iterrows():
    cites = d["citedby"]
    print "PMID[%s]:%s" %(i,cites)
    if cites == "":
        cites = []
    else:
        cites = cites.split(",")
    for c in cites:
        c = int(c)
        if c in df.index:
            c_year = df.ix[c,"year"]
            d_dict = {'Source': i, 'Target': c, 'source_year':d["year"],'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
            d_list.append(d_dict)
            
d_list
df[5409710]
df[5409710]
df.ix[5409710]
d_list
df.ix[5409710]
df = pd.read_csv("PMID_2000.tsv", sep="\t",index_col="PMID")
df.head()
df[19726863]
df['19726863']
df.ix[19726863]
df.ix[19170410]
dit = df.head().iteritems()
dit
dit.next()
dit = df.head().iterkv()
dit.next()
k, dit = df.head().iterkv()
k
k, dit = df.head().itertuples()
dit = df.head().itertuples()
dit.next()
df.head()
dit = df.head().iterrows()
dit.next()
i,d = dit.next()
i
d
d_list
dit = pd.DataFrame(d_list,columns=['Source', 'Target', 'source_year',\
    'target_year', 'weight','norm_weight'])
dit
dit_c = dit["Source"].groupby("Source").count()
dit_c = dit[["Source"]].groupby("Source").count()
dit_c
df_h = df.head(100)
df_h[df_h["citedby"] != ""]
df_h[df_h["citedby"] != np.NaN]
df_h[df_h["citedby"] != np.NaN]
df["citedby"] = df["citedby"].fillna("")
df.head()
d_list = []
for i,d in df.head(100).iterrows():
    cites = d["citedby"]
    print "PMID[%s]:%s" %(i,cites)
    if cites == "":
        cites = []
    else:
        cites = cites.split(",")
    for c in cites:
        c = int(c)
        if c in df.index:
            c_year = df.ix[c,"year"]
            d_dict = {'Source': i, 'Target': c, 'source_year':d["year"],'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
            d_list.append(d_dict)
            
d_list
df_h[df_h["citedby"] != ""]
dit = pd.DataFrame(d_list,columns=['Source', 'Target', 'source_year',\
    'target_year', 'weight','norm_weight'])
dit_c = dit[["Source"]].groupby("Source").count()
dit_c
dit_c.index = ["PMID"]
dit_c.index.name = "PMID"
dit_c
df_all = pd.concat([df_h[df_h["citedby"] != ""], df_c], axis=1, join="outer")
df_all = pd.concat([df_h[df_h["citedby"] != ""], dit_c], axis=1, join="outer")
df_all
df.head()
df.count()
df.ix[19170410]
d = df.ix[19170410]
cites = d["citedby"]
cites
cites != ""
cites == ""
cites = []
for c in cites:
    print c
    
for i,d in df.iterrows():
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    for c in cites:
        c = int(c)
        if c in df.index:
            2121
            +11fdada
            
d_list = []
for i,d in df.iterrows():
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    for c in cites:
        c = int(c)
        if c in df.index:
            c_year = df.ix[c,"year"]
            d_dict = {'Source': i, 'Target': c, 'source_year':d["year"],'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
            d_list.append(d_dict)
            
df_pp = pd.DataFrame(d_list,columns=['Source', 'Target', 'source_year',\
    'target_year', 'weight','norm_weight'])
df_pp.head()
df_pp[df_pp["Source"] == 19170410]
df_pp.dtypes
df_pp.to_csv("SOURCE_TARGET_SY_TY_W_NW.tsv", sep="\t",index=False)
df_pp.head()
df.head()
df_yp_grp = df_pp.groupby(["source_year","target_year"])["weight"].count()
df_yp_grp.head()
df_yp_grp.to_csv("YEAR_PAIR_COUNTS.tsv",sep="\t",index_label=["source_year","target_year"])
df_year_tot = df_yp_grp.groupby(level=["source_year"]).sum()
def get_prob(r):
    tot = df_year_tot.ix[r.name[0]]
    return r*1.0/tot
df_yp_grp.head()
df_yp_grp.columns
df_yp_grp = df_pp.groupby(["source_year","target_year"])[["weight"]].count()
df_yp_grp.head()
df_yp_grp = df_pp[["weight"]].groupby(["source_year","target_year"]).count()
df_yp_grp = df_pp[["source_year","target_year","weight"]].groupby(["source_year","target_year"]).count()
df_yp_grp.head()
df_yp_grp = df_pp.groupby(["source_year","target_year"]).count()["weight"]
df_yp_grp.head()
df_yp_grp.columns
df_yp_grp[["weight"]] = df_yp_grp[["counts"]].apply(get_prob, axis=1)
df_yp_grp = df_pp.groupby(["source_year","target_year"])["weight"].count()
df_yp_grp.head()
df_yp_grp = pd.DataFrame(df_yp_grp)
df_yp_grp.columns = ["counts"]
df_yp_grp.head()
df_yp_grp.to_csv("YEAR_PAIR_COUNTS.tsv",sep="\t",index_label=["source_year","target_year"])
df_year_tot = df_yp_grp.groupby(level=["source_year"]).sum()
df_yp_grp[["weight"]] = df_yp_grp[["counts"]].apply(get_prob, axis=1)
df_yp_grp.head()
df_yp_grp.head(20)
df_yp_grp.to_csv("YEAR_PAIR_COUNTS.tsv",sep="\t",index_label=["source_year","target_year"])
df_target_count = df_pp[["Target"]].groupby("Target").count()
def norm_weight(r):
    
    
    
    None
    
df_target_count.columns = ["total_cited"]
df_target_count.head()
def norm_weight(r):
    norm_f = df_target_count.ix[r["Target"],"total_cited"]
    r["weight"] = df_yp_grp.ix[(r["source_year"],r["target_year"]), "weight"]
    r["norm_weight"] = -np.log10(r["weight"])/norm_f
    return r
df_pp_weights = df_pp.apply(norm_weight, axis=1)
df_pp_weights.head()
df_pp_weights.count()
df_pp_weights.to_csv("SOURCE_TARGET_SY_TY_ALL_WEIGHTS.tsv",sep="\t",index=False)
df_pp_weights[["Source","Target","norm_weight"]].to_csv("T_S_W.tsv",sep="\t",header=None,cols=["Target","Source","norm_weight"],index=False)
df_source_grp = df_pp_weights.groupby("Source").agg({"Target": "count", "source_year": "first", "target_year": {"min": np.min, "max": np.max}, "weight": np.sum, "norm_weight": np.sum})
df_source_grp.to_csv("SOURCE_AGG.tsv", sep="\t",index_label=["Source"], header= ["_".join(k) for k in df_source_grp.columns])
import igraph as ig
g = ig.Graph.Read_Ncol("T_S_W.tsv", names=True, weights=True, directed=True)
pr = g.personalized_pagerank(directed=True,weights="weight")
ec = g.eigenvector_centrality(weights="weight")
df_pp_weights.dtypes
df[['two', 'three']] = df[['two', 'three']].astype(float)
df[["Source","Target","source_year","target_year"]] = df[["Source","Target","source_year","target_year"]].astype(int)
df_pp_weights[["Source","Target","source_year","target_year"]] = df_pp_weights[["Source","Target","source_year","target_year"]].astype(int)
df_pp_weights.head()
df_pp_weights.to_csv("SOURCE_TARGET_SY_TY_ALL_WEIGHTS.tsv",sep="\t",index=False)
df_pp_weights[["Source","Target","norm_weight"]].to_csv("T_S_W.tsv",sep="\t",header=None,cols=["Target","Source","norm_weight"],index=False)
df_source_grp = df_pp_weights.groupby("Source").agg({"Target": "count", "source_year": "first", "target_year": {"min": np.min, "max": np.max}, "weight": np.sum, "norm_weight": np.sum})
df_source_grp.to_csv("SOURCE_AGG.tsv", sep="\t",index_label=["Source"], header= ["_".join(k) for k in df_source_grp.columns])
g = ig.Graph.Read_Ncol("T_S_W.tsv", names=True, weights=True, directed=True)
pr = g.personalized_pagerank(directed=True,weights="weight")
ec = g.eigenvector_centrality(weights="weight")
ec[0]
ec[10]
pr[0]
df = pd.DataFrame(g.vs["name"])
df.head()
df.columns = ["PMID"]
df["ec"] = ec
df["pr"] = pr
df["deg"] = g.outdegree()
df.head()
df.dtypes
df_pmid = df
df_pmid["PMID"] = df_pmid["PMID"].astype(int)
df_source_grp.head()
df_agg = pd.read_csv("SOURCE_AGG.tsv",sep="\t")
df_agg.rename(columns={'Source':'PMID'}, inplace=True)
df_agg[["PMID"]] = df_agg[["PMID"]].astype(int)
df_agg.head()
df_pmid = df_pmid.set_index("PMID")
df_agg = df_agg.set_index("PMID")
df_all = pd.concat([df_agg, df_pmid], axis=1, join="outer")
df_all.count()
df_all_nonull = df_all[pd.notnull(df_all['source_year_first'])]
df_all_nonull.head()
df_all_nonull.to_csv("PMID_CENTRALITY.tsv",sep="\t",index_label=["PMID"])
df_all_nonull[df_all_nonull["ec"] > 0.1].count()
df_all_nonull[df_all_nonull["ec"] > 0.0001].count()
df_all_nonull[df_all_nonull["ec"] > 0.0000000000000000001].count()
df_all_nonull[df_all_nonull["pr"] > 0.1].count()
df_all_nonull[df_all_nonull["pr"] > 0.01].count()
df_all_nonull[df_all_nonull["pr"] > 0.001].count()
df_all_nonull[df_all_nonull["pr"] > 0.00001].count()
df_all_nonull[-np.log10(df_all_nonull["pr"]) < 10].count()
df_all_nonull[-np.log10(df_all_nonull["pr"]) < 3].count()
df_all_nonull[-np.log10(df_all_nonull["pr"]) < 5].count()
df_all_nonull[-np.log10(df_all_nonull["pr"]) < 6].count()
hubs = g.hub_score(weights="weight")
authority = g.authority_score(weights="weight")
df.head()
df["hub"] = hubs
df["auth"] = authority
df.head()
df_s = df.sort("pr",ascending=False)
df_s.head()
df_s.head(10)
df_deg = df.sort("deg",ascending=False)
df_deg.head()
df["in_deg"] = g.indegree()
df.head()
df_deg = df.sort("in_deg",ascending=False)
df_deg.head()
df["deg"] = g.indegree()
df.drop('in_deg', axis=1, inplace=True)
df.drop('in_deg', axis=1)
df = df.drop('in_deg', axis=1)
df.head()
df_pmid = df
df_pmid["PMID"] = df_pmid["PMID"].astype(int)
df_agg.head()
df_all = pd.concat([df_agg, df_pmid], axis=1, join="outer")
df_all_nonull = df_all[pd.notnull(df_all['source_year_first'])]
df_all_nonull[["source_year_first","target_year_max","target_year_min"]] = df_all_nonull[["source_year_first","target_year_max","target_year_min"]].astype(int)
df_all_nonull.dtypes
df_all_nonull.head()
df_pmid = df_pmid.set_index("PMID")
# Concatanate columns in dataframes join on PMID
df_all = pd.concat([df_agg, df_pmid], axis=1, join="outer")
# Drop null value rows after join
df_all_nonull = df_all[pd.notnull(df_all['source_year_first'])]
# Covert datatypes to Int for years.
df_all_nonull[["source_year_first","target_year_max","target_year_min"]] = df_all_nonull[["source_year_first","target_year_max","target_year_min"]].astype(int)
df_pmid["PMID"] = df_pmid["PMID"].astype(int)
df_pmid = df
df_pmid["PMID"] = df_pmid["PMID"].astype(int)
df_pmid = df_pmid.set_index("PMID")
df_all = pd.concat([df_agg, df_pmid], axis=1, join="outer")
# Drop null value rows after join
df_all_nonull = df_all[pd.notnull(df_all['source_year_first'])]
# Covert datatypes to Int for years.
df_all_nonull[["source_year_first","target_year_max","target_year_min"]] = df_all_nonull[["source_year_first","target_year_max","target_year_min"]].astype(int)
df_all_nonull.dtypes
df_all_nonull.to_csv("PMID_CENTRALITY.tsv",sep="\t",index_label=["PMID"])
ec_nw = g.eigenvector_centrality(weights=None)
ec_nw[0:10]
df["ec_nw"] = ec_nw
df.head()
df_tt = df[df["ec"] != df["ec_nw"]]
df_tt.head()
df_tt = df[abs(df["ec"]- df["ec_nw"]) > 0.0000000000000001 ]
df_tt.head()
df_tt = df
df_tt["log_ec"] = np.log10(df["ec"])
df_tt["log_ec_nw"] = np.log10(df["ec_nw"])
df_tt.head()
df_tt["log_ec"] = np.log10(df["ec"]+1)
df_tt["log_ec_nw"] = np.log10(df["ec_nw"]+1)
df_tt.head()
df_tt["log_ec_nw"] = np.log10(df["ec_nw"])
df_tt["log_ec"] = np.log10(df["ec"])
df_tt.head()
df_tt_s = df_tt.sort("log_ec", ascending=False)
df_tt_s.head()
df_tt_s.head()
df_tt_s_nw = df_tt.sort("log_ec_nw", ascending=False)
df_tt_s_nw.head()
pr_nw = g.personalized_pagerank(directed=True)
df.head()
df["pr_nw"] = pr_nw
df.head()
df_tt = df
df_tt_s = df_tt.sort("pr", ascending=False)
df_tt_s.head()
df_tt_s = df_tt.sort("pr_nw", ascending=False)
df_tt_s.head()
np.log10(range(0,10))
np.log10(range(0,11))
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
df_all_nonull.to_csv("PMID_CENTRALITY.tsv",sep="\t",index_label=["PMID"])
df_all_nonull.head()
df_all_nonull["cite_span"] = PMID    source_year_first       target_year_max target_year_min weight_sum      norm_weight_sum Target_count    ec      pr      deg     hub     auth    ec_nw   log_ec  log_ec_nw       pr_nw
10474002        2000    2008    2008    0.13739817853877345     0.086201902459672367    1.0     0.0     2.9085662990539447e-07  1       0.0     0.0     0.0                     2.897646624704449e-07
10474004        2000    2008    2008    0.13739817853877345     0.17240380491934473     1.0     2.1511333965389885e-20  3.186688224919885e-07   1       0.0     0.0     0.0     -19.667332657216228            3.1017020974497797e-07
10474011        2000    2003    2000    0.091853310396002461    0.74058235527835026     2.0     1.0415663920109481e-20  4.0937913550179313e-07  2       0.0     0.0     0.0     -19.982313041832402            4.1218176158834216e-07
10494624        2000    2003    2003    0.077842871872403227    0.073918743328818717    1.0     0.0     2.7858523363971727e-07  1       0.0     9.0818007850878673e-15  0.0                   2.8040881033004038e-07
10494625        2000    2009    2000    1.4270783250560695      3.1734324624494477      20.0    3.4719847964929602e-19  1.5779824712467994e-06  20      0.0     7.955624734928117e-14   3.6368765648506693e-17 -18.459422185227595     -16.439271438597178     1.5611126057853466e-06
10494626        2000    2009    2001    1.2335383426759416      0.63785569527302466     11.0    1.3389109374339706e-20  4.2988529886317748e-07  11      0.0     2.4472361994643554e-09  6.9176769308052033e-19 -19.873248310715692     -18.160039724259331     4.1827640196213486e-07
10494627        2000    2011    2001    1.6500141737141525      1.7432254920528498      18.0    1.6657435191728295e-19  8.1126074060869319e-07  18      0.0     1.5087082515120198e-13  2.3906507049691156e-18 -18.778391867744926     -17.621483873481068     8.1077024875532056e-07
10503188        2000    2006    2006    0.086490921875043425    0.0088585789490143001   1.0     2.0355334263312206e-21  2.695132897470487e-07   1       0.0     3.5792136661589007e-15  3.7416320334373123e-18 -20.691321761497793     -17.426938924934728     2.6937360058548698e-07
10503189        2000    2011    2001    2.240315323452494       0.93590927169848626     21.0    4.2743378773208685e-20  5.3598297166807107e-07  21      0.0     1.4606288633613245e-13  6.5474493291811004e-18 -19.369131150759646     -17.18392785390192      5.0527328973254728e-07
df_all_nonull["cite_span"]
df_all_nonull["cite_age"] = df_all_nonull["target_year_max"] - df_all_nonull["source_year_first"]
df_all_nonull["cite_span"] = df_all_nonull["target_year_max"] - df_all_nonull["target_year_min"]
df_all_nonull.head()
df_all_nonull.head(10)
df_all_nonull.head(2).to_string()
df_all_nonull.head(2).to_wide()
df_all_nonull.head(2).to_records()
df_all_nonull[["weight_sum","norm_weight_sum","Target_count","ec","pr","deg","hub","auth","ec_nw","log_ec","log_ec_nw","pr_nw","cite_age","cite_span"]].head(2)
df_all_nonull[["weight_sum","norm_weight_sum","Target_count","ec","pr","deg","hub","auth","ec_nw","log_ec","log_ec_nw","pr_nw","cite_age","cite_span"]].head(10)
df_tt.head()
df_tt = df_all_nonull
df_s = df_tt.sort("cite_span",ascending=False)
df_s[["source_year_first","weight_sum","norm_weight_sum","Target_count","ec","pr","deg","hub","auth","ec_nw","log_ec","log_ec_nw","pr_nw","cite_age","cite_span"]].head(10)
df_s[["source_year_first","weight_sum","norm_weight_sum","Target_count","ec","pr","deg","hub","auth","ec_nw","log_ec","log_ec_nw","pr_nw","cite_age","cite_span"]].head(10)
df_s = df_tt.sort(["cite_span","Target_count"],ascending=False)
df_s[["source_year_first","weight_sum","norm_weight_sum","Target_count","ec","pr","deg","hub","auth","ec_nw","log_ec","log_ec_nw","pr_nw","cite_age","cite_span"]].head(10)
df_all_nonull.head()
df_all_nonull["avg_cite"] = df_all_nonull["Target_count"]/df_all_nonull["cite_age"]
df_all_nonull["avg_cite_for_span"] = df_all_nonull["Target_count"]/(df_all_nonull["cite_span"]+1)
df_all_nonull.to_csv("PMID_CENTRALITY.tsv",sep="\t",index_label=["PMID"])
df_pp.head()
df_tcs = df_pp.groupby(["Source","target_year"]).agg({"source_year":np.first,"weight":np.count})
df_tcs = df_pp.groupby(["Source","target_year"]).agg({"source_year":first,"weight":np.count})
df_tcs = df_pp.groupby(["Source","target_year"]).agg({"source_year":first,"weight":np.count})
df_tcs = df_pp.groupby(["Source","target_year"]).agg({"source_year":"first","weight":"count"})
df_tcs.head()
df_tmp = df_tcs.head()
df_tmp.head()
df_tmp = pd.DataFrame(df_tmp)
df_tmp
df_tmp.reset_index()
df_tmp.reset_index(1)
df_tmp.reset_index(2)
df_tmp.reset_index(0)
df_tmp.reset_index("target_year")
df_tmp.reset_index(["target_year"])
df_tmp.reset_index()
df_tmp.reset_index("Source")
df_tmp.reset_index(level="Source")
df_tmp.dtypes
type(df_tmp)
pd.__version__
df_tmp.reset_index()
df_tmp = df_tmp.reset_index()
df_tmp
df_tmp.set_index("Source")
df_tmp
df_tmp = df_tmp.set_index("Source")
df_tmp["diff_y"] = df_tmp["target_year"] - df_tmp["source_year"]
df_tmp
df_tmp = df_tmp.reset_index()
df_tmp
df_tmp_tot = df_tmp.groupby("target_year").count()["weight"]
df_tmp_tot
df_tmp_tot = df_tmp.groupby("target_year").agg({"weight":"count"})
df_tmp_tot
df_tmp_tot.columns = ["total_cites"]
df_tmp_tot
df_tmp
df_tmp["w_cite"] = df_tmp["weight"]*1.0*df_tmp["diff_y"]/df_tmp_tot.ix[df_tmp["target_year"]]
df_tmp["w_cite"] = df_tmp.apply(lambda x: x["weight"]*1.0*x["diff_y"]/df_tmp_tot.ix[x["target_year"]])
df_tmp["w_cite"] = df_tmp.apply(lambda x: x["weight"]*1.0*x["diff_y"]/df_tmp_tot.ix[x["target_year"]],axis=1)
def w_cites:
    
def w_cites(r):
    print r
    tot = df_tmp_tot.ix[r["target_year"],"weight"]
    return r["weight"]*1.0*r["diff_y"]/tot
df_tmp["w_cite"] = df_tmp.apply(w_cites,axis=1)
def w_cites(r):
    print r
    tot = df_tmp_tot.ix[r["target_year"],"total_cites"]
    return r["weight"]*1.0*r["diff_y"]/tot
df_tmp["w_cite"] = df_tmp.apply(w_cites,axis=1)
df_tmp
df_tmp_tot
df_tcs.head()
df_tcs_tot = df_tcs.groupby("target_year").count()["weight"]
df_tcs.head()
df_tcs = df_tcs.reset_index()
df_tcs.head()
df_tcs.head(20)
df_tcs_tot = df_tcs.groupby("target_year").count()["weight"]
df_tcs_tot
df_tcs_tot.columns = ["total_cites"]
df_tcs_tot
df_tcs_tot = pd.DataFrame(df_tcs.groupby("target_year").count()["weight"])
df_tcs_tot.columns = ["total_cites"]
df_tcs_tot
df_tcs_tot["log_cites"] = np.log10(df_tcs_tot["total_cites"])
df_tcs_tot
def w_cites(r):
    print r
    tot = df_tmp_tot.ix[r["target_year"],"log_cites"]
    diff_y = r["target_year"] - r["source_year"] + 1
    return r["weight"]*diff_y/tot
def w_cites(r):
    print r
    tot = df_tcs_tot.ix[r["target_year"],"log_cites"]
    diff_y = r["target_year"] - r["source_year"] + 1
    return r["weight"]*diff_y/tot
df_tcs_tot
df_tcs.head()
df_tcs["w_cites"] = df_tcs.apply(w_cites,axis=1)
def w_cites(r):
    tot = df_tcs_tot.ix[r["target_year"],"log_cites"]
    diff_y = r["target_year"] - r["source_year"] + 1
    return r["weight"]*diff_y/tot
df_tcs["w_cites"] = df_tcs.apply(w_cites,axis=1)
df_tcs.head()
df_tcs_agg = df_tcs.groupby("PMID")["weight"].count()
df_tcs_agg = df_tcs.groupby("Source")["weight"].count()
df_tcs_agg.head()
df_tcs_agg = df_tcs.groupby("Source").agg("w_cites":"sum")
df_tcs_agg = df_tcs.groupby("Source").agg({"w_cites":"sum"})
df_tcs_agg.head()
df_tcs.head()
df_tcs_agg.index.name
df_tcs_agg.index.name = "PMID"
df_tcs_agg.head()
df_all_nonull.head()
df_all_final = pd.concat(df_all_nonull,df_tcs_agg,join="outer")
df_all_final = pd.concat([df_all_nonull,df_tcs_agg],join="outer")
df_all_final.head()
df_all_final["w_cites"].head()
df_tcs_agg.ix[10474002]
df_tcs_agg.ix[10474002]
df_all_final
df_all_final.head()["w_cites"]
df_all_nonull
df_all_final.head()[["w_cites","pr_nw"]]
df_tcs_agg
df_all_final = pd.concat([df_all_nonull,df_tcs_agg],join="inner")
df_all_final.head()
df_all_nonull
df_all_nonull.head()
df_all_nonull.head()["weight"]
df_all_nonull.head()
df_all_nonull.head()["pr"]
df_tcs_agg
df_tcs_agg.head()
df_all_final = pd.concat([df_all_nonull,df_tcs_agg],join_axes=["PMID"])
df_tcs_agg
df_tcs_agg.head()
df_all_nonull.head()
df_all_nonull.head()["ec"]
df_all_nonull.head()[["ec"]]
df_tcs_agg.head()
pd.concat([df_all_nonull.head()[["ec"]],df_tcs_agg.head()],join="outer")
df_tcs_agg.head()
df_tcs_agg.reset_index()
df_tcs_agg = df_tcs_agg.reset_index()
df_tcs_agg
df_tcs_agg[["PMID"]]
df_tcs_agg = df_tcs_agg.set_index("PMID")
df_tcs_agg
pd.concat([df_all_nonull.head()[["ec"]],df_tcs_agg.head()],join="outer")
df_all_nonull
df_all_final = df_all_nonull
df_all_final["w_cites"] = df_tcs_agg["w_cites"]
df_all_final.head()["w_cites","ec"]
df_all_final.head()[["w_cites","ec"]]
df_all_nonull[["ec"]].head()
df_tcs_agg[["w_cites"]].head()
df_tcs_agg.to_csv("PMID_CENTRALITY_WC.tsv",sep="\t",index_label=["PMID"])
get_ipython().magic(u'save new_metric_agg 0-447')