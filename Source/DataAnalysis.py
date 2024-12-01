# -*- coding: utf-8 -*-
"""
@author: Ndriqim Lahu
"""

from pandas import *
import pandas as pd
from numpy import *
import numpy as np

#DataAnalysis

doganaData = pd.read_csv('Open_Data_Import_2021.csv')
print ("Leximi i fajllit nga Dogana e Kosovës:\n", doganaData)
print ("_________________________________________________________________________")

doganaData['Sasia']=pd.to_numeric(doganaData['Sasia'],errors='coerce')
doganaData['Vlera Mallrave']=pd.to_numeric(doganaData['Vlera Mallrave'],errors='coerce')
doganaData['Netweight']=pd.to_numeric(doganaData['Netweight'],errors='coerce')
doganaData['Taksa Doganës']=pd.to_numeric(doganaData['Taksa Doganës'],errors='coerce')
doganaData['Taksa Akcizës']=pd.to_numeric(doganaData['Taksa Akcizës'],errors='coerce')
doganaData['Taksa TVSH-së']=pd.to_numeric(doganaData['Taksa TVSH-së'],errors='coerce')

doganaD1 = pd.DataFrame(doganaData, columns=['VITI', 'Sasia'])
print ("Shuma e sasisë (të hyrave) të realizuara sipas vitit:\n", doganaD1['Sasia'].sum())
print ("_________________________________________________________________________")

doganaD2 = pd.DataFrame(doganaData, columns=['VITI', 'MUAJI', 'Taksa Akcizës'])
print ("Shuma e taksës së akcizës sipas vitit dhe muajit:\n", doganaD2['Taksa Akcizës'].sum())
print ("_________________________________________________________________________")

doganaD3 = pd.DataFrame(doganaData, columns=['Vlera Mallrave'])
print ("Shuma e vlerave të mallërave të ndaluara nga Dogana:\n", doganaD3['Vlera Mallrave'].sum().max())
print ("_________________________________________________________________________")

doganaD4 = pd.DataFrame(doganaData, columns=['Netweight'])
print ("Vlera mesatare për peshat neto:\n", doganaD4['Netweight'].mean())
print ("_________________________________________________________________________")

doganaD5 = pd.DataFrame(doganaData, columns=['Kodi Tarifor'])
print ("Importet apo të hyrat e produkteve unike nga Dogana:\n", doganaD5['Kodi Tarifor'].unique())
print ("_________________________________________________________________________")

doganaD6 = pd.DataFrame(doganaData, columns=['Origjina', 'Sasia'])
print ("Top shtetet nga të cilat bëhet importi me sasi:\n")
print (doganaD6.dropna().sort_values(['Origjina', 'Sasia'], ascending=False).head(10))
print ("_________________________________________________________________________")

doganaD7 = doganaData.drop(['VITI', 'MUAJI', 'Regjimi', 'Kodi Tarifor'], axis=1)
print ("Fshirja e disa kolonave të caktuara:\n", doganaD7.columns)
print ("_________________________________________________________________________")

doganaD8 = doganaData.groupby('Origjina').sum()
doganaD8 = doganaData.sort_values('Taksa Doganës',ascending=False)
print ("Grupimi sipas shteteve, mbledhja dhe sortimi sipas taksës së doganës:\n", doganaD8.dropna().head(10))
print ("_________________________________________________________________________")