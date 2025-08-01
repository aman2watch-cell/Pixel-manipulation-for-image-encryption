from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                # XOR each pixel value with the key
                pixels[i, j] = (r ^ key, g ^ key, b ^ key)

        img.save(output_path)
        print(f"Encrypted image saved to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(input_path, output_path, key):
    # Decryption is same as encryption (XOR is reversible)
    encrypt_image(input_path, output_path, key)

def main():
    print("=== Image Encryption Tool ===")
    mode = input("Choose mode: (E)ncrypt or (D)ecrypt: ").strip().upper()

    if mode not in ['E', 'D']:
        print("Invalid choice.")
        return

    input_path = input("Enter the path of the image file: ").strip()
    output_path = input("Enter the path to save the output image: ").strip()
    try:
        key = int(input("Enter a numeric key (1-255): "))
        if not (1 <= key <= 255):
            print("Key must be between 1 and 255.")
            return
    except ValueError:
        print("Invalid key. Must be a number.")
        return

    if not os.path.exists(input_path):
        print("Input file not found.")
        return

    if mode == 'E':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

if __name__ == "_main_":
    main()