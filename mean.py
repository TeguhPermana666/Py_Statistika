import numpy as py
import pandas as pd
import matplotlib.pylab as plt
#loading dataset
corona_indonesia=pd.ExcelFile("D:/TeguhPermana_data/Statistika deskriptif/kawalcovid-data.xlsx")
corona_indonesia=corona_indonesia.parse("total_positive_cases")

#filter dataset
corona_indonesia =corona_indonesia[corona_indonesia["Total Kasus"]=="3/18/2020"]
total_kasus=corona_indonesia.iloc[:,1:-1].values[0]

#menghitung rata rata
mean=sum(total_kasus)/len(total_kasus)
print("Rata rata total kasus pada 18-Mar adalah {:.2f} ribu".format(mean/1000))


