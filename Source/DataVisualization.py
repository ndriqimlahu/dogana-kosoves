# -*- coding: utf-8 -*-
"""
@author: Ndriqim Lahu
"""

from pandas import *
import pandas as pd
from matplotlib.pyplot import figure, plot, bar, pie, draw, scatter
import matplotlib.pyplot as plt

#DataVisualization

doganaData = pd.read_csv('Open_Data_Import_2021.csv')
print ("Leximi i fajllit nga Dogana e Kosovës:\n", doganaData)
print ("_________________________________________________________________________")

doganaData['Sasia']=pd.to_numeric(doganaData['Sasia'],errors='coerce')
doganaData['Vlera Mallrave']=pd.to_numeric(doganaData['Vlera Mallrave'],errors='coerce')
doganaData['Netweight']=pd.to_numeric(doganaData['Netweight'],errors='coerce')
doganaData['Taksa Doganës']=pd.to_numeric(doganaData['Taksa Doganës'],errors='coerce')
doganaData['Taksa Akcizës']=pd.to_numeric(doganaData['Taksa Akcizës'],errors='coerce')
doganaData['Taksa TVSH-së']=pd.to_numeric(doganaData['Taksa TVSH-së'],errors='coerce')

doganaD9 = doganaData.head(15).plot(kind='bar',y=['Taksa Doganës','Taksa Akcizës','Taksa TVSH-së'],rot=60)
print ("Grafiku sipas taksës së doganës, akcizës dhe tvsh-së:\n", doganaD9)
print ("_________________________________________________________________________")

doganaD10 = doganaData.dropna().head(15).plot(kind='bar',y=['Sasia','Vlera Mallrave','Netweight'],figsize=(6,6))
print ("Grafiku sipas sasisë, vlerës së mallrave dhe peshës neto:\n", doganaD10)
print ("_________________________________________________________________________")

muajt = ['Janar','Shkurt','Mars','Prill','Maj','Qershor','Korrik','Gusht','Shtator','Tetor','Nentor','Dhjetor']
doganaD11 = doganaData.dropna().head(12).plot(kind='pie',labels=muajt,autopct='%.02f',y='Taksa TVSH-së',figsize=(9,9),legend=False)
print ("Përqindja nga taksa tvsh-së e grumbulluar sipas muajve të vitit:\n", doganaD11)
print ("_________________________________________________________________________")

doganaD12 = doganaData.groupby('VITI').sum()
doganaD12 = doganaD12.drop(['MUAJI','Sasia','Vlera Mallrave','Netweight'],axis=1)
doganaD12 = doganaD12.stack().plot(kind='pie',autopct='%.2f',label="",y=['Taksa Doganës','Taksa Akcizës','Taksa TVSH-së'])
print ("Përqindja e taksave dhe vlerës së mallrave në total:\n", doganaD12)
print ("_________________________________________________________________________")

doganaD13 = doganaData.groupby('MUAJI').sum()
doganaD13 = doganaD13.drop(['VITI','Taksa Doganës','Taksa Akcizës','Taksa TVSH-së'],axis=1)
doganaD13 = doganaD13.unstack().plot(kind='pie',autopct='%.2f',label="",y=['Vlera Mallrave','Netweight'])
print ("Përqindja e vlerës së mallrave dhe peshës neto në total për 4 mujorin e vitit 2021:\n", doganaD13)
print ("_________________________________________________________________________")

fig = plt.figure()
ax = fig.add_subplot(3,1,1)
doganaD14 = doganaData.dropna().plot(kind='line',y='Taksa Doganës',color='r',figsize=(10,3))
ax = fig.add_subplot(3,1,2)
doganaD14 = doganaData.dropna().plot(kind='line',y='Taksa Akcizës',color='g',figsize=(10,3))
ax = fig.add_subplot(3,1,3)
doganaD14 = doganaData.dropna().plot(kind='line',y='Taksa TVSH-së',color='b',figsize=(10,3))
print ("Paraqitja e 3 grafeve për taksat në një figurë:\n", doganaD14)
print ("_________________________________________________________________________")

doganaD15 = doganaData.dropna().head(15).plot(kind='line',y=['Taksa Doganës','Taksa Akcizës','Taksa TVSH-së'])
print ("Paraqitja e taksave në një grafik të vetëm:\n", doganaD15)
print ("_________________________________________________________________________")