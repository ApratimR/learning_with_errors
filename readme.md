# LAT-LWE-4

A Lattice(LAT) based Asymetric public-key encryption algorithm based on learning with errors(LWE) problem.

It uses methods which are proposed to be secure against cryptanalytic attack by a quantum computer.

The Name LWE-4 is derived from the max half-error amount percentage during the key generation which comes to around 4 percet thus deriving the name LWE-4

## How to use

```python
import LWE4 as lwe
import json
import secrets

# genetaring a test string to encrypt
original_string = secrets.token_hex(16)

# generating the keys for encryption process
private_key,public_key = lwe.keygen.keygen(50,8096)

# converting string data to json
private_key = json.loads(private_key)
public_key = json.loads(public_key)

# using public key to encrypt the test string
encrypted_string = json.loads(lwe.encrypt.encrypt(original_string,public_key))

# decrypting the string using private key
decrypted_string = json.loads(lwe.decrypt.decrypt(encrypted_string,private_key))

# comparing the string to check for error observed for particular public and private key combo
if original_string != decrypted_string:
    print("ERROR",private_key,public_key)
```

You can directly look into the test.py or brute_force_test.py files from the repo to directly start the testing after cloning the repo.
Or you can directly use the Jupyter notebook for testing/playing around in the playground which i had been using for my development preocess.

## NOTE !

* This is still an indevelopment project and shouldn't be used for any production usecase.