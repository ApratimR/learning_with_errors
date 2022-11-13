import lwe
import json

temp = json.loads(lwe.keygen.keygen(4,1024))
temp = lwe.encrypt.encrypt("🤣bPeShVmYq3t6v9\ny$B&E)H@McQfTjWnZr",temp["public_key"],temp['ring_size'])

lwe.decrypt.decrypt(temp)