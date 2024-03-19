
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
    for i in string:
        if i in leet_dict.keys():
            return string.join(leet_dict.values())
        else:
            return string.join(leet_dict.keys())
    return string


proba_1 = leet_Converter("leet")
print(proba_1)


# la idea es convertir letras
