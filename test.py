import lwe
import json
import secrets
from multiprocessing import Process

def func():
    test_string = secrets.token_hex(16)
    temp = json.loads(lwe.keygen.keygen(50,10240))
    temp1 = json.loads(lwe.encrypt.encrypt(test_string,temp["public_key"],temp['ring_size']))
    if test_string == json.loads(lwe.decrypt.decrypt(temp1,temp['private_key'])):
        pass
    else:
        print("ERROR",temp,temp1)

for temp in range(50):
    p1 = Process(target=func)
    p1.start()
    p2 = Process(target=func)
    p2.start()
    p3 = Process(target=func)
    p3.start()
    p4 = Process(target=func)
    p4.start()
    # p5 = Process(target=func)
    # p5.start()
    # p6 = Process(target=func)
    # p6.start()
    # p7 = Process(target=func)
    # p7.start()
    # p8 = Process(target=func)
    # p8.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    # p5.join()
    # p6.join()
    # p7.join()
    # p8.join()
    
print("DONE OPERATION")