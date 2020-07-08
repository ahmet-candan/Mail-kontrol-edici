#ödev1
"""def frekans():
    liste = dict()
    x = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
    for i in x:
        if( i in liste):
            liste[i] +=1
        else:
            liste[i]=1
    for anahtar,deger in liste.items():
        print("{} harfinden {} adet vardır".format(anahtar,deger))

frekans()"""

#ödev2
"""def düzenle():
    with open("şiir.txt","r+",encoding="utf-8") as file:
        data = ""
        lines = file.readlines()
        for line in lines:
            data = data +" "+ line.strip()
        print(data)
düzenle()"""

#ödev3
"""isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim =["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
for i,j in list(zip(isim,soyisim)):
    print(i,j)"""

#ödev4
def kontrol():
    with open("mailler.txt","r",encoding="utf-8") as file:
        oku = file.readlines()
        print(oku)
        a =list()
        for i in oku:
            #print(i)
            if i.endswith(".com\n"):
                a.append(i)
        for i in a:
            if "@" in i:
                print(i)                       
kontrol()


            
           

    


