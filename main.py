ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    text = input("What text do you want to covert? ").upper()
    shift = int(input('how much would you like to shift the key by? '))
    encryption(text,shift)


def encryption(text,shift):
    for textIndex in range(0,len(text)):
        indexOfCurrentElementBeignConverted = ALPHABETS.index(text[textIndex])
        shiftedIndex = indexOfCurrentElementBeignConverted + shift
        if shiftedIndex > 25:
            shiftedIndex = shiftedIndex-26
        print(ALPHABETS[shiftedIndex])


main()