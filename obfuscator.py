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
    data = obfuscate(inStr.encode(encoding='utf-8'))
    return data

def myDecode(inBytes):
    data = obfuscate(inBytes).decode(encoding='utf-8')
    return data

def rawbytes(s):
    #https://stackoverflow.com/questions/42795042/how-to-cast-a-string-to-bytes-without-encoding
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

#to Debug Decode
#str2decode = input('Enter the hash that needs decoded:')
#print(myDecode(rawbytes(str2decode)))

if not args.decode and not args.encode:
    parser.print_help()
else:
    if args.encode:
        print(myEncode(args.string))
    else:
        print(myDecode(rawbytes(args.string)))
