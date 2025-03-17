import zlib
import binascii
import math
from PIL import Image
import argparse
import sys

def title():
    print('+-----------------------------------------------------+')
    print('+                    CTF Misc                         +')
    print('+                   LZ77 Tools                        +')
    print('+                    By Dalock                        +')
    print('+-----------------------------------------------------+')

def parse_arguments():
    parser = argparse.ArgumentParser(description="LZ77 decompression tool")
    parser.add_argument('-r', '--read', type=str, required=True, help='Read the file and get the IDAT data')
    parser.add_argument('-M', required=False, choices=['Q','S','QS'], help='Mode: Q for QR code, S for string, QS for both')
    parser.add_argument('-o', '--output', type=str, required=False, help='Output the QRCode to a file')
    # parser.add_argument('-o', '--output', type=str, required='-M' in sys.argv and ('Q' in sys.argv or 'QS' in sys.argv), help='Output the QRCode to a file')
    return parser.parse_args()

def compressData(IDAT_PATH):
    print('+-----------------------------------------------------+')
    print('+                Decompress the data                  +')
    print('+-----------------------------------------------------+')
    # IDAT = input("Enter the IDAT data: ")
    IDAT = open(IDAT_PATH, 'r').read()
    DecompressedData = zlib.decompress(binascii.unhexlify(IDAT))
    result = binascii.hexlify(DecompressedData)
    print("[SUCCESS] Hex of the decompressed data: \n", result)

    lenth = len(DecompressedData)
    print("\nThe length of the decompressed data is: ", lenth)
    print()
    return DecompressedData, lenth


def checkIfQRCode(DecompressedData, lenth, Output_PATH):
    print('+-----------------------------------------------------+')
    print('+                Transfer to QR code                  +')
    print('+-----------------------------------------------------+')
    DecompressedData = DecompressedData.decode()
    if math.isqrt(lenth) ** 2 == lenth:
        side = math.isqrt(lenth)
        # Create a new image with mode '1' for 1-bit pixels, black and white
        img = Image.new('1', (side, side))

        # Load pixel data
        pixels = img.load()

        # Fill the image with the decompressed data
        for i in range(side):
            for j in range(side):
                if DecompressedData[i * side + j] == '1':
                    pixels[j, i] = 1
                else:
                    pixels[j, i] = 0
            #     print(pixels[j, i]," ", end="")
            # print()

        # Open and display the image
        img.show()
        # Save the image
        if Output_PATH is not None:
            img.save(Output_PATH)
        print("[SUCCESS] Transfer to QR code successfully.")
    else:
        print("[ERROR] It is not a QR code.")
    
    print()

def convertDecompressedDataToString(data):
    print('+-----------------------------------------------------+')
    print('+            Convert Decompressed Data to String      +')
    print('+-----------------------------------------------------+')
    # Ensure the data length is a multiple of 8
    if len(data) % 8 != 0:
        print("[ERROR] Data length is not a multiple of 8.")
        return None

    # Convert each 8 bits to a character
    result = ''.join([chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8)])
    print("[SUCCESS] Converted string: ", result)
    print()
    return result

def main():
    title()
    args = parse_arguments()
    IDAT_PATH = args.read
    Output_PATH = args.output
    Mode = args.M

    DecompressedData,lenth = compressData(IDAT_PATH)
    
    if Mode is not None:
        if 'Q' in Mode:
            checkIfQRCode(DecompressedData, lenth, Output_PATH)
        if 'S' in Mode:
            convertDecompressedDataToString(DecompressedData)

if __name__ == '__main__':
    main()