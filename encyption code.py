import cv2
import os

# Load the cover image
img = cv2.imread("stegoimg.png")  # Ensure "stegoimg.png" exists in the same directory
if img is None:
    print("Error: Image not found!")
    exit()

# Get user input for password and secret message
password = input("Enter a password: ")
msg = input("Enter secret message: ")

# Combine the password and message with a separator and an end delimiter
hidden_data = password + "|" + msg + "~"

# Encode the hidden data into the blue channel of the image
msg_index = 0
rows, cols, _ = img.shape

for i in range(rows):
    for j in range(cols):
        if msg_index < len(hidden_data):
            img[i, j, 0] = ord(hidden_data[msg_index])
            msg_index += 1
        else:
            break
    if msg_index >= len(hidden_data):
        break

# Save and open the encrypted image
cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Windows-specific
print("Encryption Complete! The password and message are hidden inside 'encryptedImage.png'.")
