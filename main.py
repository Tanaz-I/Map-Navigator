import tkinter as tk
from tkinter import ttk
import math
import matplotlib.pyplot as plt
import networkx as nx
import csv
import webbrowser
import folium
import Map as m
from tkinter.ttk import *


def graphplot(path):
    G=nx.Graph()
    m.g1=m.graph(G)
    m.g1.edge()
    tw=m.g1.connectsp(path)
    print(tw)
    folium_map=m.g1.draw()
    folium_map.save('graph_map1.html')
    webbrowser.open('graph_map1.html', new=2)  
        
    
def route():
    n1=sourcechoosen.get()
    n2=destchoosen.get()
    f=open("cities.csv","rt")
    fp=csv.reader(f)
    j=1
    for i in fp:
           if (n1==i[1]):
                   s=int(i[0])
           elif(n2==i[1]):
                   d=int(i[0])
                   
    f.close()
    path=m.g.dijkstra(s,d)
    print(path)
    graphplot(path)
   
        


k=[]
G=nx.Graph()
m.g=m.graph(G)
m.g.edge()
m.g.connect()
folium_map=m.g.draw()
folium_map.save('graph_map.html')
webbrowser.open('graph_map.html', new=2)
root=tk.Tk()
root.title("MAP NAVIGATOR")
root.geometry("500x300")

f=open("cities.csv","rt")
fp=csv.reader(f)
j=1
for i in fp:
    k.append(i[1])
f.close()




n1= tk.StringVar()
n2=tk.StringVar()
sourcechoosen = ttk.Combobox(root, width = 18,justify="center",textvariable = n1,state='readonly',height=15,font=("times new roman",23,"italic"))
sourcechoosen['values'] =k
destchoosen = ttk.Combobox(root, width = 18,justify="center",textvariable = n2,state='readonly',height=15,font=("times new roman",23,"italic"))
destchoosen['values'] =k
submit = tk.Button(root, text="Find Route",command=route,width=20,font=("times new roman",23,"bold"),justify="center",bg="black",fg="white")
sourcechoosen.grid(row=0, column=0, padx=10, pady=10)
destchoosen.grid(row=1, column=0, padx=10, pady=10)
submit.grid(row=2,column=0,padx=10, pady=10)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.mainloop()

