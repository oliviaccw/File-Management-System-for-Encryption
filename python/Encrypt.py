from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import os


def encrypt_file_with_pwd(input_file, output_file, pwd):
    # Generate the key
    key = get_key_from_pwd(pwd)

    # Generate an IV (Initialization Vector)
    iv = b'\x00' * 16

    # Create a Cipher object with AES algorithm in CFB mode
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    # Create an encryptor object
    encryptor = cipher.encryptor()

    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        while True:
            chunk = f_in.read(8192)
            if not chunk:
                break
            encrypted_chunk = encryptor.update(chunk)
            f_out.write(encrypted_chunk)

def decrypt_file_with_pwd(input_file, output_file, pwd):
    # Generate the key
    key = get_key_from_pwd(pwd)

    # Generate an IV (Initialization Vector)
    iv = b'\x00' * 16

    # Create a Cipher object with AES algorithm in CFB mode
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    # Create a decryptor object
    decryptor = cipher.decryptor()

    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        while True:
            chunk = f_in.read(8192)
            if not chunk:
                break
            decrypted_chunk = decryptor.update(chunk)
            f_out.write(decrypted_chunk)

def get_key_from_pwd(pwd):
    pwd = pwd.encode()  # convert pwd to byte

    # Derive a key from the user-entered password
    salt = b'\x00' * 16  # Salt value for key derivation
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 key size
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(pwd)
    return key      # type: bytes

##########################################################

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    
    return private_key, public_key

def save_private_key(private_key, password, filename):
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    )
    with open(filename, 'wb') as file:
        file.write(private_key_pem)

def save_private_key_without_pwd(private_key, file_path):
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(file_path, 'wb') as file:
        file.write(private_key_pem)

def save_public_key(public_key, filename):
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(filename, 'wb') as file:
        file.write(public_key_pem)

def encrypt_file_with_RSA_AES(input_file, output_folder, public_key_file, encrypted_symmetric_key_folder):
    # Load the recipient's public key
    with open(public_key_file, 'rb') as file:
        recipient_public_key = serialization.load_pem_public_key(
            file.read(),
            backend=default_backend()
        )

    # Generate a random symmetric key for AES encryption
    symmetric_key = os.urandom(32)

    # Encrypt the symmetric key using RSA
    encrypted_symmetric_key = recipient_public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save the encrypted symmetric key to a file
    # filename = input_file name + input_file ext
    # file ext = .bin
    encrypted_symmetric_key_filename = f'{os.path.basename(input_file)}.bin'
    encrypted_symmetric_key_file = os.path.join(encrypted_symmetric_key_folder, encrypted_symmetric_key_filename)
    with open(encrypted_symmetric_key_file, 'wb') as file:
        file.write(encrypted_symmetric_key)

    # Generate a random IV for AES encryption
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())

    # Save the encrypted file
    # filename = input_file name + input_file ext
    # file ext = .bin
    output_file_name = f'{os.path.basename(input_file)}.bin'
    output_file = os.path.join(output_folder, output_file_name)
    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        encryptor = cipher.encryptor()

        # Write the IV to the output file first
        file_out.write(iv)

        while True:
            chunk = file_in.read(16 * 1024)  # 16KB
            if len(chunk) == 0:
                break
            encrypted_chunk = encryptor.update(chunk)
            file_out.write(encrypted_chunk)

def decrypt_file_with_RSA_AES(input_file, output_file, private_key_file, encrypted_symmetric_key_file, password):
    # Load the private key for decryption
    with open(private_key_file, 'rb') as file:
        private_key = serialization.load_pem_private_key(
            file.read(),
            password=password.encode(),
            backend=default_backend()
        )

    # Load the encrypted symmetric key
    with open(encrypted_symmetric_key_file, 'rb') as file:
        encrypted_symmetric_key = file.read()

    # Decrypt the symmetric key using RSA
    symmetric_key = private_key.decrypt(
        encrypted_symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt the file using the symmetric key and AES
    with open(input_file, 'rb') as file_in:
        # Read the IV from the input file first (the first 16 bytes)
        iv = file_in.read(16)

        cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        with open(output_file, 'wb') as file_out:
            while True:
                chunk = file_in.read(16 * 1024)  # 16KB
                if len(chunk) == 0:
                    break
                decrypted_chunk = decryptor.update(chunk)
                file_out.write(decrypted_chunk)

def generate_and_save_encrypted_symmetric_key(public_key, encrypted_symmetric_key_file):
    # Generate a random symmetric key for AES encryption
    symmetric_key = os.urandom(32)

    # Encrypt the symmetric key using RSA
    encrypted_symmetric_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save the encrypted symmetric key to a file
    with open(encrypted_symmetric_key_file, 'wb') as file:
        file.write(encrypted_symmetric_key)

def generate_and_save_symmetric_key(symmetric_key_file):
    # Generate a random symmetric key for AES encryption
    symmetric_key = os.urandom(32)

    # Save the symmetric key to a file
    with open(symmetric_key_file, 'wb') as file:
        file.write(symmetric_key)

# This method use to deal with the case that the user provide the private key file and encrypted symmetric key file for the encryption
def encrypt_file_with_RSA_given_AES_key(input_file, output_file, private_key_file, encrypted_symmetric_key_file):
    # Load the recipient's public key
    with open(private_key_file, 'rb') as file:
        private_key = serialization.load_pem_private_key(
            file.read(),
            password=None,
            backend=default_backend()
        )

    # Load the encrypted symmetric key
    with open(encrypted_symmetric_key_file, 'rb') as file:
        encrypted_symmetric_key = file.read()

    # Decrypt the symmetric key using RSA
    symmetric_key = private_key.decrypt(
        encrypted_symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Generate a random IV for AES encryption
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())

    # Save the encrypted file
    # file ext = .bin
    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        encryptor = cipher.encryptor()

        # Write the IV to the output file first
        file_out.write(iv)

        while True:
            chunk = file_in.read(16 * 1024)  # 16KB
            if len(chunk) == 0:
                break
            encrypted_chunk = encryptor.update(chunk)
            file_out.write(encrypted_chunk)

# This method use to deal with the case that the given private key is not encrypted
def decrypt_file_with_RSA_AES_without_pwd(input_file, output_file, private_key_file, encrypted_symmetric_key_file):
    # Load the private key for decryption
    with open(private_key_file, 'rb') as file:
        private_key = serialization.load_pem_private_key(
            file.read(),
            password=None,
            backend=default_backend()
        )

    # Load the encrypted symmetric key
    with open(encrypted_symmetric_key_file, 'rb') as file:
        encrypted_symmetric_key = file.read()

    # Decrypt the symmetric key using RSA
    symmetric_key = private_key.decrypt(
        encrypted_symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt the file using the symmetric key and AES
    with open(input_file, 'rb') as file_in:
        # Read the IV from the input file first (the first 16 bytes)
        iv = file_in.read(16)

        cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        with open(output_file, 'wb') as file_out:
            while True:
                chunk = file_in.read(16 * 1024)  # 16KB
                if len(chunk) == 0:
                    break
                decrypted_chunk = decryptor.update(chunk)
                file_out.write(decrypted_chunk)

def encrypt_file_with_RSA(input_file, output_file, public_key_file):
    # Load the public key
    with open(public_key_file, 'rb') as file:
        public_key = serialization.load_pem_public_key(
            file.read(),
            backend=default_backend()
        )

    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        # Encrypt the symmetric key using RSA
        ciphertext = public_key.encrypt(
            file_in.read(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        file_out.write(ciphertext)

def decrypt_file_with_RSA(input_file, output_file, private_key_file):
    # Load the private key for decryption
    with open(private_key_file, 'rb') as file:
        private_key = serialization.load_pem_private_key(
            file.read(),
            password=None,
            backend=default_backend()
        )

    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        plaintext = private_key.decrypt(
                    file_in.read(),
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
        )
        file_out.write(plaintext)
        plaintext = ''
                    
                    