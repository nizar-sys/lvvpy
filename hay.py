print('hai selamat datang, aku adalah bot di program ini!')
print('pilih menu di bawah ini')

print('1. Bilang i love u ke kamu')
print('2. Gombalin kamu')
print('3. Keluar')

pilih = int(input('pilihan kamu : '))

if pilih == 1:
    kali = int(input('berapa kali ? '))
    print('i love uu\n' * kali)

    ulang = str(input('ulang ? (y/n) '))
    while (ulang == 'y'):
        kali = int(input('berapa kali ? '))
        print('i love uu\n' * kali)
        break
elif pilih == 2:
    print('kamu tau ga apa bedanya kamu sama aku ?')
    print('yaa. kalo aku dibuat sama program, kalo kamu itu buat akuu tee-hee:P')

    lagi = str(input('mau yang lain ? (y/n) '))
    while (lagi == 'y'):
        print('cape cape overthinking buat kamu')
        print('eh ternyata kamu nya juga suka sama aku')
        break
else:
    yakin = str(input('yakin ? (y/n) '))
    while(yakin == 'y'):
        print('byee, makasih udah main sama aku:)')
        break
