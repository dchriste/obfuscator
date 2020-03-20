#python3.8

"""
This script functions as a symmetric cipher.
It takes one string and returns it obfuscated.
It takes the obfuscated string, and return it elucidated.

code adapted from: 
    (1) https://stackoverflow.com/questions/7488995/python-efficient-obfuscation-of-string/7489718
    (2) https://stackoverflow.com/questions/42795042/how-to-cast-a-string-to-bytes-without-encoding

The obfuscate function and concepts were adapted from (1).
The rawbytes function is lightly modified from (2).

I added i/o, argument parsing, variable salt, and combined the concepts.
"""

import argparse
import struct

parser = argparse.ArgumentParser(description='encode and decode a string')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d','--decode',help='decode an encoded string',nargs=1,metavar='TEXT')
group.add_argument('-e','--encode',help='encode a plain text string',nargs=1,metavar='TEXT')
parser.add_argument('-s', '--salt', help='salt to encode or decode with',type=str,required=True)
args = parser.parse_args()

def obfuscate(byt,mask):
    # Use same function in both directions.  
    # Input and output are bytes objects.
    lmask = len(mask)
    return bytes(c ^ mask[i % lmask] for i, c in enumerate(byt))

def myEncode(inStr,salt):
    data = obfuscate(inStr.encode(encoding='utf-8'),salt)
    return data

def myDecode(inBytes,salt):
    data = obfuscate(inBytes,salt).decode(encoding='utf-8')
    return data

def rawbytes(s):    
    """Convert a string to raw bytes without encoding"""
    if s[0] == 'b': s = s[1:] #remove the byte indicator if present
    if s[0] =='\"': s = s[1:len(s)-1] #unwrap the quotes
    s= bytes(s, "utf-8").decode("unicode_escape")
    outlist = []
    for cp in s:
        num = ord(cp)
        if num < 255:
            outlist.append(struct.pack('B', num))
        elif num < 65535:
            outlist.append(struct.pack('>H', num))
        else:
            b = (num & 0xFF0000) >> 16
            H = num & 0xFFFF
            outlist.append(struct.pack('>bH', b, H))
    return b''.join(outlist)

def main():
    saltyBytes = rawbytes(args.salt)
    if args.encode != None:
        print(myEncode(args.encode[0],saltyBytes))
    else:
        print(myDecode(rawbytes(args.decode[0]),saltyBytes))

if __name__ == "__main__":
    main()