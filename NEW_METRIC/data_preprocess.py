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