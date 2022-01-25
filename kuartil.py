#Kuartil adalah suatu nilai data yang membagi empat sama banyak kumpulan data yang telah diurutkan
import pandas as pd
import numpy as np
#loading dataset
corona_indonesia=pd.ExcelFile("D:/TeguhPermana_data/Statistika deskriptif/kawalcovid-data.xlsx")
corona_indonesia=corona_indonesia.parse("total_positive_cases")

#filtering data
corona_indonesia=corona_indonesia[corona_indonesia["Total Kasus"]=="7/25/2020"]
total_kasus=corona_indonesia.iloc[:,1:-1].values[0]
provinsi=corona_indonesia.columns[1:-1]

#menghitung kuartil atas dan bawah
kuartil_atas=np.percentile(total_kasus,25)
kuartil_bawah=np.percentile(total_kasus,75)

provinsi_bawah=provinsi[np.where(total_kasus<=kuartil_bawah)]
provinsi_atas=provinsi[np.where(total_kasus>=kuartil_atas)]

print("\n\nKuartil bawah kasus korona di Indonesia adalah {:.2f} ribu dimana provinsi yang termasuk adalah {}".format(kuartil_bawah/1000,list(provinsi_bawah)))
print("\n\nKuartil atas kasus korona di indonesia adlah {:.2f} ribu dimana provinsi yang termasuk adalah {}".format(kuartil_atas/1000,list(provinsi_atas)))

#menghitung kuartil tengah dan median

median=np.median(total_kasus)
kuartil_tengah=np.percentile(total_kasus,50)

print("\n\n\nMedian tengah adalah {} dengan kuartil {:.2f}".format(median,kuartil_tengah))
#kuartil tengah==median
"""
1   merupakan syntax menghitung kuartil bawah dengan library Numpy, angka 25 merupakan kode bahwa itu kuartil bawah (25%)

#2   merupakan syntax menghitung kuartil atas dengan library Numpy, angka 75 merupakan kode bahwa itu kuartil atas (75%)

#3   merupakan kode untuk menyaring list provinsi yang memiliki total_case di bawah Q1 dan di atas Q3

#4   merupakan syntax menghitung kuartil tengah dengan library Numpy, angka 50 merupakan kode bahwa itu kuartil tengah (50%)
"""