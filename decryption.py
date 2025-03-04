import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")
if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Extract the hidden data from the blue channel
hidden_data = ""
rows, cols, _ = img.shape

for i in range(rows):
    for j in range(cols):
        char = chr(img[i, j, 0])
        if char == "~":
            break
        hidden_data += char
    if char == "~":
        break

if "|" in hidden_data:
    stored_password, secret_message = hidden_data.split("|", 1)
else:
    print("Error: Data format incorrect. No password found.")
    exit()

# Prompt for the decryption password
user_password = input("Enter the decryption password: ")
if user_password == stored_password:
    print("✅ Correct Password! Decrypted Message:", secret_message)
else:
    print("❌ Incorrect Password! Decryption failed.")
