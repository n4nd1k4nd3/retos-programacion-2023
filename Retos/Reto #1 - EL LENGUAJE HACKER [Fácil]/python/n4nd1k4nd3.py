
'''/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */'''



def leet_Converter(string):
    leet_dict = {
        'l': '1',
        'e': '3',
        't': '7',
        'a': '4'     
    }
    new_string = ""
    claves = leet_dict.keys()
    for i in string:
        if i in claves:
            new_string += leet_dict[f"{i}"] 
        else:
            new_string += f'{i}'
    return new_string


proba_1 = leet_Converter("lert")
print(proba_1)


# la idea es convertir letras
