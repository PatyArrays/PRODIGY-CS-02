from PIL import Image
import random


def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    random.seed(key)
    random.shuffle(pixels)

    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(pixels)
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")


def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    encrypted_pixels = list(image.getdata())

    random.seed(key)

    # Create a list of indices and shuffle them using the same seed
    indices = list(range(len(encrypted_pixels)))
    random.shuffle(indices)

    # Create a list to hold the decrypted pixels
    decrypted_pixels = [None] * len(encrypted_pixels)

    # Place each pixel back to its original position based on shuffled indices
    for i, index in enumerate(indices):
        decrypted_pixels[index] = encrypted_pixels[i]

    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")


def main():
    choice = input("Would you like to (e)ncrypt or (d)ecrypt an image? (e/d): ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")
        return

    image_path = input("Enter the path to your image file: ")
    output_path = input("Enter the path to save the output image: ")
    key = int(input("Enter the encryption/decryption key (integer): "))

    if choice == 'e':
        encrypt_image(image_path, output_path, key)
    else:
        decrypt_image(image_path, output_path, key)


if __name__ == "__main__":
    main()
