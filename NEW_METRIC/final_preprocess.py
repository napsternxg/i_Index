# coding: utf-8
get_ipython().magic(u'save data_preprocess 0-60')
df_data
df_pmid
df_data.head()
df_data.ix[21785590]
df_data.index = ["PMID"]
df_data.set_index("PMID")
df_data.head()
df_data = df_data.set_index("PMID")
df_data.head()
df_data.ix[21785590]
df_data.ix["21785590"]
df_data.ix[["21785590"]]
df_data.ix[[21785590]]
df_data.head()
df_data.ix[[20876490]]
df_data.ix[[21331282]]
df_data.ix[[21876846]]
df_data.tail()
df_data.ix[[23308049]]
df_data.ix[[23304098]]
df = pd.read_csv("PMID_2000.tsv", sep="\t",index_cols="PMID")
df = pd.read_csv("PMID_2000.tsv", sep="\t",index="PMID")
df = pd.read_csv("PMID_2000.tsv", sep="\t",index_columns="PMID")
df = pd.read_csv("PMID_2000.tsv", sep="\t",index_col="PMID")
df.head()
df.ix[[22053223]]
df_pmid
df
for d in df.head():
    print d
    
for d in df.head().rows():
    print d
    
for d in df.head().iterrows():
    print d
    
for d in df.head().iterrows():
    print d["year"]
    
for d in df.head().iteritems():
    print d
    
for i,d in df.head().iterrows():
    print d["year"]
    
for i,d in df.head().iterrows():
    print i, d["year"]
    
for i,d in df.head().iterrows():
    print i, d["year"]
    
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites is not np.NaN:
        cites = cites.split(",")
    else:
        cites = []
        
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites is not np.NaN:
        cites = cites.split(",")
    else:
        cites = []
        print "Cites: ", cites
        
df
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != np.NaN:
        cites = cites.split(",")
    else:
        cites = []
        print "Cites: ", cites
        
df.dtypes = ['int64','str']
df.head()["citedby"]
df.head()["citedby"].astype('str')
a = ""
a.split(,)
a.split(",")
a = None
a.split(",")
df["citedby"].fillna("")
df["citedby"].head().fillna("")
df["citedby"].head()
df["citedby"] = df["citedby"].fillna(None)
df.head()
df["citedby"] = df["citedby"].fillna("")
df.head()
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
        print "Cites: ", cites
        
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
        print "Cites: ", cites
        
df_pmid
df_p = df_pmid
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
        print "Cites: ", cites
        for c in cites:
            c_year = df.ix[[int(c)]]["year"]
            print c_year
            
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
        print "Cites: ", cites
        for c in cites:
            c_year = df.ix[[int(c)]]["year"]
            print "C_year: ", c_year
            
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    print "Cites: ", cites
    for c in cites:
        c_year = df.ix[[int(c)]]["year"]
        print "C_year: ", c_year
        
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    print "Cites: ", cites
    for c in cites:
        c_year = df.ix[[int(c)],["year"]]
        print "C_year: ", c_year
        
df.head().values)(
df.head().values()
df.head().values
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    print "Cites: ", cites
    for c in cites:
        c_year = df.ix[[int(c)],["year"]]
        print "C_year: ", c_year.values()
        
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    print "Cites: ", cites
    for c in cites:
        c_year = df.ix[[int(c)],["year"]]
        print "C_year: ", c_year.values
        
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    print "Cites: ", cites
    for c in cites:
        c_year = df.ix[int(c),"year"]
        print "C_year: ", c_year.values
        
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    print "Cites: ", cites
    for c in cites:
        c_year = df.ix[int(c),"year"]
        print "C_year: ", c_year
        
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    print "Cites: ", cites
    for c in cites:
        c_year = df.ix[int(c),"year"]
        print "C_year: ", c_year
        d_dict = {'Source': i, 'Target': c, 'source_year':d["year"], 'target_year':c_year, 'weight':0.0}
        
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    print "Cites: ", cites
    for c in cites:
        c_year = df.ix[int(c),"year"]
        print "C_year: ", c_year
        d_dict = {'Source': i, 'Target': c, 'source_year':d["year"], 'target_year':c_year, 'weight':0.0}
        df_p.append(d_dict, ignore_index=True)
        
df_p
d_dict
df_p.append(d_dict, ignore_index=True)
df_p
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    print "Cites: ", cites
    for c in cites:
        c_year = df.ix[int(c),"year"]
        print "C_year: ", c_year
        d_dict = {'Source': i, 'Target': c, 'source_year':d["year"], 'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
        df_p.append(d_dict, ignore_index=True)
        
d_list = []
for i,d in df.head().iterrows():
    print i, d["year"]
    print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    print "Cites: ", cites
    for c in cites:
        c_year = df.ix[int(c),"year"]
        print "C_year: ", c_year
        d_dict = {'Source': i, 'Target': c, 'source_year':d["year"], 'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
        d_list.append(d_dict)
        
d_list
df_p
df_p.append(d_list, ignore_index=True)
df_pp = pd.DataFrame(d_list)
df_pp
df_pp = pd.DataFrame(d_list,columns=['Source', 'Target', 'source_year', 'target_year', 'weight',])
df_pp
df_pp = pd.DataFrame(d_list,columns=['Source', 'Target', 'source_year', 'target_year', 'weight','norm_weight'])
df_pp
d_list
d_list = []
for i,d in df.iterrows():
    #print i, d["year"]
    #print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    #print "Cites: ", cites
    for c in cites:
        c_year = df.ix[int(c),"year"]
        #print "C_year: ", c_year
        d_dict = {'Source': i, 'Target': c, 'source_year':d["year"], 'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
        d_list.append(d_dict)
        
df.head().index
10587346 in df.head().index
20800420 in df.head().index
for i,d in df.iterrows():
    #print i, d["year"]
    #print d["citedby"]
    cites = d["citedby"]
    if cites != "":
        cites = cites.split(",")
    else:
        cites = []
    #print "Cites: ", cites
    for c in cites:
        if c in df.index:c_year = df.ix[int(c),"year"]
        #print "C_year: ", c_year
        d_dict = {'Source': i, 'Target': c, 'source_year':d["year"], 'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
        d_list.append(d_dict)
        
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
            d_dict = {'Source': i, 'Target': c, 'source_year':d["year"], 'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
            d_list.append(d_dict)
            
d_list
d_list = [
]
d_list = []
d_list
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
            d_dict = {'Source': i, 'Target': c, 'source_year':d["year"], 'target_year':c_year, 'weight':0.0,'norm_weight':0.0}
            d_list.append(d_dict)
            
d_list[0]
len(d_list)
df_pp = pd.DataFrame(d_list,columns=['Source', 'Target', 'source_year', 'target_year', 'weight','norm_weight'])
df_pp
df_pp.head
df_pp.head()
df_pp.to_csv("SOURCE_TARGET_SY_TY_W_NW.tsv", sep="\t")
df_pp.head()
df_pp.head()["weight"]
df_pp.head().groupby(["target_year","source_year"]).count()
df_pp.head().groupby(["target_year"]).count()
df_pp.head().groupby(["Target"]).count()
df_pp.head().groupby(["target_year","source_year"]).count()
df_pp.head().groupby(["target_year","source_year"])["weight"].count()
t = df_pp.head().groupby(["target_year","source_year"])["weight"].count()
t
t.index
t.name
t
t = pd.DataFrame(df_pp.head().groupby(["target_year","source_year"])["weight"].count())
t
t.columns
t.columns = ["counts"]
t
t = df_pp.head().groupby(["target_year","source_year"])["weight"].count()
t[0]
t.ix[(2011,2010)]
t = df_pp.head().groupby(["source_year","target_year"])["weight"].count()
t
t.ix[(2010,2011)]
t.ix[(2010,2013)]
df_yp_grp = df_pp.groupby(["source_year","target_year"])["weight"].count()
df_yp_grp
df_yp_grp.head()
df_yp_grp[2000]
df_yp_grp[2000].sum()
df_yp_grp[2000]
df_yp_grp[2000].apply(lambda t: print t)
df_yp_grp[2000].apply(lambda t: print t; return t)
df_yp_grp[2000].apply(lambda t: return t)
df_yp_grp[2000].apply(lambda t: t)
df_yp_grp[2000].apply(lambda t: t/100)
df_yp_grp[2000].apply(lambda t: t/100.0)
df_yp_grp[2000].apply(lambda t: t.index)
df_yp_grp[2000]
df_yp_grp.apply(lambda t: t.index)
df_yp_grp.apply(lambda t: t)
def test(r):
    print r
    return 0
df_yp_grp.apply(test)
df_yp_grp.head().apply(test)
def test(r):
    print r
    total = r["source_year"].sum()
    return r*1.0/total
df_yp_grp.head().apply(test)
def test(r):
    print r
    total = r[0].sum()
    return r*1.0/total
df_yp_grp.head().apply(test)
df_yp_grp.head().apply(test,axis=1)
def test(r):
    print "Row value: ", r
    total = r[0].sum()
    return r*1.0/total
df_yp_grp.head().apply(test)
def test(r):
    print "Row value: ", r
    total = r.sum()*1.0
    r = r.apply(lambda x: x/total)
    return r
df_yp_grp.head().apply(test)
df_yp_grp.head().sum()
30733/745777
30733.0/745777
df_yp_grp.apply(test)
df_yp_prob = df_yp_grp.apply(test)
df_yp_prob
df_yp_grp
df_yp_prob
def test(r):
    total = r.sum()*1.0
    r = r.apply(lambda x: x/total)
    print "Total: ", total
    return r
df_yp_prob = df_yp_grp.apply(test)
df_yp_prob.head()
df_yp_prob = df_yp_grp["target_year"].apply(test)
df_yp_grp
df_yp_grp = pd.DataFrame(df_yp_grp)
df_yp_grp
df_yp_grp.columns = ["counts"]
df_yp_grp
df_yp_grp.head()
df_yp_prob = df_yp_grp.apply(test)
df_yp_prob = df_yp_grp.apply(test,axis=1)
df_yp_prob = df_yp_grp.head().apply(test,axis=1)
df_yp_prob
def test(r):
    total = r.sum()*1.0
    r = r.apply(lambda x: x/total)
    print "Total: ", total
    print "Row: ", r
    return r
df_yp_prob = df_yp_grp.head().apply(test,axis=1)
df_yp_grp.head()[df_yp_grp.index[0]].sum()
df_yp_grp.head()[df_yp_grp.index].sum()
df_yp_grp.head().groupby(df_yp_grp.index[0]).sum()
df_yp_grp.head().groupby("source_year").sum()
df_yp_grp
df_yp_grp[0]
df_yp_grp.iloc
df_yp_grp.irow[0]
df_yp_grp.irow(0)
df_yp_grp.head()
df_yp_grp.to_csv("YEAR_PAIR_COUNTS.tsv",sep="\t",index_label=["source_year","target_year"])
df_pp.head()
df_pp[df_pp["source_year"] < 2009].size()
df_pp[df_pp["source_year"] < 2009].count()
df_pp.count()
df_pp = df_pp[df_pp["source_year"] < 2009].count()
df_pp
get_ipython().magic(u'save curr_code.py')
get_ipython().magic(u'save curr_code 0-264')
df_pp = pd.DataFrame(d_list,columns=['Source', 'Target', 'source_year', 'target_year', 'weight','norm_weight'])
df_yp_grp.groupby(level=["source_year"]).sum()
df_year_tot = df_yp_grp.groupby(level=["source_year"]).sum()
df_year_tot
df_yp_grp.apply(lambda x: x, axis=1)
df_yp_grp.apply(lambda x: x.name, axis=1)
df_yp_grp.apply(lambda x: x.index, axis=1)
df_yp_grp.apply(lambda x: x.label, axis=1)
test
test.__code__
test.__str__
test.__format__
test.__code__()
test.__code__
test.func_code
test.func_code.co_code
def test(r):
    print dir(r)
    return 0
df_yp_grp.head(2).apply(test, axis=1)
df_yp_grp.head()
df_year_tot
df_year_tot[2000]
df_year_tot.ix[2000]
df_year_tot.ix[2000,"counts"]
def test(r):
    print r.reset_index()
    return 0
df_yp_grp.head(2).apply(test, axis=1)
def test(r):
    print r.index
    return 0
df_yp_grp.head(2).apply(test, axis=1)
def test(r):
    print r.keys
    return 0
df_yp_grp.head(2).apply(test, axis=1)
def test(r):
    print r.keys()
    return 0
df_yp_grp.head(2).apply(test, axis=1)
def test(r):
    print r.name
    return 0
df_yp_grp.head(2).apply(test, axis=1)
def test(r):
    print r.name
    tot = df_year_tot.ix[r.name[0], "count"]
    return r*1.0/tot
df_yp_grp.head(2).apply(test, axis=1)
def test(r):
    print r.name
    tot = df_year_tot.ix[r.name[0]]
    return r*1.0/tot
df_yp_grp.head(2).apply(test, axis=1)
def test(r):
    print r.name
    tot = df_year_tot.ix[r.name[0]]
    print r.name[0], tot
    return r*1.0/tot
df_yp_grp.head(2).apply(test, axis=1)
df_year_tot
df_yp_grp.head(20).apply(test, axis=1)
df_yp_grp.apply(test, axis=1)
df_yp_grp["weight"] = df_yp_grp.apply(test, axis=1)
df_yp_grp[["weight"]] = df_yp_grp.apply(test, axis=1)
df_yp_grp
def test(r):
    tot = df_year_tot.ix[r.name[0]]
    return r*1.0/tot
df_yp_grp[["weight"]] = df_yp_grp[["count"]].apply(test, axis=1)
df_yp_grp
df_yp_grp[["weight"]] = df_yp_grp[["counts"]].apply(test, axis=1)
df_yp_grp
df_yp_grp.to_csv("YEAR_PAIR_COUNTS.tsv",sep="\t",index_label=["source_year","target_year"])
df_pp.head()
df_pp.head()["Target"].groupby("Target").count()
df_pp.head().groupby("Target").count()
df_pp.head().groupby("Target")[["Target"]].count()
df_pp.head()[["Target"]].groupby("Target").count()
df_pp.head()[["Target"]]
df_target_count = df_pp[["Target"]].groupby("Target").count()
df_target_count.head()
df_target_count.columns
df_target_count.columns = ["total_cited"]
df_target_count.head()
df_pp.head()
def norm_weight(r):
    norm_f = df_target_count.ix[r["Target"],"total_cited"]
    r["weight"] = df_yp_grp.ix[(r["source_year"],r["target_year"]), "weight"]
    r["norm_weight"] = r["weight"]/norm_f
    return r
df_pp.head().apply(norm_weight, axis=1)
df_yp_grp.ix[(2010,2011)]
df_target_count.ix[22053223,"total_cited"]
0.536136/31
df_pp_weights = df_pp.apply(norm_weight, axis=1)
df_pp_weights.head()
df_pp_weights.count
df_pp_weights.to_csv("SOURCE_TARGET_SY_TY_ALL_WEIGHTS.tsv",sep="\t",index=False)
np.log(10)
np.log10(10)
def norm_weight(r):
    norm_f = df_target_count.ix[r["Target"],"total_cited"]
    r["weight"] = df_yp_grp.ix[(r["source_year"],r["target_year"]), "weight"]
    r["norm_weight"] = -np.log10(r["weight"])/norm_f
    return r
def norm_weight(r):
    norm_f = df_target_count.ix[r["Target"],"total_cited"]
    r["norm_weight"] = -np.log10(r["weight"])/norm_f
    return r
 df_pp.head().apply(norm_weight, axis=1)
def norm_weight(r):
    norm_f = df_target_count.ix[r["Target"],"total_cited"]
    r["norm_weight"] = -np.log10(r["weight"])/norm_f
    return r
 df_pp.head().apply(norm_weight, axis=1)
def norm_weight(r):
    norm_f = df_target_count.ix[r["Target"],"total_cited"]
    r["norm_weight"] = -np.log10(r["weight"])/norm_f
    return r
 df_pp.head().apply(norm_weight, axis=1)
df_pp.head().apply(norm_weight, axis=1)
df_pp_weights.head().apply(norm_weight, axis=1)
df_target_count.ix[22053223,"total_cited"]
-log(0.536136)/31
-np.log10(0.536136)/31
df_pp_weights1 = df_pp_weights.apply(norm_weight, axis=1)
df_pp_weights1.head()
df_pp_weights1.to_csv("SOURCE_TARGET_SY_TY_ALL_WEIGHTS_1.tsv",sep="\t",index=False)
df_pp_weights1.head()