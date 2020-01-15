import os
import sys
from validator import Validator

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
