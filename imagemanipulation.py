from PIL import Image
import numpy as np

class ImageEncryptor:
    def __init__(self, key=50):
        # Set a key for encryption; key should be consistent between encrypt and decrypt
        self.key = key

    def encrypt(self, image_path, output_path):
        # Open the image
        img = Image.open(image_path)
        img_array = np.array(img, dtype=np.uint8)  # Ensure image array is uint8

        # Apply encryption by modifying pixel values
        encrypted_array = (img_array.astype(int) + self.key) % 256  # Add key and wrap within 0-255 range
        encrypted_array = encrypted_array.astype(np.uint8)  # Convert back to uint8 for saving

        # Save encrypted image
        encrypted_img = Image.fromarray(encrypted_array)
        encrypted_img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")

    def decrypt(self, encrypted_image_path, output_path):
        # Open the encrypted image
        img = Image.open(encrypted_image_path)
        img_array = np.array(img, dtype=np.uint8)

        # Reverse encryption by subtracting key
        decrypted_array = (img_array.astype(int) - self.key) % 256  # Subtract key and wrap within 0-255 range
        decrypted_array = decrypted_array.astype(np.uint8)  # Convert back to uint8 for saving

        # Save decrypted image
        decrypted_img = Image.fromarray(decrypted_array)
        decrypted_img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")

# Usage Example
if __name__ == "__main__":
    key = 50  # Set an encryption key (must be the same for encryption and decryption)
    encryptor = ImageEncryptor(key)

    # Encrypt the image
    encryptor.encrypt("image1.jpg", "encrypted_image.jpg")

    # Decrypt the image
    encryptor.decrypt("encrypted_image.jpg", "decrypted_image.jpg")
