
from cryptography.fernet import Fernet
from pathlib import Path
import hashlib


# File locations
BASE_DIR = Path(__file__).resolve().parent.parent
SAMPLE_FILE = BASE_DIR / "sample_student_record.txt"
ENCRYPTED_FILE = BASE_DIR / "encrypted_student_record.bin"
DECRYPTED_FILE = BASE_DIR / "decrypted_student_record.txt"
HASH_FILE = BASE_DIR / "student_record.sha256"
KEY_FILE = BASE_DIR / "secret.key"


def generate_key():
    """Generate and save an encryption key if one does not exist."""
    if not KEY_FILE.exists():
        key = Fernet.generate_key()
        KEY_FILE.write_bytes(key)
        print("Encryption key generated.")
    else:
        print("Encryption key already exists.")


def load_key():
    """Load the encryption key."""
    if not KEY_FILE.exists():
        raise FileNotFoundError("Encryption key not found.")
    return KEY_FILE.read_bytes()


def encrypt_file():
    """Encrypt the sample student record."""
    if not SAMPLE_FILE.exists():
        raise FileNotFoundError("Sample student record not found.")

    key = load_key()
    cipher = Fernet(key)

    data = SAMPLE_FILE.read_bytes()
    encrypted_data = cipher.encrypt(data)

    ENCRYPTED_FILE.write_bytes(encrypted_data)
    print("File encrypted successfully.")


def decrypt_file():
    """Decrypt the encrypted student record."""
    if not ENCRYPTED_FILE.exists():
        raise FileNotFoundError("Encrypted file not found.")

    key = load_key()
    cipher = Fernet(key)

    encrypted_data = ENCRYPTED_FILE.read_bytes()
    decrypted_data = cipher.decrypt(encrypted_data)

    DECRYPTED_FILE.write_bytes(decrypted_data)
    print("File decrypted successfully.")


def calculate_hash():
    """Calculate and save a SHA-256 hash of the original file."""
    if not SAMPLE_FILE.exists():
        raise FileNotFoundError("Sample student record not found.")

    file_data = SAMPLE_FILE.read_bytes()
    file_hash = hashlib.sha256(file_data).hexdigest()

    HASH_FILE.write_text(file_hash)
    print("SHA-256 hash created.")
    print(file_hash)


def verify_integrity():
    """Check whether the original file has been changed."""
    if not SAMPLE_FILE.exists():
        raise FileNotFoundError("Sample student record not found.")

    if not HASH_FILE.exists():
        raise FileNotFoundError("Hash file not found.")

    current_hash = hashlib.sha256(SAMPLE_FILE.read_bytes()).hexdigest()
    saved_hash = HASH_FILE.read_text().strip()

    if current_hash == saved_hash:
        print("Integrity check: PASS - file has not been changed.")
        return True
    else:
        print("Integrity check: FAIL - file has been changed.")
        return False


def main():
    try:
        generate_key()
        encrypt_file()
        decrypt_file()

        # Verify that decrypted content matches the original
        original = SAMPLE_FILE.read_bytes()
        decrypted = DECRYPTED_FILE.read_bytes()

        if original == decrypted:
            print("Decryption verification: PASS - content matches original.")
        else:
            print("Decryption verification: FAIL - content does not match.")

        calculate_hash()
        verify_integrity()

    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()