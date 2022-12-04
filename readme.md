# LAT-LWE-4

A Lattice(LAT) based Asymetric public-key encryption algorithm based on learning with errors(LWE) problem.

The amount of error introdcued during the encryption process is around 4 percent of the key space size for each dimension increment thus deriving the name LAT-LWE-4.

#### How to use

```python
import lwe
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

# Todo

* implement checks for any fault
* set and test the keygen thresholds
