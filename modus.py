#modus adalah nilai yang paling sering muncul dalam kumpulan nilai
import numpy as np
import pandas as pd

#loading dataset
corona_indonesia=pd.ExcelFile("D:\TeguhPermana_data\Statistika deskriptif\kawalcovid-data.xlsx")
corona_indonesia=corona_indonesia.parse("daily_cases")

#filtering data set
corona_indonesia=corona_indonesia[corona_indonesia["Kasus Harian"]=="7/25/2020"].fillna(0)
frekuensi_kasus=corona_indonesia.iloc[:,1:-1].values[0]
provinsi=corona_indonesia.columns[1:-1]

#menghitung modus
modus=np.argmax(frekuensi_kasus)
print("Kasus Pertambahan terbanyak adalah {}".format(provinsi[modus]))