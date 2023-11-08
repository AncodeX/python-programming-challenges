"""
    Reto #0: EL FAMOSO "FIZZ BUZZ”
    -------------------------------
    * Escribe un programa que muestre por consola (con un print) los
    * números de 1 a 100 (ambos incluidos y con un salto de línea entre
    * cada impresión), sustituyendo los siguientes:
    * - Múltiplos de 3 por la palabra "fizz".
    * - Múltiplos de 5 por la palabra "buzz".
    * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
    -------------------------------
"""


def fizzbuzz(number):
    mult_5 = number % 5 == 0
    mult_3 = number % 3 == 0
    if mult_5 and mult_3:
        print("fizzbuzz")
    elif mult_3:
        print("fizz")
    elif mult_5:
        print("buzz")
    else:
        print(number)


def main():
    for n in range(1, 101):
        fizzbuzz(n)


if __name__ == "__main__":
    main()
