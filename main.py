import os
import sys
import base64
from validator import Validator
from parser import Parser

if len(sys.argv) != 2:
    print('Requires file path to XML file to validate')
    sys.exit(1)

validator = Validator("exchange/Claim-2.0.xsd")

if validator.validate(sys.argv[1]):
    print('Valid! :)')
else:
    print('Not valid! :(')
    #print(validator.getLastError())
    validator.printErrors()
    sys.exit(1)

parser = Parser(sys.argv[1])
encodedAttachment = parser.getNodeValue("/cld:Claim/cld:Attachments/nc:Attachment/nc:BinaryBase64Object")
print(encodedAttachment)
decodedAttachment = bytearray(base64.b64decode(encodedAttachment))

f = open("test.pdf", "w+b")
f.write(decodedAttachment)
f.close()
