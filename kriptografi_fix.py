import string
import numpy as np
from textwrap import wrap

base_matrix=[[1,2,3],[0,1,4],[5,6,0]] #matrix yang jadi basis
inv_matrix=np.linalg.inv(base_matrix) #invers matrix
teks="saya ingin lulus mata kuliah aljabar linier dengan nilai terbaik" #silakan diubah sesuai selera
teks_nospace=teks.replace(" ","") #menghapus spasi di teks
teks_pecah=wrap(teks_nospace, 3)
huruf=list(string.ascii_lowercase) #index huruf 0-25

#perulangan enkripsi
def enc():
    for i in range(len(teks_pecah)):
        b=[]
        for j in range(len(list(teks_pecah[i]))):
            if len(list(teks_pecah[i]))<3:
                for k in range(0,3):
                    a=huruf.index((list(teks_pecah[i])[j]))
                    b.append(a)
            else:
                a=huruf.index((list(teks_pecah[i])[j]))
                b.append(a)
        chip=np.dot(base_matrix,b)
        chip2=chip%26
        for y in chip2:
            enc=huruf[y]
            print(str(enc),end="")
    
#dekripsi .... belum bisa buat decrypt


"""for i in range(len(pecahenc)):
    b=[]
    for j in range(len(list(pecahenc[i]))):
        if len(list(pecahenc[i]))<3:
            for k in range(0,3):
                a=huruf.index((list(pecahenc[i])[j]))
                b.append(a)
        else:
            a=huruf.index((list(pecahenc[i])[j]))
            b.append(a)
    chip=np.dot(inv_matrix,b)
    chip2=chip%26
    for y in chip2:
        print(huruf[y],end="")"""

print("Asal Kalimat: ")
print(teks)

print("Enkripsinya: ")
enc()


#untuk buat input sen