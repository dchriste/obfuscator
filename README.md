# obfuscator

## Usage
```
usage: obfuscator.py [-h] (-d TEXT | -e TEXT) -s SALT

encode and decode a string

optional arguments:
  -h, --help            show this help message and exit
  -d TEXT, --decode TEXT
                        decode an encoded string
  -e TEXT, --encode TEXT
                        encode a plain text string
  -s SALT, --salt SALT  salt to encode or decode with
```

## Examples:
### Input to Encode
```
py obfuscator.py -e "This script is nifty!" -s Himalayan
```
### Output
```
b'\x1c\x01\x04\x12L\x12\x1a\x13\x078\x1dM\x08\x1fA\x17\x08\x08<\x10L'
```
### Input to Decode
```
obfuscator.py -d "\x1c\x01\x04\x12L\x12\x1a\x13\x078\x1dM\x08\x1fA\x17\x08\x08<\x10L" -s Himalayan
```
[Note the input to decode swaps the b'' wrapping for "". Future releases may remove this necessity.]

### Output
```
This script is nifty!
```
