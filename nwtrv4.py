'''
Created on 24-May-2018

@author: rahul
'''
import py2neo
from neomodel import db
from py2neo import Graph,Node,Relationship
from py2neo.ogm import RelatedFrom, GraphObject, RelatedTo
from pandas import DataFrame
from py2neo.database import Cursor
from py2neo.types import Walkable
from platform import processor
from py2neo import cypher_escape
from neo4jrestclient.traversals import Traversal
py2neo.authenticate("localhost:7474/browser/", "admin", "password")
graph=Graph("http://localhost:7474/browser")
class nw4:
    def ntrv(self):
        lst=[]
        empt=[]
        label_inp=raw_input("enter the label")
        res=True
        
        l=graph.run("match(n:"+label_inp+") return n.name").data()
        for i in l:
            print i
        k=l[2].values()[0]
        print k
        while(True):
            s=graph.run("match(n:"+label_inp+")-[r]->(m) where n.name={g} return type(r)",g=str(k)).data()
            if(s==empt):
                break
            else:
                '''for j in range(0,len(s)):
                    t=s[j].values()[0]
                    print t
                print(len(s))
               
                for i in range(0,len(s)):
                    s2=s[i].values()[0]
                    lst.append(s2)
                print lst'''
                for j in range(0,len(s)):
                    t=s[j].values()[0]
                    print t
                    lst.append(t)
                rel_inp=raw_input("enter choice")  
                if rel_inp in lst:
                    z=graph.run("match(n:"+label_inp+")-[r:"+rel_inp+"]->(m) where n.name={g1} return m.name",g1=str(k)).data()
                    z2=z[0].values()[0]
                    print z2
                
                z1=str(z2)
                nwlb=graph.run("MATCH (r)  WHERE r.name={z1} RETURN labels(r)",z1=str(z2)).data()
                d=nwlb[0].values()[0]
                label_inp=d[0]
                k=z2
                    
            
                
                
           
                        
nw4t=nw4()
nw4t.ntrv()
