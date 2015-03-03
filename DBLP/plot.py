import igraph as ig


g = ig.Graph.Read_Ncol("T_S_W.tsv", names=True, weights=True, directed=True)
layout = g.layout("lgl")
ig.plot(g,"DBLP.pdf",layout=layout)
