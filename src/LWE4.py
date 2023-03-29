import secrets
import json


class keygen:
    # gnerate value between the given range
    @staticmethod
    def __gen_val(size: int):
        return secrets.randbelow(size)

    @staticmethod
    def keygen(parameters: int, size: int):

        if not (3 < parameters and parameters <= 30):
            raise Exception("Parameter value invalid")

        if not (1024 <= size ):
            raise Exception("size value invalid")
        private_key_array = [0] * parameters
        for temp in range(parameters):
            private_key_array[temp] = keygen.__gen_val(size)

        key_set_private = {"private_key": private_key_array,'ring_size':size}

        equations_to_generate = 2 * parameters

        equation_set = []

        for temp in range(equations_to_generate):
            temp_eq = []
            eq_sol = 0
            for temp1 in range(parameters):
                temp_val = keygen.__gen_val(size)
                temp_eq.append(temp_val)
                eq_sol += temp_val * private_key_array[temp1]

            temp_eq.append((eq_sol + (keygen.__gen_val(int(size * 0.008)))) % size)
            equation_set.append(temp_eq)

        key_set_public = {}
        key_set_public["public_key"] = equation_set
        key_set_public["ring_size"] = size
        
        key_set_private = json.dumps(key_set_private)
        key_set_public = json.dumps(key_set_public)
        return key_set_private,key_set_public



class encrypt:
    @staticmethod
    def encrypt(data: str, public_key):
        ring_size = public_key['ring_size']
        public_key = public_key['public_key']
        data = bin(int.from_bytes(data.encode(), "big"))[2:]

        encrypted_data = []
        for temp in data:
            encrypted_data.extend(encrypt.encrypt_bit(temp, public_key, ring_size))

        payload = {}
        payload["data"] = encrypted_data
        return json.dumps(payload)

    @staticmethod
    def encrypt_bit(bit, public_key, ring_size):
        equation_set_lenght = len(public_key)
        equation_parameter_size = len(public_key[0]) - 1

        if bit == '0':
            error = secrets.choice(
                range(ring_size//50)
            )
        else:
            error = secrets.choice(
                range((ring_size // 2) - ring_size//50, ring_size // 2)
            )
        
        selection_acceptable = True
        while selection_acceptable:
            selection_list = [secrets.randbelow(2) for _ in range(equation_set_lenght)]
            if selection_list.count(1) == (equation_parameter_size):
                selection_acceptable = False

        sum_array = [0] * (equation_parameter_size + 1)
        for temp in range(len(public_key)):
            if selection_list[temp] == 1:
                sum_array = [sum(value) for value in zip(sum_array, public_key[temp])]

        sum_array[-1] = sum_array[-1] + error

        sum_array = [(x) % ring_size for x in sum_array]

        return sum_array


class decrypt:
    @staticmethod
    def decrypt(payload,private_key):
        ring_size = private_key['ring_size']
        private_key = private_key['private_key']
        count = len(private_key)+1
        if isinstance(payload,dict) and all(key in payload for key in ['data']):
            #ensure the size of data
            data = payload['data']
            equation_set = []
            if len(data)%(count) == 0:
                for temp in range(len(data)//(count)):
                    equation_set.append(data[temp*count : (temp+1)*count])
                bin_data = ""
                for temp in equation_set:
                    bin_data += '1' if decrypt.solve_equation(private_key,temp,ring_size) else '0'
                
                bin_data = int('0b'+bin_data,2)
                bin_data = bin_data.to_bytes((bin_data.bit_length() + 7) // 8, 'big').decode()
                return json.dumps(bin_data)
            else:
                raise Exception("Invalid equation set and lattice dimentions recived")

    
    @staticmethod
    def solve_equation(private_key,data,ring_size):
        sum_actual = 0
        error_sum = data[-1]
        for temp in range(len(private_key)):
            sum_actual += (private_key[temp]*data[temp])
        
        sum_actual = sum_actual % ring_size
        error_amount = abs(error_sum-sum_actual)
        error_amount = abs(error_amount - (ring_size//2))
        error_percentage = (error_amount/(ring_size//2))*100
        return error_percentage < 50