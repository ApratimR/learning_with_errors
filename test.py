import lwe
import json

temp = json.loads(lwe.keygen.keygen(4,2048))
temp1 = json.loads(lwe.encrypt.encrypt("🤣bPeShVmYq3t6v9\ny$B&E)H@McQfT",temp["public_key"],temp['ring_size']))
print(lwe.decrypt.decrypt(temp1,temp['private_key']))