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


def bool_data(text: str):
    with_char = input(f"{text}\n").lower()
    while with_char != "s" and with_char != "n":
        with_char = input(f"{text}\n").lower()

    if with_char == "s":
        return True
    elif with_char == "n":
        return False


def main():
    try:
        length = int(
            input("Ingresa la longitud que tendra tu contraseña | rango (8 - 16)\n"))
        while length < 8 or length > 16:
            length = int(
                input("Ingresa la longitud que tendra tu contraseña | rango (8 - 16)\n"))
    except Exception as e:
        return "ERROR: " + e.__str__()

    with_capital_letters = bool_data("Con letras mayusuculas (s/n)")

    with_numbers = bool_data("Con numeros (s/n)")

    with_symbols = bool_data("Con simbolos (s/n)")

    password = password_generator(
        length, with_capital_letters, with_numbers, with_symbols)

    return password


if __name__ == "__main__":
    print(main())
