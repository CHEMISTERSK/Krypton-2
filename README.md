# Krypton 2 - Advanced Rule-Driven Substitution Cipher

Krypton 2 is an advanced rule-driven encryption system with dynamic state management and graphical user interface. It uses a combination of substitution ciphers and state-based rules for high-level security.

## Features

- **Graphical User Interface**: Modern GUI for easy encryption/decryption
- **Key Generation**: Automatic generation of 53-character keys with logging
- **Dynamic States**: System uses 4 different encryption maps (an1, an2, an3, an4)
- **Rules**: 256 rules determining state transitions
- **Encryption**: Text conversion to hexadecimal format with 32-character rows
- **Decryption**: Recovery of original text from encrypted content
- **Command Line Interface**: Core system for advanced users
- **Key Recovery**: Recovery mode for incorrectly decrypted documents
- **Multiple Input Modes**: Support for both text input and file processing

## Key Structure

Key format: `XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX`

- 6 segments separated by hyphens
- Each segment has 8 characters
- Total length: 53 characters (48 characters + 5 hyphens)

## Usage

### Graphical User Interface
Run the main application:
```python
python "Kr 2.pyw"
```

**Text Encryption/Decryption:**
1. Enter text in the INPUT field
2. Click "Encript" to encrypt (key will be automatically generated)
3. Copy the generated key from the key field
4. Enter encrypted text and the key to decrypt

**File Encryption/Decryption:**
1. Enter the file path in "Path to the File" field
2. Click "Encript" to encrypt the file (key will be generated)
3. Enter the key in the file key field and click "Decript" to decrypt

### Command Line Interface
Run the core system:
```python
python Kr_2_Core_System.py
```

**Available Commands:**
- `enc "path\to\file.txt" t` - Encrypt file
- `enc "path\to\file.txt" f` - Decrypt file  
- `enc "path\to\file.txt" rec` - Recovery mode
- `keys` - Show all generated keys
- `delkeys` - Delete all stored keys
- `cls` - Clear terminal
- `help` - Show help
- `exit` - Exit program

### Direct Function Usage
```python
from files.Kr_2 import Kr2

# Text encryption
key, encrypted_output = Kr2("Hello World", "t")

# Text decryption  
Kr_2.key = "your-generated-key"
decrypted_text = Kr2("encrypted text", "f")

# File encryption
Kr2("path/to/file.txt", "t")

# File decryption
Kr_2.key = "your-key"
Kr2("path/to/file.txt", "f")
```

## Parameters

- `text/file_name`: Text to encrypt or path to the file for encryption/decryption
- `method`: 
  - `"t"` or `"T"` - Encryption (generates new key)
  - `"f"` or `"F"` - Decryption (requires existing key)
  - `"rec"` - Recovery mode for incorrectly decrypted files

## How It Works

1. **Key Generation**: Creates a 6-segment key from printable ASCII characters (41 characters total)
2. **Mapping**: Each key segment (segments 1-4) is used to create an encryption map for states an1-an4
3. **Rules**: First segment defines 256 rules for state transitions
4. **Starting Sequence**: Last segment determines initial 4-state sequence
5. **Encryption**: Each character is encrypted based on current state and rules
   - Uses a sliding window of 4 states
   - Output is organized in rows of up to 32 hexadecimal values
   - State transitions follow predefined rules
6. **Decryption**: Reverses the process using the same key and rules

## Files

- `Kr 2.pyw` - Main GUI application
- `files/Kr_2.py` - Core encryption/decryption functions
- `files/Kr_2_Core_System.py` - Command line interface
- `files/keys.txt` - File with stored keys (auto-generated)
- `files/images/Icons/` - Application icons and graphics
- `README.md` - This documentation

## Example

### GUI Usage
1. Launch `Kr 2.pyw`
2. Enter "Hello World" in INPUT field
3. Click "Encript" - generates key and shows encrypted output
4. Copy the key and encrypted text
5. Clear fields, paste encrypted text and key
6. Click "Decript" to recover original text

### Command Line Usage
```bash
Kr_2# enc "test.txt" t
# Encrypts test.txt and generates key

Kr_2# enc "test.txt" f  
# Prompts for key and decrypts test.txt

Kr_2# keys
# Shows all generated keys
```

### Programming Interface
```python
from files.Kr_2 import Kr2

# Encrypt text
key, encrypted = Kr2("Secret Message", "t")
print(f"Key: {key}")
print(f"Encrypted: {encrypted}")

# Decrypt text
Kr_2.key = key
decrypted = Kr2(encrypted, "f")
print(f"Decrypted: {decrypted}")
```

## Security Features

- Uses 4 different substitution tables (an1, an2, an3, an4)
- Dynamically changes state during encryption using sliding window
- 256 unique rules for complex state transitions
- Pseudo-random key generation from printable ASCII characters
- Hexadecimal output format for additional obfuscation
- Key logging for recovery purposes
- Recovery mode for incorrectly decrypted files (~90% recovery rate)
- Error handling for invalid characters and malformed keys

## Requirements

- Python 3.x
- Tkinter (for GUI - usually included with Python)
- Standard libraries: `random`, `string`, `sys`, `os`, `datetime`, `time`, `ctypes`

## Installation

1. Clone or download the repository
2. Ensure all files are in correct directory structure
3. Run `Kr 2.pyw` for GUI or `Kr_2_Core_System.py` for CLI

## Version

Current version: 0.2.0 (Core System)

## Author

Created by CHEMISTER_SK

## License

See LICENSE file for license details.
