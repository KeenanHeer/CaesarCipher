ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

def main():
    HowToPlay = ""
    while HowToPlay != 'Z':
        HowToPlay = input("press x to do encryption \nPress y to do decryption \nPress z to close the programme").upper()
        if HowToPlay == 'X':
            text = input("What text do you want to covert? ").upper()
            shift = int(input('how much would you like to shift the key by? '))
            print(encryption(text,shift))
            
        if HowToPlay == 'Y':
            DecryptText = input('what text would you like to decrypt?').upper()
            Decryptshift = int(input('how much would you like to shift the key by? '))
            print(decryption(DecryptText,Decryptshift))
    
 
            


def encryption(text,shift):
    encrypted = []
    for textIndex in range(0,len(text)):
        indexOfCurrentElementBeignConverted = ALPHABETS.index(text[textIndex])
        shiftedIndex = indexOfCurrentElementBeignConverted + shift
        if shiftedIndex > 26:
            shiftedIndex = shiftedIndex-27
        encrypted.append(ALPHABETS[shiftedIndex])
    return "".join(encrypted)


def decryption(text,shift):
    encrypted = []
    for textIndex in range(0,len(text)):
        indexOfCurrentElementBeignConverted = ALPHABETS.index(text[textIndex])
        shiftedIndex = indexOfCurrentElementBeignConverted - shift
        if shiftedIndex > 26:
            shiftedIndex = shiftedIndex-27
        encrypted.append(ALPHABETS[shiftedIndex])
    return "".join(encrypted)

main()

