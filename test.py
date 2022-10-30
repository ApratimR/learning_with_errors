import lwe
import json

temp = json.loads(lwe.keygen.keygen(4,1024))

lwe.encrypt.encrypt("🤣bPeShVmYq3t6v9\ny$B&E)H@McQfTjWnZr",temp["public_key"])