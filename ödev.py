#Ödev1
"""def hesapla(listem):
    return listem[0]*listem[1]

liste =  [(3,4),(10,3),(5,6),(1,9)]
print(list(map(hesapla,liste)))"""


#ödev2
"""def hesapla(listem):
    if (listem[0]+listem[1]>listem[2] and listem[0]+listem[2]>listem[1] and listem[1]+listem[2]>listem[0]):
        return True
    else:
        return False
liste =  [(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(hesapla,liste)))"""


#ödev3
"""from functools import reduce
def tek_cift(x):

    if (x % 2 == 0):
        return True
    else:
        return False

def hesapla(x,y):
    return x+y

liste = [1,2,3,4,5,6,7,8,9,10]

liste2 = list(filter(tek_cift,liste))

print(reduce(hesapla,liste2))"""


#ödev4
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in list(zip(isimler,soyisimler)):
    print(i,j)

    











