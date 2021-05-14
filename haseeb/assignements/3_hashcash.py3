##################################
#            PART 1              #
##################################
from hashlib import sha256

#creates a sha256 digest
def _sha2(s):
  return sha256(s.encode()).hexdigest()


#helper function that tells me how many leading zeros there are in the binary representation
def binary_leading_0s(hex_str: str):
    binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
    return len(binary_representation) - len(binary_representation.lstrip('0'))


def is_valid(token: str, date: str, email: str, difficulty: int) -> bool:
  token_split = token.split(":")

  if token_split[2] != email:
    return False
  elif len(date) != 6:
    return False
  elif len(token_split[3]) != 16:
    return False
  
  sha_digest = _sha2(token)
  if binary_leading_0s(sha_digest) < difficulty:
    return False

  return True 


# print(binary_leading_0s(_sha2("1:081031:satoshin@gmx.com:b4c26b1694691666")))

print(is_valid("1:210214:satoshin@gmx.com:32572a910499e4b8",
               "210214", "satoshin@gmx.com", 16))

##################################
#            PART 2              #
##################################

def mint(date: str, email: str, difficulty: int) -> str:
  pass  # Your code here
