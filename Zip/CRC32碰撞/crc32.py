import binascii
import itertools
import string
import zipfile
import argparse
import os

def title():
    print('+-----------------------------------------------------+')
    print('+                    CTF Misc                         +')
    print('+           压缩包CRC32碰撞获取文件内容               +')
    print('+                    By Dalock                        +')
    print('+-----------------------------------------------------+')

# crc = binascii.crc32(b"flag") & 0xffffffff
def get_crc32_from_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        crc_list = {info.filename: info.CRC for info in zip_ref.infolist()}
    return crc_list

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process zip file and find CRC32 matches.")
    parser.add_argument('-r', '--zip_path', type=str, required=True, help='Path to the zip file')
    parser.add_argument('-b', '--char_count', choices=[1, 2, 3, 4, 5], type=int, required=True, help='Number of characters to brute force')
    return parser.parse_args()

def crc32Analysis(zip_path):
    print('+-----------------------------------------------------+')
    print('+                   压缩包 CRC32 分析                 +')
    print('+-----------------------------------------------------+')
    crc_values = {filename: hex(crc) for filename, crc in get_crc32_from_zip(zip_path).items()}
    print(f"ZipFileName: {os.path.basename(zip_path)}")
    for filename, crc in crc_values.items():
        print(f"Filename: {filename}, CRC32: {crc}")
    print()
    return crc_values

def crc32BruteForce(crc_values, char_count):
    print('+-----------------------------------------------------+')
    print('+                    CRC32 碰撞                       +')
    print('+-----------------------------------------------------+')
    # crc = 0xD1F4EB9A # crc of example
    printable_chars = string.printable.encode('ascii')
    # print(printable_chars) # b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

    result = ""
    for filename,crc in crc_values.items():
        crc = int(crc, 16)
        for combo in itertools.product(printable_chars, repeat=char_count):
            if binascii.crc32(bytes(combo)) & 0xffffffff == crc:
                result += bytes(combo).decode('ascii')
                print("FileName:",filename)
                print("CRC32:",hex(crc))
                print("Content:",bytes(combo).decode('ascii'))
                print()
                break
    print(result)

def main():
    title()
    args = parse_arguments()
    zip_path = args.zip_path
    char_count = args.char_count

    crc_values = crc32Analysis(zip_path)
    crc32BruteForce(crc_values, char_count)

if __name__ == "__main__":
    main()