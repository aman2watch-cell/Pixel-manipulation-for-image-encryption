# 🖼️ Pixel Manipulation for Image Encryption

A lightweight Python tool for **encrypting** and **decrypting** images using simple **XOR pixel manipulation**. Designed to demonstrate how basic bitwise operations can obscure image data.

## 🔐 How It Works

Each pixel’s Red, Green, and Blue values are individually XORed with a secret numeric key (between 1–255). The same operation reverses the process during decryption, thanks to the symmetric nature of XOR.

## 🚀 Features

- Supports both encryption and decryption modes
- No external libraries needed except `Pillow`
- Preserves image dimensions and format

## 📦 Requirements

- Python 3.x
- `Pillow` library (install with `pip install Pillow`)

## 💻 Usage

Run the script in your terminal:

```bash
python TASK 2.py
```

You’ll be prompted for:
- Mode: **E** for Encrypt or **D** for Decrypt
- Input image path
- Output image path
- A numeric key between **1 and 255**

### 🔧 Example

```bash
=== Image Encryption Tool ===
Choose mode: (E)ncrypt or (D)ecrypt: E
Enter the path of the image file: input.jpg
Enter the path to save the output image: encrypted.jpg
Enter a numeric key (1-255): 77
Encrypted image saved to: encrypted.jpg
```

## 🐞 Notes

Make sure to fix this line for proper execution:

```python
if __name__ == "_main_":
```

Change it to:

```python
if __name__ == "__main__":
```

## 📁 File Structure

- `TASK 2.py` – Python script containing encryption and decryption logic

## 🛡️ Disclaimer

This tool is for educational and illustrative purposes. It's not secure for real-world image protection applications.

## 📄 License

Free to use, modify, and share. Attribution appreciated but not required.
