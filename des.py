IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

S_BOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28,
       15, 6, 21, 10, 23, 19, 12, 4,
       26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56,
       34, 53, 46, 42, 50, 36, 29, 32]

ROTATIONS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def hex_to_bin(input_hex):
    return bin(int(input_hex, 16))[2:].zfill(len(input_hex) * 4)

def bin_to_hex(input_bin):
    return hex(int(input_bin, 2))[2:].upper().zfill(len(input_bin) // 4)

def text_to_bin(input_text):
    return ''.join(format(ord(char), '08b') for char in input_text)

def bin_to_text(input_bin):
    text = ""
    for i in range(0, len(input_bin), 8):
        byte = input_bin[i:i+8]
        char_code = int(byte, 2)
        if char_code > 0:
            text += chr(char_code)
    
    #Erase padding
    if text:
        end_padding = ord(text[-1])
        if end_padding <= 8 and text.endswith(chr(end_padding) * end_padding):
            return text[:-end_padding]
    return text

def pad(input_bin):
    block_size = 64
    padding_len = block_size - (len(input_bin) % block_size)
    if padding_len == 0:
        padding_len = block_size
        
    padding_bytes = padding_len // 8
    padding_bin = format(padding_bytes, '08b') * padding_bytes
    return input_bin + padding_bin

def permute(block, table):
    return "".join(block[i - 1] for i in table)

def xor(a, b):
    return "".join('1' if x != y else '0' for x, y in zip(a, b))

def sbox_substitute(block_48bit):
    result = ""
    for i in range(8):
        chunk = block_48bit[i*6 : (i+1)*6]
        row = int(chunk[0] + chunk[5], 2)
        col = int(chunk[1:5], 2)
        val = S_BOX[i][row][col]
        result += format(val, '04b')
    return result

def gen_subkeys(key_64bit):
    key_56bit = permute(key_64bit, PC1)
    C, D = key_56bit[:28], key_56bit[28:]
    subkeys = []
    for shift in ROTATIONS:
        C = C[shift:] + C[:shift]
        D = D[shift:] + D[:shift]
        subkey = permute(C + D, PC2)
        subkeys.append(subkey)
    return subkeys

def process_block(block_64bit, subkeys):
    block_64bit = permute(block_64bit, IP)
    L, R = block_64bit[:32], block_64bit[32:]

    for i in range(16):
        R_more = permute(R, E)
        R_xor = xor(R_more, subkeys[i])
        s_substituted = sbox_substitute(R_xor)
        p_permuted = permute(s_substituted, P)
        
        new_R = xor(L, p_permuted)
        L = R
        R = new_R

    return permute(R + L, FP)

def run_des(input_message, input_key_string, mode='encrypt'):
    if len(input_key_string) != 8:
        raise ValueError("Key must be exactly 8 characters.")
        
    key_bin = text_to_bin(input_key_string)
    subkeys = gen_subkeys(key_bin)
    
    if mode == 'encrypt':
        bin_data = text_to_bin(input_message)
        padded_data = pad(bin_data)
        process_func = lambda block: process_block(block, subkeys)
        output_converter = bin_to_hex
        input_blocks = [padded_data[i:i+64] for i in range(0, len(padded_data), 64)]

    elif mode == 'decrypt':
        bin_data = hex_to_bin(input_message)
        if len(bin_data) % 64 != 0:
            raise ValueError("Somehow bin_data is not multiple of 64 bits.")
        
        reversed_subkeys = list(reversed(subkeys))
        process_func = lambda block: process_block(block, reversed_subkeys)
        output_converter = bin_to_text
        input_blocks = [bin_data[i:i+64] for i in range(0, len(bin_data), 64)]
    
    else:
        raise ValueError("Error. Choose decrypt or encrypt.")

    processed_bin = "".join(process_func(block) for block in input_blocks)
    return output_converter(processed_bin)