def alphabet_position(letter):
    lowa = letter.lower()
    compare = "abcdefghijklmnopqrstuvwxyz"
    #return the index of the provided letter in the alphabet_position
    result = compare.index(lowa)
    return result

def rotate_character(char, rot):
    if ord(char) >= 65 and ord(char) <= 90 or ord(char) >= 97 and ord(char) <= 122:
        compare = "abcdefghijklmnopqrstuvwxyz"
        place = alphabet_position(char)
        nuplace = (place + rot) % 26
        nuletta = compare[nuplace]
        if ord(char) < 97:
            return nuletta.upper()
        return nuletta
    else:
        return char

def encrypt(text, rot):
    crypted = ""
    for eachcar in text:
        dodis = rotate_character(eachcar, rot)
        crypted = crypted + dodis
    return crypted    
