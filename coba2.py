class kalkulator :
    def hasil():
        print('selamat datang di program kalkulator sederhana')
        menu_list = ('1. penjumlahan' ,'2. pengurangan', '3. perkalian'  ,'4. pembagian')
        for i in menu_list :
            print(i)

        pemilihan = int(input("masukkan pilihan(1/2/3/4):"))
        bilpertama = float(input("masukkan bilangan pertama :"))
        bilkedua = float(input("masukkan bilkedua :"))

        if pemilihan == 1:
            jumlah = bilpertama + bilkedua
            print(bilpertama,"+",bilkedua,"=",jumlah)
        elif pemilihan == 2:
            jumlah = bilpertama - bilkedua
            print(bilpertama,"-",bilkedua,"=",jumlah)
        elif pemilihan == 3:
            jumlah = bilpertama * bilkedua
            print(bilpertama,"x",bilkedua,"=",jumlah)
        elif pemilihan == 4:
            jumlah = bilpertama / bilkedua
            print(bilpertama,"/",bilkedua,"=",jumlah)

x = kalkulator
x.hasil()