import src.LWE4 as lwe
import json
import secrets
from multiprocessing import Process


def function():
    # genetaring a test string to encrypt
    for temp in range(50):
        original_string = secrets.token_hex(16)

        parameter_value = secrets.randbelow(26)+4
        parameter_size = secrets.randbelow(10000)+1024

        # generating the keys for encryption process
        private_key,public_key = lwe.keygen.keygen(parameter_value,parameter_size)

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
    
    processes = []

    for temp in range(3):
        processes.append(Process(target = function))

    for pr in processes:
        pr.start()

    for pr in processes:
        pr.join()

    print("All Process Compleated")
    

        
        