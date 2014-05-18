testString = ""
searchChar = ""
newChar= ""

while testString == "" and len(searchChar) != 1 and newChar=="":
    testString = input("Please enter some text to search : ")
    searchChar = input("Enter a character to search for : ")
    newChar = input("What would you like to replace the character with? : ")

print(testString.replace(searchChar,newChar))
