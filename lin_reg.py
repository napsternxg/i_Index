import statsmodels.api as sm
import pandas as pd
import numpy as np

def prepareDatFrame(filename="pmid_avg_age_sum.tsv"):
  df = pd.read_csv(filename,sep="\t",index_col=['pmid'])
  #df.head()
  """
  pmid    avg_c   min_y   max_y   age     sum_c
  """
  print "Finished data prep"
  return df

def trainModel(df):
  print "Start model training"
  y = df['sum_c']

  #X = df.drop(['Velocity_max_neg_acc_noNan','Velocity_min_pos_acc_noNan','cited_count','Journal', 'Year'],1)
  #X = df.drop(['Cited_Count','Journal', 'Year', 'log_Cited_Count'],1)
  X = df.drop(['sum_c'],1)
  print X.head()
  mod = sm.OLS(y,X)
  res = mod.fit()
  print res.summary()


if __name__ == "__main__":
  df = prepareDatFrame()
  trainModel(df)
