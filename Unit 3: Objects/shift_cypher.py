word = input("Enter a three-capital letter word: ")
shift = int(input("Shift by how many letters: "))
l_1 = chr(ord(word[0])+shift)
l_2 = chr(ord(word[1])+shift)
l_3 = chr(ord(word[2])+shift)
word = str(l_1+l_2+l_3)
print("The secret message is:",word)

