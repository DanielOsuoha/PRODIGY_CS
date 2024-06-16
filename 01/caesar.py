import string

def caesar(text, shift, alphabet):
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    
    shifted_alphabets = tuple(map(shift_alphabet, alphabet))
    final_alphabet = ''.join(alphabet)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet, alphabet)
    return text.translate(table)


plain_text = input("Enter plain text: ")
print(caesar(plain_text))