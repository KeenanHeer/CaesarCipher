ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

def main():
    HowToPlay = ""
    while HowToPlay != 'Z':
        HowToPlay = input("press x to do encryption: \nPress y to do decryption: \nPress z to close the programme:\nPress H to find all pssibilties of the decrypted text: ").upper()
        if HowToPlay == 'X':
            text = input("\nWhat text do you want to covert?\n").upper()
            shift = int(input('\nhow much would you like to shift the key by? \n'))
            print(encryption(text,shift))
        elif HowToPlay == 'Y':
            DecryptText = input('\nwhat text would you like to decrypt?\n').upper()
            Decryptshift = int(input('\nhow much would you like to shift the key by?\n '))
            print(decryption(DecryptText,Decryptshift))
        elif HowToPlay == 'H':
            DecryptText = input('\nwhat text would you like to decrypt?\n').upper()
            allPossibilities(DecryptText)

    

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


def allPossibilities(text):
    shiftValue = 0
    while shiftValue < 26:
        if(checkIfEnglishWord(decryption(text,shiftValue))):
            print(f"{shiftValue}:{decryption(text,shiftValue)}")
            return
        shiftValue = shiftValue + 1 
    while shiftValue < 26:
        print(f"{shiftValue}:{decryption(text,shiftValue)}")
        shiftValue = shiftValue + 1

def checkIfEnglishWord(textToCheck):
    with open("./words.txt","r") as myNewFile:
        for lineIndex,line in enumerate(myNewFile):
            for word in textToCheck.split(' '):
                if len(word)>0 and line.replace('\n','').upper() == word:
                    return True
    return False
        
main()
