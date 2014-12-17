import pandas as pd

def populateTable(filename,outfile):
    f = open(filename)
    cite_edg = []
    id_dict = {}
    INDEX = "";
    TITLE = "";
    AUTHORS = "";
    YEAR = "";
    PUB_VENUE = "";
    REF_ID = [];
    REF_NUM = 0;
    ABSTRACT = "";
    i = 0;
    print("Adding papers:")
    for rline in f:
        line = rline.decode("utf-8").rstrip();
        if line.startswith('#index'):
            INDEX += line.lstrip('#index');
            INDEX = int(INDEX)
        if line.startswith('#*'):
            TITLE += line.lstrip('#*');
        if line.startswith('#@'):
            AUTHORS += line.lstrip('#@');
        if line.startswith('#t'):
            YEAR += line.lstrip('#t');
            YEAR = int(YEAR)
        if line.startswith('#c'):
            PUB_VENUE += line.lstrip('#c');
        if line.startswith('#%'):
            r = line.lstrip('#%').strip()
            if len(r) > 0:
              REF_ID.append(int(r))
            REF_NUM = REF_NUM+1;
        if line.startswith('#!'):
            ABSTRACT += line.lstrip('#!');
        if line=="":
            if INDEX not in id_dict:
              id_dict[INDEX] = [None,[]]
            id_dict[INDEX][0] = YEAR
            #print INDEX + ", " + TITLE;
            #print >> outf, '%s\t%s\t%s' % (INDEX, YEAR, ",".join(REF_ID));
            for r in REF_ID:
              if r not in id_dict:
                id_dict[r] = [None,[]]
              id_dict[r][1].append(INDEX)
            INDEX = "";
            TITLE = "";
            AUTHORS = "";
            YEAR = "";
            PUB_VENUE = "";
            REF_ID = [];
            REF_NUM = 0;
            ABSTRACT = "";
            i += 1
        if i%10000==0:
            print ".",
    f.close()
    outf = open(outfile,"wb+")
    print >> outf, "%s\t%s\t%s" % ('PMID', 'year', 'citedby')
    for k in id_dict:
      if id_dict[k][0] is not None:
        print >> outf, "%s\t%s\t%s" % (k, id_dict[k][0],",".join([str(k) for k in id_dict[k][1]]))
    outf.close()

import sys, os
if __name__ == "__main__":
  print "Arguments: ", sys.argv
  if(len(sys.argv) < 3):
    print "%s <inputfile> <outputfile>" % (os.path.basename(__file__))
    exit(0)
  populateTable(sys.argv[1],sys.argv[2])

