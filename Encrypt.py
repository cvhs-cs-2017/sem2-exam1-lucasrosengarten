"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
def novowels(anystring):
    newstring = ""
    for ch in anystring:
        a = ord(ch)
        a = a + 5
        newstring = newstring + chr(a)
    return newstring
print (novowels ("Cmptr Scnc Mks th Wrld g rnd bt t dsn't mk th wrld rnd tslf!"))

def decrypt(anystring):
    newstring = ""
    for ch in anystring:
        a = ord(ch)
        a = a - 5
        newstring = newstring + chr(a)
    return newstring
print (decrypt(novowels("Cmptr Scnc Mks th Wrld g rnd bt t dsn't mk th wrld rnd tslf"))





"""Write an encryption code that you make up and run it for the variable NoVowels"""
