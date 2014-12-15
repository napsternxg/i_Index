# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("PMID_YEAR_CITED_COUNT.tsv",sep="\t")
df.head()
grouped = df.groupby('PMID')
grouped = df.groupby('pmid')
df.head()
df.columns  = ["PMID","CITEDBY","YEAR"]
df.head()
grouped = df.groupby('PMID')
df_h = grouped['CITEDBY'].count()
df_h = grouped['CITEDBY'].count()
df_h.head()
df_h.sort(ascending=False).head()
df_h.sort(ascending=False).head()
dh_h.columns
df_h.columns
df_h.column
df_h.index
df_h.keys
df_h.sort(1,ascending=False)
df_h.sort(1,ascending =False)
df_h.sort()
df_hs = df_h.sort()
df_hs
df_hs.head()
df_hs = df_h.sort(0)
df_hs.head()
df_h.head)(
df_h.head)(
df_h.head()
df_h.tail()
dh_h
df_h.
df_h
df
df_pyj = pd.read_csv("pmid_year_journal.tsv",sep="\t",index_col='PMID')
df_pyj.head()
df = pd.read_csv("PMID_YEAR_CITED_COUNT.tsv",sep="\t", header=None, names=["PMID","CITEDBY","YEAR"])
df.head()
df.columns
df.columns = ['PMID', 'YEAR', 'CITEDBY']
df.head()
df = pd.read_csv("PMID_CITEDBY_YEAR.tsv",sep="\t", header=None, names=["PMID","CITEDBY","YEAR"])
df.head()
df = pd.read_csv("PMID_CITEDBY_YEAR.tsv",sep="\t")
df.head()