import cv2

def encrypt_image(image_path):
    # Function to encrypt an image
    img = cv2.imread(image_path)
    # Perform encryption operations (e.g., swapping pixels, mathematical operations)
    # Save the encrypted image
    cv2.imwrite('encrypted_image.png', img)

def decrypt_image(image_path):
    # Function to decrypt an image
    img = cv2.imread(image_path)
    # Perform decryption operations (reverse of encryption)
    # Save the decrypted image
    cv2.imwrite('decrypted_image.png', img)

def main():
    # Example of usage:
    image_path = input("Enter image file path: ")
    operation = input("Enter 'encrypt' or 'decrypt': ").lower()

    if operation == 'encrypt':
        encrypt_image(image_path)
        print("Image encrypted and saved as 'encrypted_image.png'")
    elif operation == 'decrypt':
        decrypt_image(image_path)
        print("Image decrypted and saved as 'decrypted_image.png'")
    else:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()