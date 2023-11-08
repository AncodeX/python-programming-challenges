"""
    Reto #3: EL GENERADOR DE CONTRASEÑAS
    -------------------------------------
    * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
    * Podrás configurar generar contraseñas con los siguientes parámetros:
    * - Longitud: Entre 8 y 16.
    * - Con o sin letras mayúsculas.
    * - Con o sin números.
    * - Con o sin símbolos.
    * (Pudiendo combinar todos estos parámetros entre ellos)
    -------------------------------------
"""
from string import digits, ascii_uppercase, punctuation
from random import choices


def password_generator(length: int, with_capital: bool, with_numbers: bool, with_symbols: bool) -> str:
    characters = ""
    if with_capital:
        characters += ascii_uppercase
    if with_numbers:
        characters += digits
    if with_symbols:
        characters += punctuation

    password = ""
    try:
        for _ in range(length):
            password += "".join(choices(characters))
    except Exception as e:
        return "ERROR: " + e.__str__() + "\nTu contraseña debe tener al menos un caracter"
    return password


def main():
    try:
        length = int(
            input("Ingresa la longitud que tendra tu contraseña | rango (8 - 16)\n"))
        while length < 8 or length > 16:
            length = int(
                input("Ingresa la longitud que tendra tu contraseña | rango (8 - 16)\n"))
    except Exception as e:
        return "ERROR: " + e.__str__()

    with_capital_letters = input("Con letras mayusuculas (s/n): ").lower()
    while with_capital_letters != "s" and with_capital_letters != "n":
        with_capital_letters = input("Con letras mayusuculas (s/n): ").lower()

    if with_capital_letters == "s":
        with_capital_letters = True
    elif with_capital_letters == "n":
        with_capital_letters = False

    with_numbers = input("Con numeros (s/n): ").lower()
    while with_numbers != "s" and with_numbers != "n":
        with_numbers = input("Con numeros (s/n): ").lower()

    if with_numbers == "s":
        with_numbers = True
    elif with_numbers == "n":
        with_numbers = False

    with_symbols = input("Con simbolos (s/n): ").lower()
    while with_symbols != "s" and with_symbols != "n":
        with_symbols = input("Con simbolos (s/n): ").lower()

    if with_symbols == "s":
        with_symbols = True
    elif with_symbols == "n":
        with_symbols = False

    password = password_generator(
        length, with_capital_letters, with_numbers, with_symbols)

    return password


if __name__ == "__main__":
    print(main())
