import binascii
import sys, msvcrt

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
    str = "733N1GN3 1A>17T>313"
    str = input("input string: ")
    
    # encoded_string = encode(str)
    encoded_string = str

    # print("original string: {}".format(encoded_string))
    decoded_string = decode(encoded_string)

    print("decoded string: {}".format(decoded_string))

    print("press any key to exit...")
    msvcrt.getch()
    sys.exit(0)

if __name__ == "__main__":
    main()

