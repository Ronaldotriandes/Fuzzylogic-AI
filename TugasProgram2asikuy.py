from random import uniform
import pandas as pd
import csv
#Ronaldo Triandes 1301154108
#FUzzy Logic


#df = pd.read_excel("DataTugas2.xlsx")
#Pendapat = df['Pendapat'].values.tolist()
#Hutang = df['Hutang'].values.tolist()
Pendapat=[]
Hutang=[]
Has=[]
Hasilnya=[]
#Pendapat = [1.632,0.825,1.273,1.534,1.596,0.664,1.68,0.925,0.806,1.178,1.548,1.617,0.89,1.354,0.428,1.319,0.859,1.345,0.599,1.763,0.155,0.828,0.112,0.819,1.723,1.41,1.255,1.369,1.684,1.794,0.63,1.352,0.923,0.515,1.325,0.946,1.755,0.747,1.332,1.263,1.159,0.507,1.353,0.902,1.736,1.714,0.78,1.433,0.516,1.818,0.689,1.551,0.473,0.756,1.623,1.251,1.336,0.748,0.493,0.765,0.88,1.159,1.423,0.588,1.282,0.666,1.385,1.306,1.218,1.025,1.046,1.641,0.158,0.6,0.894,0.791,1.217,1.9,1.227,0.664,1.164,1.804,0.219,1.643,1.03,1.531,1.593,1.209,0.754,1.586,0.793,0.817,0.557,1.474,1.329,0.91,0.95,1.406,0.816,1.183]
#Hutang = [39.375,39.236,80.701,73.641,37.319,63.226,37.761,0,69.192,26.359,53.764,55.544,41.718,61.333,38.739,41.201,26.266,76.343,45.566,55.289,29.496,56.747,26.202,60.764,33.533,25.133,27.166,50.779,45.068,24.11,20.042,55.861,37.382,41.771,70.009,98,42.045,25.471,68.795,45.986,68.12,16.331,61.466,68.021,27.34,36.429,78.054,78.028,43.66,49.628,2.032,51.746,28.74,11.764,41.85,48.798,62.094,23.649,27.813,36.031,79.878,87.871,27.672,35.48,29.854,60.245,61.661,52.933,17.396,29.924,13.541,46.775,1.472,80.864,22.836,39.781,82.991,32.769,20.851,39.692,18.112,27.693,11.55,57.308,25.246,21.48,41.325,67.625,37.883,38.999,11.302,62.427,29.517,56.534,71.308,43.769,23.79,46.838,18.123,28.061]
data = pd.read_csv("DataTugas2.csv", delimiter = "," ,header = 0)
data.iat[1,2]
for i in range(100):
    Pendapat.append(data.iat[i,1])
    Hutang.append(data.iat[i,2])

#Implementasi untuk pendapatan
def FuzzyPendapat(Pendapat, Pendapatkec, Pendapatsed, Pendapatting):
    if (Pendapat <= 0.5):
        Pendapatkec = 1
    elif (Pendapat >= 0.5 and Pendapat <=1):
        Pendapatkec= (1 - Pendapat) #/ float(0.4)
        Pendapatsed = (Pendapat - 0.5) #/float(0.4)
    elif (Pendapat >= 1 and Pendapat <= 1.4):
        Pendapatsed = 1
    elif (Pendapat >= 1.4 and Pendapat <= 1.9):
        Pendapatsed = (1.9 - Pendapat) #/float(0.4)
        Pendapatting = (Pendapat - 1.4)# /float(0.4
    elif (Pendapat >= 1.9):
        Pendapatting = 1
    return Pendapatkec, Pendapatsed, Pendapatting

#implementasi untuk hutang
def FuzzyHutang(Hutang, Hutangsed, Hutangkec, Hutangting):
    if (Hutang <= 10):
        Hutangkec = 1
    elif (Hutang >= 10 and Hutang <= 35):
        Hutangkec = (35 - Hutang) #/float(20)
        Hutangsed = (Hutang - 10 )# /float(20)
    elif (Hutang >= 35 and Hutang <= 50):
        Hutangsed = 1
    elif (Hutang >= 50 and Hutang <= 70):
        Hutangsed = (70 - Hutang)# / float(20)
        Hutangting = (Hutang - 50) #/float(20)
    elif (Hutang >= 70):
        Hutangting = 1
    return Hutangkec, Hutangsed, Hutangting


def inferensi(Pendapatkec, Pendapatsed, Pendapatting, Hutangkec, Hutangsed, Hutangting):
    Ya = 0
    Tidak = 0
    Ya1 = 0
    Ya2 = 0
    Ya3 = 0
    #Ya4 = 0
    #Ya5 = 0
    Tidak1 = 0
    Tidak2 = 0
    Tidak3 = 0
    Tidak4 = 0
    Tidak5 = 0
    Tidak6 = 0
#implementasi untuk rule yang digunakan
    if (Pendapatkec !=0 and Hutangkec !=0):
        Tidak1 = min(Pendapatkec, Hutangkec)
    if (Pendapatkec !=0 and Hutangsed !=0):
        Ya1 = min(Pendapatkec, Hutangsed)
    if (Pendapatkec !=0 and Hutangting !=0):
        Ya2 = min(Pendapatkec, Hutangting)

    if (Pendapatsed !=0 and Hutangkec !=0):
        Tidak2 = min(Pendapatsed, Hutangkec)
    if (Pendapatsed !=0 and Hutangsed !=0):
        Tidak3 = min(Pendapatsed, Hutangsed)
    if (Pendapatsed!=0 and Hutangting!=0):
        Ya3 = min(Pendapatsed, Hutangting)

    if (Pendapatting !=0 and Hutangkec !=0):
        Tidak4 = min(Pendapatting, Hutangkec)
    if (Pendapatting !=0 and Hutangsed!=0):
        Tidak5 = min(Pendapatting, Hutangsed)
    if (Pendapatting !=0 and Hutangting !=0):
        tidak6 = min(Pendapatting, Hutangting)

    Ya = max(Ya1, Ya2, Ya3)
    Tidak = max(Tidak1, Tidak2, Tidak3, Tidak4, Tidak5, Tidak6)
    if (Ya > Tidak):
        Ket = "Ya"
    else:
        Ket = "Tidak"
    return Ya, Tidak, Ket

def Defuzzy(Ya, Tidak):
    BLT = (Tidak * 20 + Ya * 80) / (Tidak + Ya)
    return BLT

count = 0
dapat = 0
jml = 0
while count <100:
   
    Pendapatkec = 0
    Pendapatsed = 0
    Pendapatting = 0
    Hutangkec = 0
    Hutangsed = 0
    Hutangting = 0
    Ya = -1
    Tidak = -1
    BLT = 0
    Pendapatkec, Pendapatsed, Pendapatting = FuzzyPendapat(Pendapat[count], Pendapatkec, Pendapatsed, Pendapatting)
    Hutangkec, Hutangsed, Hutangting = FuzzyHutang(Hutang[count], Hutangkec, Hutangsed, Hutangting)
    Ya, Tidak, Ket = inferensi(Pendapatkec, Pendapatsed, Pendapatting, Hutangkec, Hutangsed, Hutangting)
    BLT = Defuzzy(Ya, Tidak)
    if (Ket=="Ya"):
        dapat += 1
        Has.append(count+1)
        # codingan untuk menampilkan yang dapat blt aja
        #print ( count + 1, \
        #",Pendapatan: ", Pendapat[count], \
        #",Hutang: ", Hutang[count], \
        #",DapatBLT : ", Ket, " (",BLT,")")
        #print (" ")
        #print(jml) 
        count += 1
    else:
        count +=1
print("Nomor Baris Yang layak dapat Blt adalah ",Has)
Hasilnya.append(Has)
#codingan untuk menampilkan semuanya
    #print ( count + 1, \
      #  ",Pendapatan: ", Pendapat[count], \
     #   ",Hutang: ", Hutang[count], \
     #   ",DapatBLT : ", Ket, " (",BLT,")")
   # print (" ") 
    #count += 1
with open('TebakanTugas2.csv', 'a', newline='') as filecsv:
    datafile = csv.writer(filecsv)
    datafile.writerows(Hasilnya)
#Hasilnya = pd.DataFrame((Hasilnya), columns = list("nomor baris yang layak menerima blt"))
#Hass.to_csv("TebakanTugas2.csv",sep="\t",index=false)  

print("Total yang mendapatkan BLT adalah ",dapat,"Orang") #untuk menghitung yang dapat blt