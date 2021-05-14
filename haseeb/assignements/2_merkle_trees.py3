#######################################
#              PART 1                 #
#######################################

from enum import Enum
from hashlib import sha256
import math


class Block:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


def merkleize(sentence):
    blocks = sentence.split(" ")
    if blocks == 1:
      return Block(sha256(blocks[0].encode()).hexdigest())
    base_layer_hash = []
    block_nodes = []
    # check if sent_split is a power of two
    # if it's not then keep adding padding chr(0)
    power = math.log(len(blocks), 2)
    while power - int(power) != 0:
        blocks.append(chr(0))
        power = math.log(len(blocks), 2)
    
    # create base hashed layer while making sure not to hash the padding 0 bytes
    for block in blocks:
        if block == chr(0):
          base_layer_hash.append(block)
        else:
          base_layer_hash.append(sha256(block.encode()).hexdigest())
  
    def create_block_nodes():
        for block in base_layer_hash:
            block_nodes.append(Block(block))

    create_block_nodes()
    build_tree(block_nodes)


def build_tree(base_layer):
    current_level = base_layer

    while len(current_level) > 1:
        new_level = []
        for i in range(1, len(current_level)):
            if i % 2 != 0:
              parent = Block(sha256((current_level[i-1].val + current_level[i].val).encode()).hexdigest())
              parent.left = current_level[i-1]
              parent.right = current_level[i]
              new_level.append(parent)

        current_level = new_level

    print(current_level[0].val)


# merkleize("I love chicken!")
# merkleize("hello world")  
# merkleize("hello")  
# merkleize("Oh joyous day!")  
# merkleize("I write this sitting in the kitchen sink.")  
# merkleize("It was a bright cold day in April, and the clocks were striking thirteen.")


#######################################
#              PART 2                 #
#######################################


class Side(Enum):
    LEFT = 0
    RIGHT = 1


def _sha2(s):
  return sha256(s.encode()).hexdigest()

def validate_proof(root, data, proof):

    # data_hashed = _sha2(data)
    print(proof[0][1].name)
    # if proof[0][1] == 1:
    #     combined_hash = _sha2(data_hashed + proof[0][0])

    # final = _sha2(proof[1][0] + combined_hash)

    # if final == root:
    #     return True
    # else:
    #     return False


#
print(Side.RIGHT.name)
validate_proof(1,1,1)
