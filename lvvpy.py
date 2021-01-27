def ily():
    inputIly = int(input('berapa kali ? '))
    print('i love uu\n' * inputIly)

    ulang = str(input('lagi ? (y/n) '))
    while (ulang == 'y'):
        ily()
    if ulang == 'n':
        menu()


def gombal():
    print('kamu tau ga bedanya kamu sama aku ?')
    print('kalo aku dibuat sama program, kalo kamu dibuat untuk aku... tee-hee')
    kembali = str(input('kembali ke menu ? (y) '))
    if kembali == 'y':
        menu()


def menu():
    print('===Menu===')
    print('1. Bilang i love u')
    print('2. Gombal')
    print('3. Keluar')

    menu = str(input('Pilih menu : '))

    if menu == '1':
        ily()
    elif menu == '2':
        gombal()
    else:
        exit('byee, makasi ya udah ngunjungin akuuu')


if __name__ == "__main__":

    while(True):
        menu()
