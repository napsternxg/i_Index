"""
# Social and Economic Networks CS 598 HS
# Assignment 2 Part C 2
# Author: Shubhanshu Mishra
"""

import snap
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np

"""
Load data from the tab seperated file. It is important that each line only represents an edge. No comments in file are allowed as opposed to the case of Snap.py
"""
def loadData(filename):
    data = None
    data = snap.LoadEdgeList(snap.PUNGraph,filename,0,1)
    return data
    
    
"""
Get simple graph statistics.
"""
def getSummary(data):
    summary = dict()
    summary["Nodes"] = data.GetNodes()
    summary["Edges"] = data.GetEdges()
    #summary["Clustering Coeff"] = snap.GetClustCf(data)
    print summary
    #summary["Triads"] = snap.GetTriads(data)
    print summary
    return summary

"""
Get node degree indexed by node name.
"""
def getNodeDeg(data):
    node_deg = dict()
    for node in data.Nodes():
        node_deg[node.GetId()] = node.GetOutDeg()
    return node_deg

"""
Get degree distribution
"""
def getDegreeDist(node_deg):
    degDist = dict()
    for n in node_deg.iteritems():
        if n[1] not in degDist:
            degDist[n[1]] = 0
        degDist[n[1]] += 1
    return OrderedDict(sorted(degDist.iteritems(), key=lambda x: x[0])) # Sort by key so that it is easier while plotting.

"""
Plot the node degree distribution. 
"""
def plotDegDist(degDist,title='',loglog=False):
    plt.clf()
    plt.title(title)
    """
    Use a sorted dictionary so that the plot is made using the order of the keys.
    """
    if loglog:
        plt.loglog(degDist.keys(), degDist.values(), 'ro-')
    else:
        plt.plot(degDist.keys(), degDist.values(), 'ro-')
    plt.ylabel('Degree Count')
    plt.xlabel('Degree')
    plt.show()

   


"""
Helper function to print the dictionary. 
"""
def printTable(data_dict, table_format, table_header_tpl,n=None):
    i = 0
    print table_format % table_header_tpl
    for k in data_dict:
        if n is not None and i > n:
            break
        print table_format % (k,data_dict[k])
        i += 1


"""
Perform standard process on each network.
"""
def procData(data,title='', plot=False):
    print title
    if data is not None:
        print "Graph Summary"
        printTable(getSummary(data),"%s\t%s", ("Property", "Count"))
        node_deg = getNodeDeg(data)
        print "Degree Distribution"
        degDist = getDegreeDist(node_deg)
        print degDist
        if plot:
            plotDegDist(degDist,title=title)
            plotDegDist(degDist,title=title,loglog=True)
        avg_clust_coeff = snap.GetClustCf(data)
        print "Average clustering coefficient: ", avg_clust_coeff
        return degDist


"""
Cumulative Frequency
"""
def getF(degDist):
    x = degDist.keys()
    y = degDist.values()
    norm_y = sum(y)
    cfd = OrderedDict()
    for i in range(len(x)):
        cfd[x[i]] = sum(y[:i+1])*1.0/norm_y
    return cfd

"""
Get X,Y,C
"""
import math
def getEquationVals(cfd,m,alpha=0.01):
    Y = []
    X = []
    C = []
    X1 = []
    #print"CFD: ", cfd
    for d in cfd.keys()[:-1]:
        #print d, cfd[d]
        Y.append(math.log(1-cfd[d]))
        x = math.log(d +  (2*alpha*m)/(1-alpha))
        c = math.log(m +  (2*alpha*m)/(1-alpha))
        X.append(x)
        C.append(c)
        X1.append(-x+c)
    return X,X1,Y,C

"""
Run least squares lin reg
"""
def linReg(cfd,m,alpha=0.01):
    X,X1,Y,C = getEquationVals(cfd,m,alpha)
    A = np.vstack([X1]).T
    Y = np.array(Y)
    gamma = np.linalg.lstsq(A,Y) # m = 2/1-alpha1
    #print "M: ", gamma
    alpha1 = 1-2.0/gamma[0]
    return alpha1[0]

"""
Run least squares lin reg
"""
def linReg1(cfd,m,alpha=0.01):
    X,X1,Y,C = getEquationVals(cfd,m,alpha)
    p,V = np.polyfit(X,Y,1) # m = 2/1-alpha1
    gamma = p
    print "P: ", p
    alpha1 = 1-2.0/p
    return alpha1


"""
Run least squares lin reg
"""
from scipy import stats
def linReg2(cfd,m,alpha=0.01):
    X,X1,Y,C = getEquationVals(cfd,m,alpha)
    slope, intercept, r_value, p_value, std_er = stats.linregress(X,Y) # m = 2/1-alpha1
    p = slope
    print "P: ", slope, intercept, r_value, p_value, std_er
    alpha1 = 1-2.0/p
    return alpha1   
    
    
    

"""
Run Experiment
"""
def runExp(data):
    node_deg = getNodeDeg(data)
    print "Degree Distribution"
    degDist = getDegreeDist(node_deg)
    cfd = getF(degDist)
    x = degDist.keys()
    y = degDist.values()
    m = sum([x[i]*y[i] for i in range(len(x))])/(2.0*sum(y)) # Average degree/2
    alpha0 = np.arange(0.999,0.99999,0.00005)
    alpha1 = []
    for a0 in alpha0:
        a1 = linReg(cfd,m,a0)
        alpha1.append(a1)
    for i in range(len(alpha0)):
        print alpha0[i], alpha1[i]
    
    
def getEVCentrality(data):
  NIdEigenH = snap.TIntFltH()
  snap.GetEigenVectorCentr(data, NIdEigenH)
  evc_data = []
  with open("evc.dat", "wb+") as fp:
    # nodeid  eigen_vector_centrality
    for item in NIdEigenH:
      print >> fp, "%d\t%f" % (item, NIdEigenH[item])
      evc_data.append((item, NIdEigenH[item]))
  s_evc = sorted(evc_data, key=lambda x: x[1],reverse=True)
  print s_evc[:10]
  print s_evc[:-10]
    

"""
Main function to run the code.
"""
if __name__ == "__main__":
    
    data = loadData("data.txt")
    print getSummary(data)
    getEVCentrality(data)
    #snap.PrintInfo(data,"PUBMED citation network", "pmid_network_stats_fast.txt", True)

    print "Running experiment on PUBMED 2010 dataset"
    #runExp(data)
    """
    data = loadData("Email-Enron.txt")
    print "Running experiment on Enron dataset"
    runExp(data)
    """
    print "Done."
        
    

