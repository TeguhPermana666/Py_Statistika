#Median adalah nilai tengah dari sebuah kumpulan data yang sudah diurutkan.map
#  
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

#loading set
corona_indonesia=pd.ExcelFile("D:/TeguhPermana_data/Statistika deskriptif/kawalcovid-data.xlsx")
corona_indonesia=corona_indonesia.parse("total_positive_cases")
#filter data set
corona_indonesia=corona_indonesia[corona_indonesia["Total Kasus"]=="10/29/2020"]
total_kasus=corona_indonesia.iloc[:,1:-1].values[0]
#menghitung median
median=np.median(total_kasus)
print("Nilai Tengah kasus 10/29/2020 adalah {:.2f}".format(median))
