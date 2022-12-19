# BinaryToShellcode
Convert binary raw to different shellcode formats. Usefull to adapt to other languages like csharp, fhsarp, etc.

## Introduction
Convert your binary in raw mode to different type of shellcodes like Csharp style. I did not found any script in python3. All the scripts were in python2.7. The hard work is done by FortyNorthSecurity. I just adapted it.  https://github.com/FortyNorthSecurity/RandomScripts/blob/main/Cobalt%20Scripts/shellcode_formatter.py

## Usage
```
usage: binaryToShellcode.py [-h] -f FILE [-o OUTPUT] [-c] [-s] [--fsharp] [--base64]

Convert binary raw to different Shellcode formats

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File to convert to Csharp
  -o OUTPUT, --output OUTPUT
                        Name of the output file
  -c, --csharp          Convert to Csharp
  -s, --standard        Convert to standard Shellcode
  --fsharp              Convert to fsharp Shellcode
  --base64              Convert to Base64
```
