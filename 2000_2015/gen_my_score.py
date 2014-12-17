df_tcs = df_pp.groupby(["Source","target_year"]).agg({"source_year":"first","weight":"count"})
