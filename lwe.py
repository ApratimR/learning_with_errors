import secrets
import json
from typing import List
import base64

class keygen:
    
    #gnerate value between the given range 
    @staticmethod
    def __gen_val(size:int):
        return secrets.randbelow(size)
    
    
    @staticmethod
    def keygen(parameters:int,size:int):
        
        if not(3 < parameters and parameters <= 10):
            raise Exception("Parameter value invalid")
        
        if not(512 < size and size <= 2048):
            raise Exception("size value invalid")
        
        
        private_key_array = [0]*parameters
        for temp in range(parameters):
            private_key_array[temp] = keygen.__gen_val(size)
            
        key_set = {"private_key" : private_key_array}
        
        equations_to_generate = 2 * parameters
        
        equation_set = []
        
        for temp in range(equations_to_generate):
            temp_eq = []
            eq_sol = 0
            for temp1 in range(parameters):
                temp_val = keygen.__gen_val(size)
                temp_eq.append(temp_val)
                eq_sol += (temp_val*private_key_array[temp1])
            
            temp_eq.append((eq_sol+(keygen.__gen_val(size)//10))%size)
            equation_set.append(temp_eq)

        key_set["public_key"] = equation_set
        key_set['ring_size'] = size
        return json.dumps(key_set)

# data = int('0b'+data,2)
# data = data.to_bytes((data.bit_length() + 7) // 8, 'big').decode()

class encrypt():
    @staticmethod
    def encrypt(data:str,public_key:List[List[int]],ring_size:int):
        
        data = bin(int.from_bytes(data.encode(), "big"))[2:]
        
        encrypted_data = []
        
        for temp in data:
            encrypted_data.extend(encrypt.encrypt_bit(temp,public_key,ring_size))
        
        payload = {}

        payload['ring_size']= ring_size
        payload['data']= encrypted_data
        payload['count'] = "INSERT SOMETHING HERE"
        print(payload)

    @staticmethod
    def encrypt_bit(bit,public_key,ring_size):
        equation_set_lenght=len(public_key)
        equation_parameter_size = len(public_key[0])-1
        
        if bit == 0:
            error = keygen.__gen_val(ring_size)//20
        else:
            error = secrets.choice(range((ring_size//2)-(ring_size//10),ring_size//2))
        

        selection_acceptable = True
        while selection_acceptable :
            selection_list = [secrets.randbelow(2) for _ in range(equation_set_lenght)]
            if selection_list.count(1)==(equation_parameter_size):
                selection_acceptable = False
        
        sum_array = [0]*(equation_parameter_size+1)
        for temp in range(len(public_key)):
            if selection_list[temp] == 1:
                sum_array = [sum(value) for value in zip(sum_array,public_key[temp])]
        
        sum_array[-1] = sum_array[-1]+error

        
        sum_array = [(x)%ring_size for x in sum_array]

        return sum_array
        
        