import math
import matplotlib.pyplot as plt
import networkx as nx
import csv
import webbrowser
import folium
from fh1 import FibonacciHeap



class city:
    def __init__(self,no,name,lat,long):
        self.no=no
        self.name=name
        self.latitude=lat
        self.longtitude=long

class graph:
     def __init__(self,g):
         self.g=g

     def distance(self,lat1,lon1,lat2,lon2):
        R = 6371
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)          
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        dis=R*c
        return (dis)
        
     def edge(self):
         f=open("cities.csv","rt")
         fp=csv.reader(f)
         j=1
         for i in fp:
             self.g.add_node(j,data=city(int(i[0]),i[1],float(i[2]),float(i[3])))
             j+=1         
             
     def draw(self):
        m = folium.Map(location=[self.g.nodes[1]['data'].latitude, self.g.nodes[1]['data'].longtitude], zoom_start=5.5)

        for node in self.g.nodes:
            folium.Marker(
                location=[self.g.nodes[node]['data'].latitude, self.g.nodes[node]['data'].longtitude],
                popup=self.g.nodes[node]['data'].name
            ).add_to(m)

        for edge in self.g.edges:
            u, v = edge
            lat1, lon1 = self.g.nodes[u]['data'].latitude, self.g.nodes[u]['data'].longtitude
            lat2, lon2 = self.g.nodes[v]['data'].latitude, self.g.nodes[v]['data'].longtitude
            folium.PolyLine(
                locations=[(lat1, lon1), (lat2, lon2)],
                color='red',
                weight=2# Adjust the weight for better visualization
            ).add_to(m)

        return m


   
     def connect(self):
         self.g.add_edge(1,5,weight=self.distance(self.g.nodes[1]['data'].latitude,   self.g.nodes[1]['data'].longtitude,    self.g.nodes[5]['data'].latitude,    self.g.nodes[5]['data'].longtitude))
         self.g.add_edge(1,15,weight=self.distance(self.g.nodes[1]['data'].latitude,   self.g.nodes[1]['data'].longtitude,    self.g.nodes[15]['data'].latitude,    self.g.nodes[15]['data'].longtitude))
         self.g.add_edge(1,21,weight=self.distance(self.g.nodes[1]['data'].latitude,   self.g.nodes[1]['data'].longtitude,    self.g.nodes[21]['data'].latitude,    self.g.nodes[21]['data'].longtitude))
         self.g.add_edge(1,10,weight=self.distance(self.g.nodes[1]['data'].latitude,   self.g.nodes[1]['data'].longtitude,    self.g.nodes[10]['data'].latitude,    self.g.nodes[10]['data'].longtitude))
         self.g.add_edge(2,11,weight=self.distance(self.g.nodes[2]['data'].latitude,   self.g.nodes[2]['data'].longtitude,    self.g.nodes[11]['data'].latitude,    self.g.nodes[11]['data'].longtitude))
         self.g.add_edge(2,13,weight=self.distance(self.g.nodes[2]['data'].latitude,   self.g.nodes[2]['data'].longtitude,    self.g.nodes[13]['data'].latitude,    self.g.nodes[13]['data'].longtitude))
         self.g.add_edge(2,17,weight=self.distance(self.g.nodes[2]['data'].latitude,   self.g.nodes[2]['data'].longtitude,    self.g.nodes[17]['data'].latitude,    self.g.nodes[17]['data'].longtitude))
         self.g.add_edge(2,8,weight=self.distance(self.g.nodes[2]['data'].latitude,   self.g.nodes[2]['data'].longtitude,    self.g.nodes[8]['data'].latitude,    self.g.nodes[8]['data'].longtitude))
         self.g.add_edge(3,17,weight=self.distance(self.g.nodes[3]['data'].latitude,   self.g.nodes[3]['data'].longtitude,    self.g.nodes[17]['data'].latitude,    self.g.nodes[17]['data'].longtitude))
         self.g.add_edge(3,12,weight=self.distance(self.g.nodes[3]['data'].latitude,   self.g.nodes[3]['data'].longtitude,    self.g.nodes[12]['data'].latitude,    self.g.nodes[12]['data'].longtitude))
         self.g.add_edge(4,20,weight=self.distance(self.g.nodes[4]['data'].latitude,   self.g.nodes[4]['data'].longtitude,    self.g.nodes[20]['data'].latitude,    self.g.nodes[20]['data'].longtitude))
         self.g.add_edge(4,6,weight=self.distance(self.g.nodes[4]['data'].latitude,   self.g.nodes[4]['data'].longtitude,    self.g.nodes[6]['data'].latitude,    self.g.nodes[6]['data'].longtitude))
         self.g.add_edge(17,18,weight=self.distance(self.g.nodes[17]['data'].latitude,   self.g.nodes[17]['data'].longtitude,    self.g.nodes[18]['data'].latitude,    self.g.nodes[18]['data'].longtitude))
         self.g.add_edge(5,10,weight=self.distance(self.g.nodes[5]['data'].latitude,   self.g.nodes[5]['data'].longtitude,    self.g.nodes[10]['data'].latitude,    self.g.nodes[10]['data'].longtitude))
         self.g.add_edge(5,21,weight=self.distance(self.g.nodes[5]['data'].latitude,   self.g.nodes[5]['data'].longtitude,    self.g.nodes[21]['data'].latitude,    self.g.nodes[21]['data'].longtitude))
         self.g.add_edge(6,20,weight=self.distance(self.g.nodes[6]['data'].latitude,   self.g.nodes[6]['data'].longtitude,    self.g.nodes[20]['data'].latitude,    self.g.nodes[20]['data'].longtitude))
         self.g.add_edge(6,11,weight=self.distance(self.g.nodes[6]['data'].latitude,   self.g.nodes[6]['data'].longtitude,    self.g.nodes[11]['data'].latitude,    self.g.nodes[11]['data'].longtitude))
         self.g.add_edge(6,13,weight=self.distance(self.g.nodes[6]['data'].latitude,   self.g.nodes[6]['data'].longtitude,    self.g.nodes[13]['data'].latitude,    self.g.nodes[13]['data'].longtitude))
         self.g.add_edge(7,9,weight=self.distance(self.g.nodes[7]['data'].latitude,   self.g.nodes[7]['data'].longtitude,    self.g.nodes[9]['data'].latitude,    self.g.nodes[9]['data'].longtitude))
         self.g.add_edge(7,16,weight=self.distance(self.g.nodes[7]['data'].latitude,   self.g.nodes[7]['data'].longtitude,    self.g.nodes[16]['data'].latitude,    self.g.nodes[16]['data'].longtitude))
         self.g.add_edge(7,19,weight=self.distance(self.g.nodes[7]['data'].latitude,   self.g.nodes[7]['data'].longtitude,    self.g.nodes[19]['data'].latitude,    self.g.nodes[19]['data'].longtitude))
         self.g.add_edge(8,14,weight=self.distance(self.g.nodes[8]['data'].latitude,   self.g.nodes[8]['data'].longtitude,    self.g.nodes[14]['data'].latitude,    self.g.nodes[14]['data'].longtitude))
         self.g.add_edge(8,11,weight=self.distance(self.g.nodes[8]['data'].latitude,   self.g.nodes[8]['data'].longtitude,    self.g.nodes[11]['data'].latitude,    self.g.nodes[11]['data'].longtitude))
         self.g.add_edge(9,16,weight=self.distance(self.g.nodes[9]['data'].latitude,   self.g.nodes[9]['data'].longtitude,    self.g.nodes[16]['data'].latitude,    self.g.nodes[16]['data'].longtitude))
         self.g.add_edge(10,14,weight=self.distance(self.g.nodes[10]['data'].latitude,   self.g.nodes[10]['data'].longtitude,    self.g.nodes[14]['data'].latitude,    self.g.nodes[14]['data'].longtitude))
         self.g.add_edge(10,17,weight=self.distance(self.g.nodes[10]['data'].latitude,   self.g.nodes[10]['data'].longtitude,    self.g.nodes[17]['data'].latitude,    self.g.nodes[17]['data'].longtitude))
         self.g.add_edge(12,16,weight=self.distance(self.g.nodes[12]['data'].latitude,   self.g.nodes[12]['data'].longtitude,    self.g.nodes[16]['data'].latitude,    self.g.nodes[16]['data'].longtitude))
         self.g.add_edge(12,18,weight=self.distance(self.g.nodes[12]['data'].latitude,   self.g.nodes[12]['data'].longtitude,    self.g.nodes[18]['data'].latitude,    self.g.nodes[18]['data'].longtitude))
         self.g.add_edge(13,16,weight=self.distance(self.g.nodes[13]['data'].latitude,   self.g.nodes[13]['data'].longtitude,    self.g.nodes[16]['data'].latitude,    self.g.nodes[16]['data'].longtitude))
         self.g.add_edge(14,17,weight=self.distance(self.g.nodes[14]['data'].latitude,   self.g.nodes[14]['data'].longtitude,    self.g.nodes[17]['data'].latitude,    self.g.nodes[17]['data'].longtitude))
         self.g.add_edge(14,15,weight=self.distance(self.g.nodes[14]['data'].latitude,   self.g.nodes[14]['data'].longtitude,    self.g.nodes[15]['data'].latitude,    self.g.nodes[15]['data'].longtitude))
         self.g.add_edge(15,21,weight=self.distance(self.g.nodes[15]['data'].latitude,   self.g.nodes[15]['data'].longtitude,    self.g.nodes[21]['data'].latitude,    self.g.nodes[21]['data'].longtitude))
         self.g.add_edge(16,18,weight=self.distance(self.g.nodes[16]['data'].latitude,   self.g.nodes[16]['data'].longtitude,    self.g.nodes[18]['data'].latitude,    self.g.nodes[18]['data'].longtitude))
         
         
         self.g.add_edge(4,22,weight=self.distance(self.g.nodes[4]['data'].latitude,   self.g.nodes[4]['data'].longtitude,    self.g.nodes[22]['data'].latitude,    self.g.nodes[22]['data'].longtitude))
         self.g.add_edge(22,20,weight=self.distance(self.g.nodes[22]['data'].latitude,   self.g.nodes[22]['data'].longtitude,    self.g.nodes[20]['data'].latitude,    self.g.nodes[20]['data'].longtitude))
         self.g.add_edge(25,7,weight=self.distance(self.g.nodes[25]['data'].latitude,   self.g.nodes[25]['data'].longtitude,    self.g.nodes[7]['data'].latitude,    self.g.nodes[7]['data'].longtitude))
         self.g.add_edge(24,23,weight=self.distance(self.g.nodes[24]['data'].latitude,   self.g.nodes[24]['data'].longtitude,    self.g.nodes[23]['data'].latitude,    self.g.nodes[23]['data'].longtitude))
         self.g.add_edge(23,7,weight=self.distance(self.g.nodes[23]['data'].latitude,   self.g.nodes[23]['data'].longtitude,    self.g.nodes[7]['data'].latitude,    self.g.nodes[7]['data'].longtitude))
         self.g.add_edge(10,26,weight=self.distance(self.g.nodes[10]['data'].latitude,   self.g.nodes[10]['data'].longtitude,    self.g.nodes[26]['data'].latitude,    self.g.nodes[26]['data'].longtitude))
         self.g.add_edge(26,5,weight=self.distance(self.g.nodes[26]['data'].latitude,   self.g.nodes[26]['data'].longtitude,    self.g.nodes[5]['data'].latitude,    self.g.nodes[5]['data'].longtitude))
         self.g.add_edge(23,25,weight=self.distance(self.g.nodes[23]['data'].latitude,  self.g.nodes[23]['data'].longtitude,     self.g.nodes[25]['data'].latitude,   self.g.nodes[25]['data'].longtitude)) 
         self.g.add_edge(26,3,weight=self.distance(self.g.nodes[26]['data'].latitude,   self.g.nodes[26]['data'].longtitude,     self.g.nodes[3]['data'].latitude,   self.g.nodes[3]['data'].longtitude))

     def connectsp(self,path):
        tw=0
        for i in range(len(path)):
                      if(i==len(path)-1):
                                  break
                      j=i+1
                      self.g.add_edge(path[i],path[j],weight=self.distance(self.g.nodes[path[i]]['data'].latitude,   self.g.nodes[path[i]]['data'].longtitude,    self.g.nodes[path[j]]['data'].latitude,    self.g.nodes[path[j]]['data'].longtitude))
                      tw+=self.distance(self.g.nodes[path[i]]['data'].latitude,   self.g.nodes[path[i]]['data'].longtitude,    self.g.nodes[path[j]]['data'].latitude,    self.g.nodes[path[j]]['data'].longtitude)
        return tw



        
             

     def dijkstra(self,source, sink = None):
        distance={}
        visited={}
        heap1={}
        heap = FibonacciHeap()
        for node in self.g.nodes:
            
            
            distance[node] = float('inf')
            heap1[node] = heap.insert(float('inf'),node) 
       
 
               

        distance[source] = 0
        heap.decrease_key(heap1[source], 0)

        while heap.total_nodes:
            current = heap.extract_min()
            

            #early exit
            if sink and current == sink:
                break

            for neighbor in self.g.neighbors(current.value) :
                   weight = self.g[current.value][neighbor]['weight']
                   if distance[current.value] + weight < distance[neighbor]:
                        distance[neighbor] = distance[current.value] + weight
                        visited[neighbor]=current.value
                        heap.decrease_key(heap1[neighbor], distance[neighbor])
                

        
        path=[]
        current=sink
        while current is not None:
            print(current)
            path.insert(0,current)
            current=visited.get(current)
        return path










 
   
