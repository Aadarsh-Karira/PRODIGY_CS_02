from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size

    pixels = image.load()

    for i in range(height):
        for j in range(width):
            r, g, b = pixels[j, i]
            r ^= key
            g ^= key
            b ^= key
            pixels[j, i] = (r, g, b)

    image.save("encrypted_image.png")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size

    pixels = image.load()

    for j in range(height):
        for k in range(width):
            r, g, b = pixels[k, j]
            r ^= key
            g ^= key
            b ^= key
            pixels[k, j] = (r, g, b)

    image.save("decrypted_image.png")

def main():
    choice = int(input("Enter 1 to Encrypt Image\n2 to Decrypt: "))
    image_path = input("Enter The Image Path: ")
    key = int(input("Enter the key: "))
    if choice == 1:
        encrypt_image(image_path, key)
    elif choice == 2:
        decrypt_image(image_path, key)

if __name__ == '__main__':
    main()
