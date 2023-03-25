a = int(input("ilk sayıyı giriniz "))
b = int(input("ikinci sayıyı giriniz "))

def ebob(sayı1,sayı2):
    ortak = []
    carpim = sayı2*sayı1
    for i in range(1,sayı1+1):
        for j in range(1,sayı2+1):
            if sayı1 % i == 0 and sayı2 % j == 0 and i == j:
                ortak.append(i)
    print(carpim/ortak[-1])

ebob(a,b)