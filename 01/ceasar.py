import string

shift = 4

alphabet = string.ascii_lowercase
print(alphabet)
shifted = alphabet[shift:]+alphabet[:shift]

table = str.maketrans(alphabet, shifted)


plain_text = input("Enter the text to be encrypted: ")
encrypted = plain_text.translate(table)
print(encrypted)