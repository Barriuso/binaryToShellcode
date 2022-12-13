#!/usr/bin/env python3
import argparse
import base64
'''Based on the script of FortyNorthSecurity. Thank you so much for doing the hard work.
 https://github.com/FortyNorthSecurity/RandomScripts/blob/main/Cobalt%20Scripts/shellcode_formatter.py

Edited by @_Barriuso  
'''

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def get_args():
    parser = argparse.ArgumentParser(description='Convert binary raw to different Shellcode formats')
    parser.add_argument('-f', '--file', dest='file', type=str, required=True, help='File to convert to Csharp')
    parser.add_argument('-c', '--csharp', dest='csharp', action="store_true",default=False,
                        help='Convert to Csharp')
    parser.add_argument('-s', '--standard', dest='standard', action="store_true", default=False,
                        help='Convert to standard Shellcode')
    parser.add_argument('--fsharp', dest='fsharp',action="store_true", default=False,
                        help='Convert to fsharp Shellcode')
    parser.add_argument('--base64', dest='base64',action="store_true",  default=False,
                        help='Convert to Base64')
    return parser.parse_args()

def readFile(fileRead):
    try:
        with open(fileRead, 'rb') as sc_handle:
            return sc_handle.read()
    except FileNotFoundError:
        print (Color.RED+"The file does not exists.")

def writeToFile(filename,content):
    f = open(filename, "a+")
    f.write(content)
    f.close()

def convertShellcode(file,csharp,standard,fsharp,b64):
    # Just raw binary blog base64 encoded
    if (b64):
        encoded_raw = base64.b64encode(file)
        print(Color.GREEN+"Your base64 raw shellcode is in file called base64_raw.txt")
        writeToFile("base64_raw.txt",encoded_raw.decode('ascii'))

    # Print in "standard" shellcode format \x41\x42\x43....
    binary_code = ''
    fs_code = ''
    for byte in file:
        binary_code += "\\x" + hex(byte)[2:].zfill(2)
        # this is for f#
        fs_code += "0x" + hex(byte)[2:].zfill(2) + "uy;"
    if (standard):
        print(Color.GREEN + "Your standard shellcode is in file called standard_shellcode.txt")
        writeToFile("standard_shellcode.txt",binary_code)
    if (fsharp):
        print(Color.GREEN + "Your fsharp shellcode is in file called fsharp_shellcode.txt")
        writeToFile("fsharp_shellcode.txt", fs_code)
    if (csharp):
        # Convert this into a C# style shellcode format
        cs_shellcode = "0" + ",0".join(binary_code.split("\\")[1:])
        print(Color.GREEN + "Your chsarp shellcode is in file called fsharp_shellcode.txt")
        writeToFile("csharp_shellcode.txt",cs_shellcode)
        # Base 64 encode the C# code (for use with certain payloads :))
        encoded_cs = base64.b64encode(cs_shellcode.encode())
        print(Color.GREEN + "Your chsarp shellcode is in base64 file called b64Csharp_shellcode.txt")
        writeToFile("b64Csharp_shellcode.txt", encoded_cs.decode('ascii'))

if __name__ == '__main__':
    args = get_args()
    file = args.file
    csharp = args.csharp
    fsharp = args.fsharp
    standard = args.standard
    b64 = args.base64
    if (b64 == False and csharp == False and fsharp == False and standard == False):
        print (Color.BOLD+Color.RED+"You need to put one shellcode format to convert the binary")
        exit()
    convertShellcode(readFile(file),csharp,standard,fsharp,b64)
