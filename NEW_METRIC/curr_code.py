# coding: utf-8

import networkx as nx
G = nx.DiGraph([1,2])
G = nx.DiGraph([(1,2)])
G
G.nodes()
G.edges()
int.bit_length
int.bit_length()
import sys
sys.maxint
import pandas as pd
df = pd.read_csv("PMID_2000_NONULL.tsv", sep="\t")
df_pmid = DataFrame(columns=("Source","Target","ssource_year","target_year","weight","norm_weight"))
df_pmid = pd.DataFrame(columns=("Source","Target","ssource_year","target_year","weight","norm_weight"))
df_pmid.append([1,2,3,4,5,6,7])
df_pmid = pd.DataFrame(columns=("Source","Target","source_year","target_year","weight","norm_weight"))
df_pmid.concat([1,2,3,4,5,6,7])
df_data = df
df_data
df = DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
df
s = df.xs(3)
s
df.append(s, ignore_index=True)
df.append([1,2,3,4], ignore_index=True)
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
df
df.append([[1,2,3,4]], ignore_index=True)
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
df.append((1,2,3,4), ignore_index=True)
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
df.add()
df.add([1,2,3,4])
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
df
df.ix[8] = [1,2,3,4]
df.loc[8] = [1,2,3,4]
df.iloc[8] = [1,2,3,4]
df.ix[8] = [1,2,3,4]
df.irow[8] = [1,2,3,4]
df.irow[5]
df.irow(5)
df.irow(8,[1,2,3,4])
df
df.append({A:1,B:2,C:3,D:4})
df.append({'A':1,'B':2,'C':3,'D':4})
df.append({'A':1,'B':2,'C':3,'D':4},ignore_index=True)
values = np.zeros(2, dtype='int32, float32, float32')
values
index = ['x', 'y']
columns = ['a','b','c']
df = pd.DataFrame.from_records(values, index=index, columns=columns)
df
df = pd.DataFrame.from_records(values, columns=columns)
df
get_ipython().magic(u'save data_preprocess 0-')
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