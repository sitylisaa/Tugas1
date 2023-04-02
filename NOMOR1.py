import numpy as np
import math
import matplotlib.pyplot as plt

def linear_menaik(a, b, x):
    if x < a:
        return 0
    elif x >= a and x <= b:
        return (x - a) / (b - a)
    else:
        return 1

def linear_menturun(a, b, x):
    if x < a:
        return 1
    elif x >= a and x <= b:
        return (b - x) / (b - a)
    else:
        return 0

def segitiga(a, b, x):
    if x <= a:
        return 0
    elif x > a and x <= (a+b)/2:
        return 2*((x-a)/(b-a))**2
    elif x > (a+b)/2 and x < b:
        return 1-2*((x-b)/(b-a))**2
    else:
        return 1

def trapesium(a, b, c, d, x):
    if x <= a:
        return 0
    elif x > a and x <= b:
        return (x-a)/(b-a)
    elif x > b and x <= c:
        return 1
    elif x > c and x <= d:
        return (d-x)/(d-c)
    else:
        return 0

def sigmoid_penyusutan(a, b, x):
    y = 1 / (1 + math.exp(-a * (x - b)))
    return y

def sigmoid_pertumbuhan(a, b, x):
    y = 1 / (1 + math.exp(-a * (b - x)))
    return y

def gauss(x, a, b):
    return np.exp(-(x-a)**2/(2*b**2))

def plot_gauss(a, b):
    x = np.linspace(-10, 10, 1000)
    y = gauss(x, a, b)
    plt.plot(x, y)
    plt.title(f'Gaussian with a={a} and b={b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def beta(x, a, b):
    return x**(a-1)*(1-x)**(b-1)

def plot_beta(a, b):
    x = np.linspace(0, 1, 1000)
    y = beta(x, a, b)
    plt.plot(x, y)
    plt.title(f'Beta with a={a} and b={b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def main():
    while True:
        print("Program Fungsi Keanggotaan")
        print("1. Fungsi Keanggotaan Linear")
        print("2. Fungsi Keanggotaan Segitiga")
        print("3. Fungsi Keanggotaan Trapesium")
        print("4. Fungsi Keanggotaan Sigmoid")
        print("5. Fungsi Keanggotaan Gauss")
        print("6. Fungsi Keanggotaan Beta")
        print("7. Keluar")

        pilihan = int(input("Masukkan pilihan Anda: "))

        if pilihan == 1 :
            print("Pilih jenis Linear")
            print("1. Linear Naik")
            print("2. Linear Turun")
            jenis = int(input("Masukkan pilihan Anda: "))

            if jenis == 1:
                a = float(input("Masukkan nilai a: "))
                b = float(input("Masukkan nilai b: "))
                x = float(input("Masukkan nilai x: "))
                y = linear_menaik(a, b, x)
                plt.plot([a, b], [0, 1], 'r--', lw=2)
                plt.ylim(-0.1, 1.1)
                plt.title('Fungsi Keanggotaan Linear Menaik')
                plt.xlabel('Nilai x')
                plt.ylabel('Nilai y')
                plt.plot([x], [y], marker='o', markersize=8, color="red")
                plt.show()


            elif jenis == 2:
                a = float(input("Masukkan nilai a: "))
                b = float(input("Masukkan nilai b: "))
                x = float(input("Masukkan nilai x: "))
                y = linear_menturun(a, b, x)
                plt.plot([a, b], [1, 0], 'r--', lw=2)
                plt.ylim(-0.1, 1.1)
                plt.title('Fungsi Keanggotaan Linear Menurun')
                plt.xlabel('Nilai x')
                plt.ylabel('Nilai y')
                plt.plot([x], [y], marker='o', markersize=8, color="red")
                plt.show()


        elif pilihan == 2:
            a = float(input("Masukkan nilai a: "))
            b = float(input("Masukkan nilai b: "))
            x = float(input("Masukkan nilai x: "))
            y = segitiga(a, b, x)
            plt.plot([a, (a+b)/2, b], [0, 1, 0], 'r--', lw=2)
            plt.ylim(-0.1, 1.1)
            plt.title('Fungsi Keanggotaan Segitiga')
            plt.xlabel('Nilai x')
            plt.ylabel('Nilai y')
            plt.plot([x], [y], marker='o', markersize=8, color="red")
            plt.show()


        elif pilihan == 3:
            a = float(input("Masukkan nilai a: "))
            b = float(input("Masukkan nilai b: "))
            c = float(input("Masukkan nilai c: "))
            d = float(input("Masukkan nilai d: "))
            x = float(input("Masukkan nilai x: "))
            y = trapesium(a, b, c, d, x)
            plt.plot([a, b, c, d], [0, 1, 1, 0], 'r--', lw=2)
            plt.ylim(-0.1, 1.1)
            plt.title('Fungsi Keanggotaan Trapesium')
            plt.xlabel('Nilai x')
            plt.ylabel('Nilai y')
            plt.plot([x], [y], marker='o', markersize=8, color="red")
            plt.show()


        elif pilihan == 4:
            print("Pilih jenis Sigmoid")
            print("1. Kurva S-Penyusutan")
            print("2. Kurva S-Pertumbuhan")
            jenis = int(input("Masukkan pilihan Anda: "))

            if jenis == 1:
                a = float(input("Masukkan nilai a: "))
                b = float(input("Masukkan nilai b: "))
                x = float(input("Masukkan nilai x: "))
                y = sigmoid_penyusutan(a, b, x)
                print(f"Nilai keanggotaan pada Sigmoid Kurva S-Penyusutan dengan a={a}, b={b}, dan x={x} adalah {y:.3f}")

                # menampilkan grafik fungsi keanggotaan Sigmoid Kurva S-Penyusutan
                plt.plot([-10, 10], [0, 1], 'r--', lw=2)
                xs = [i/10 for i in range(-100, 100)]
                ys = [sigmoid_penyusutan(a, b, x) for x in xs]
                plt.plot(xs, ys)
                plt.ylim(-0.1, 1.1)
                plt.title('Fungsi Keanggotaan Sigmoid Kurva S-Penyusutan')
                plt.xlabel('Nilai x')
                plt.ylabel('Nilai y')
                plt.plot([x], [y], marker='o', markersize=8, color="red")
                plt.show()

            elif jenis == 2:
                a = float(input("Masukkan nilai a: "))
                b = float(input("Masukkan nilai b: "))
                x = float(input("Masukkan nilai x: "))
                y = sigmoid_pertumbuhan(a, b, x)
                print(f"Nilai keanggotaan pada Sigmoid Kurva S-Pertumbuhan dengan a={a}, b={b}, dan x={x} adalah {y:.3f}")

                # menampilkan grafik grafik fungsi keanggotaan Sigmoid Kurva S-Pertumbuhan
                plt.plot([-10, 10], [0, 1], 'r--', lw=2)
                xs = [i/10 for i in range(-100, 100)]
                ys = [sigmoid_pertumbuhan(a, b, x) for x in xs]
                plt.plot(xs, ys)
                plt.ylim(-0.1, 1.1)
                plt.title('Fungsi Keanggotaan Sigmoid Kurva S-Pertumbuhan')
                plt.xlabel('Nilai x')
                plt.ylabel('Nilai y')
                plt.plot([x], [y], marker='o', markersize=8, color="red")
                plt.show()
        
        elif pilihan == 5:
            a = float(input('Masukkan nilai a: '))
            b = float(input('Masukkan nilai b: '))
            plot_gauss(a, b)

        elif pilihan == 6:
            a = float(input('Masukkan nilai a: '))
            b = float(input('Masukkan nilai b: '))
            plot_beta(a, b)

        elif pilihan == 7:
            print("Terima kasih sudah menggunakan program ini.")
            break

        else:
            print("Pilihan yang Anda masukkan tidak valid. Silahkan coba lagi.")

if __name__ == '__main__':
    main()
