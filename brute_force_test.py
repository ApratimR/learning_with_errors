import lwe
import json
import secrets
from multiprocessing import Process,freeze_support


def function():
    # genetaring a test string to encrypt
    for temp in range(50):
        original_string = secrets.token_hex(16)

        # generating the keys for encryption process
        private_key,public_key = lwe.keygen.keygen(30,1024)

        # converting string data to json
        private_key = json.loads(private_key)
        public_key = json.loads(public_key)

        # using public key to encrypt the test string
        encrypted_string = json.loads(lwe.encrypt.encrypt(original_string,public_key))

        # decrypting the string using private key
        decrypted_string = json.loads(lwe.decrypt.decrypt(encrypted_string,private_key))

        # comparing the string to check for error observed for particular public and private key combo
        if original_string != decrypted_string:
            print("ERROR",private_key,public_key,original_string)

        else:
            print("Process Done")
        
if __name__ == "__main__":
    freeze_support()
    p1 = Process(function())
    p2 = Process(function())
    p3 = Process(function())
    p4 = Process(function())

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()

        
        