import time


def ily():
    kata = "i love uu bbyy\n"
    inputIly = int(input('berapa kali ? '))

    for inputIly in range(inputIly, 0, -1):
        time.sleep(0.1)
        print(kata)

    ulang = str(input('lagi ? (y/n) '))
    while (ulang == 'y'):
        ily()
    if ulang == 'n':
        time.sleep(0.5)
        menu()


def gombal():

    print("aku mau ngomong sesuatu, tapi malu... jadi disini aja ya hehe")
    time.sleep(0.5)
    nama = str(input("masukin nama kamu yaa : "))
    print("sekarang jawab jujur ya!")
    pacar = str(
        input("sebenernya aku suka sama kamu, kamu mau jadi pacar aku ga ? (y/n) "))
    if pacar == 'y':
        print(nama + " kamu sekarang jadi pacar aku yaaa\n")
        time.sleep(0.5)
        print("oh ya, aku ada pantun buat kamu")
        time.sleep(0.5)
        print("ikan hiu makan tomat")
        time.sleep(0.5)
        print("ai lop yuuu hehehhe")
    else:
        print("kenapa ?:(")
        time.sleep(0.5)
        print("\nyaudah deh, btw aku ada pantun buat kamu")
        time.sleep(0.5)
        print("ikan hiu makan tomat")
        time.sleep(0.5)
        print("ai lop yuuu hehehhe")
    kembali = str(input('kembali ke menu (y/n) '))
    if kembali == 'y':
        menu()
    else:
        print("udah sana, aku malu>_<")
        time.sleep(0.5)
        menu()


def about():
    print("==========================About Me======================================")
    print("| Name : Muhamad Nizar                                                 | ")
    print("| Github : github.com/nizar-sys | Instagram : instagram.com/@niizar.id | ")
    print("========================================================================")
    kembali = str(input('kembali ke menu (y/n) '))
    if kembali == 'y':
        menu()
    else:
        time.sleep(0.5)
        about()


def menu():
    print('==============Menu================')
    print('| 1. Bilang i love u  3. About   |')
    print('| 2. Gombal           4. Keluar  |')
    print('==================================')

    menu = str(input('Pilih menu : '))

    if menu == '1':
        time.sleep(0.5)
        ily()
    elif menu == '2':
        time.sleep(0.5)
        gombal()
    elif menu == '3':
        time.sleep(0.5)
        about()
    elif menu == '4':
        exit("byee, makasih ya udah ngunjungin akuu")
    else:
        print("menu yang dipilih tidak ada di list!")


if __name__ == "__main__":

    while(True):
        menu()
