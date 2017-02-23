import binascii
import sys

def decode(str):
    temp_string = binascii.unhexlify(str)
    temp_string = temp_string.decode("utf-8")

    return temp_string

def encode(str):
    temp_string = ""
    
    for c in str:
        temp_string += "{:x}".format(ord(c))

    return temp_string

def main():
    encoded_string = input("input string: ")
    
    decoded_string = decode(encoded_string)

    print("decoded string: {}".format(decoded_string))

if __name__ == "__main__":
    main()

