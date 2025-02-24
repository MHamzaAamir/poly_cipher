# Poly Cipher

## Introduction
Poly Cipher is a custom encryption algorithm that utilizes polynomial equations to encode and decode text. This cipher employs a set of three depressed quadratic functions (quadratic equations without the linear bx term) to transform plaintext characters into encoded ciphertext, ensuring an inverse function exists for decryption.

## Features
- Encrypts and decrypts text using depressed quadratic equations.
- Generates random encryption keys or allows manual key input.
- Uses special characters as delimiters to add randomness to the ciphertext.
- Supports spaces in plaintext.

## How It Works
### Encryption (encoder.py)
1. The script allows the user to either generate a random key or input a manual key.
2. The key consists of three quadratic equations, each with only two coefficients (ax² + c, skipping the bx term).
3. Each character in the plaintext is mapped to an index based on a predefined `keymap`.
4. The corresponding quadratic function is applied to the index to generate an encrypted numeric value.
5. The numeric values are converted into characters using a specific encoding scheme and randomized delimiters.
6. The final output is displayed as the ciphertext along with the encryption key.

### Decryption (decoder.py)
1. The user inputs the encryption key used during encoding.
2. The ciphertext is processed to extract numeric values.
3. The inverse quadratic operations are applied to recover the original character indices.
4. The indices are mapped back to characters using the same `keymap`.
5. The reconstructed plaintext is displayed.

## Usage
### Running the Encryption Script
1. Run `encoder.py` using Python:
   ```sh
   python encoder.py
   ```
2. Choose an encryption mode:
   - `1` for automatic key generation.
   - `2` to manually enter a key.
3. Enter the plaintext message.
4. The script outputs the ciphertext and the encryption key.

### Running the Decryption Script
1. Run `decoder.py` using Python:
   ```sh
   python decoder.py
   ```
2. Enter the encryption key used during encoding.
3. Input the ciphertext to be decoded.
4. The script outputs the original plaintext.

## Example
### Encryption
```
Poly Cipher
Select One Option: 
1) Auto Key Generation
2) Manual Key Input
1
Enter Plain Text: hello world

Ciphertext: zq@u|ef^j)!
Key: [12.34, 56.78, 90.12, 34.56, 78.90, 12.34]
```

### Decryption
```
Enter Key: [12.34, 56.78, 90.12, 34.56, 78.90, 12.34]
Enter Ciphertext: zq@u|ef^j)!

Plaintext: hello world
```

## Requirements
- Python 3.x

## Notes
- The encryption relies on floating-point arithmetic, which may introduce minor variations due to precision.
- The decryption process assumes the key is accurately retained and entered correctly.

