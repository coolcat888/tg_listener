from hexbytes import HexBytes
from web3.datastructures import AttributeDict
tx_data = AttributeDict({'blockHash': HexBytes('0x357d891537fe1c4ee8804ae8e1b14ad53a4a93ed8bf0fca27fe40e044f07b387'), 'blockNumber': 15674540, 'from': '0xDE99ec550313791471156dE29a54ea0c8D9ECEa5', 'gas': 750000, 'gasPrice': 5000100000, 'hash': HexBytes('0x929e23445858fa6fbb56d73bc81dd799980f27f28721b0629d16016e6aadec96'), 'input': '0x38ed173900000000000000000000000000000000000000000000008818cd2df8c9df243f00000000000000000000000000000000000000000000000053e4599ad69c70e000000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000de99ec550313791471156de29a54ea0c8d9ecea500000000000000000000000000000000000000000000000000000000621ddcaa000000000000000000000000000000000000000000000000000000000000000200000000000000000000000055d398326f99059ff775485246999027b3197955000000000000000000000000bb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c', 'nonce': 34881, 'to': '0x3a6d8cA21D1CF76F653A67577FA0D27453350dD8', 'transactionIndex': 56, 'value': 0, 'type': '0x0', 'v': 147, 'r': HexBytes('0xad828a02812cda3581abd96edba856859082ca66e07ef4e71eac14b93e4b48ff'), 's': HexBytes('0x3153041c50b25104a922cc627ee787d01d1a1ccb27ec58fb66d052801e7667cb')})
receipt_data = AttributeDict({'blockHash': HexBytes('0x357d891537fe1c4ee8804ae8e1b14ad53a4a93ed8bf0fca27fe40e044f07b387'), 'blockNumber': 15674540, 'contractAddress': None, 'cumulativeGasUsed': 4847784, 'from': '0xDE99ec550313791471156dE29a54ea0c8D9ECEa5', 'gasUsed': 32509, 'logs': [], 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'), 'status': 0, 'to': '0x3a6d8cA21D1CF76F653A67577FA0D27453350dD8', 'transactionHash': HexBytes('0x929e23445858fa6fbb56d73bc81dd799980f27f28721b0629d16016e6aadec96'), 'transactionIndex': 56, 'type': '0x0'})