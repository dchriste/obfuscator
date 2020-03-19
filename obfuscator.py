#python3.8

"""
take one string, return it obfuscated
code adapted from: https://stackoverflow.com/questions/7488995/python-efficient-obfuscation-of-string/7489718

I added argument parsing and i/o
"""
import argparse
import struct

parser = argparse.ArgumentParser(description='encode and decode a string')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d','--decode',help='decode an encoded string',action='store_true')
group.add_argument('-e','--encode',help='encode a plain text string',action='store_true')
parser.add_argument('string', help='a string to encode or decode',type=str)
args = parser.parse_args()

def obfuscate(byt):
    # Use same function in both directions.  Input and output are bytes
    # objects.
    mask = b'DaustinKratzerLacrosse'
    lmask = len(mask)
    return bytes(c ^ mask[i % lmask] for i, c in enumerate(byt))

def myEncode(inStr):
    data = obfuscate(inStr.encode())
    return data

def myDecode(inBytes):
    data = obfuscate(inBytes).decode()
    return data

def str_to_bytes(inStr):
    #function adapted from https://stackoverflow.com/questions/51754731/python-convert-strings-of-bytes-to-byte-array
    if inStr[0] =='\"': inStr = inStr[1:len(inStr)-1] #unwrap the quotes
    if inStr[0] == 'b': inStr = inStr[1:] #remove the byte indicator if present
    inStr = '\'' + inStr + '\''
    someBytes = b''
    for i in inStr:
        someBytes += struct.pack("B", ord(i))
    return someBytes

if not args.decode and not args.encode:
    parser.print_help()
else:
    if args.encode:
        print(myEncode(args.string))
    else:
        print(myDecode(str_to_bytes('\"' + args.string + '\"')))
