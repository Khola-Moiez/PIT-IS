from PIL import Image

def encrypt_image(image_path, output_path, key):
    """
    Encrypts an image by performing XOR operation on each pixel value with a key.
    """
    try:
        image = Image.open(image_path)
        pixels = image.load()

        # Get image dimensions
        width, height = image.size

        # Encrypt each pixel
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]  
                # Perform XOR operation with the key
                r ^= key
                g ^= key
                b ^= key
                pixels[x, y] = (r, g, b)  # Update pixel values

        # Save the encrypted image
        image.save(output_path)
        print(f"Image encrypted and saved to {output_path}")
    except Exception as e:
        print(f"Error encrypting image: {e}")

def decrypt_image(image_path, output_path, key):
    """
    Decrypts an image by performing XOR operation on each pixel value with the same key.
    """
    try:
        # Open the encrypted image
        image = Image.open(image_path)
        pixels = image.load()

        # Get image dimensions
        width, height = image.size

        # Decrypt each pixel
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]  
                r ^= key
                g ^= key
                b ^= key
                pixels[x, y] = (r, g, b)  # Update pixel values

        # Save the decrypted image
        image.save(output_path)
        print(f"Image decrypted and saved to {output_path}")
    except Exception as e:
        print(f"Error decrypting image: {e}")

def main():
    print("Simple Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        image_path = input("Enter the path of the image to encrypt: ")
        output_path = input("Enter the output path for the encrypted image: ")
        key = int(input("Enter the encryption key (an integer between 0 and 255): "))
        encrypt_image(image_path, output_path, key)
    elif choice == '2':
        image_path = input("Enter the path of the image to decrypt: ")
        output_path = input("Enter the output path for the decrypted image: ")
        key = int(input("Enter the decryption key (same as encryption key): "))
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
