def encrypt_image(image_path, key):
    file = open(image_path, 'rb')
    image = file.read()
    file.close()
    image = bytearray(image)
    #performing XOR on the image
    for index, value in enumerate(image):
        image[index] = value ^ key
    #opening file for writing purposes
    file = open(image_path, 'wb')
    #write the image
    file.write(image)
    file.close()
    print("Encryption done...")
    

def decrypt_image(image_path, key):
    file = open(image_path, 'rb')
    image = file.read()
    file.close()
    image = bytearray(image)
    
    #performing XOR on the image
    for index, value in enumerate(image):
        image[index] = value ^ key
    #opening file for writing purposes
    file = open(image_path, 'wb')
    #write the image
    file.write(image)
    file.close()
    print("Decryption done...")

def main():
    # Example of usage:
    image_path = input("Enter image file path: ")
    operation = input("Enter 'encrypt' or 'decrypt': ").lower()
    key = int(input("Enter key (a number you need to remember): ").lower())
    
    if operation == 'encrypt':
        encrypt_image(image_path, key)
        print("Image encrypted and saved as 'encrypted_image.png'")
    elif operation == 'decrypt':
        decrypt_image(image_path, key)
        print("Image decrypted and saved as 'decrypted_image.png'")
    else:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()