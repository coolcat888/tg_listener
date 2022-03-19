from hexbytes import HexBytes
from web3.datastructures import AttributeDict
tx_data = AttributeDict({'blockHash': HexBytes('0x273004c599db110263aa028ee287578d551d053e3de55fdf0e52dc68dd73c64c'), 'blockNumber': 15647639, 'from': '0xB4CDb76C29ae0386885B1b33e4F14db5b1D16fC2', 'gas': 138499, 'gasPrice': 5000000000, 'hash': HexBytes('0xe4502e017582a3786545d6b6a5b84c1e21a5c4fd1ac22266a4e304a9fa3a1853'), 'input': '0x38ed173900000000000000000000000000000000000000000000000052ea296c744b9f9800000000000000000000000000000000000000000000000038e45dd05fe76cd700000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000b4cdb76c29ae0386885b1b33e4f14db5b1d16fc200000000000000000000000000000000000000000000000000000000621ca20a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000b15ddf19d47e6a86a56148fb4afffc6929bcb89000000000000000000000000e9e7cea3dedca5984780bafc599bd69add087d56', 'nonce': 228, 'to': '0x10ED43C718714eb63d5aA57B78B54704E256024E', 'transactionIndex': 223, 'value': 0, 'type': '0x0', 'v': 148, 'r': HexBytes('0x7b9c341f2d745c2afba6191d3c788784bbde1a0269208481f99021d0b8a2258b'), 's': HexBytes('0x4040a3875aa1b27de2b785ee479d890e29a803d08f650feb800fbf13f5dcba94')})
receipt_data = AttributeDict({'blockHash': HexBytes('0x273004c599db110263aa028ee287578d551d053e3de55fdf0e52dc68dd73c64c'), 'blockNumber': 15647639, 'contractAddress': None, 'cumulativeGasUsed': 30468872, 'from': '0xB4CDb76C29ae0386885B1b33e4F14db5b1D16fC2', 'gasUsed': 104654, 'logs': [AttributeDict({'address': '0x0b15Ddf19D47E6a86A56148fb4aFFFc6929BcB89', 'topics': [HexBytes('0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'), HexBytes('0x000000000000000000000000b4cdb76c29ae0386885b1b33e4f14db5b1d16fc2'), HexBytes('0x00000000000000000000000010ed43c718714eb63d5aa57b78b54704e256024e')], 'data': '0x000000000000000000000000000000000de0b6b3a763fffc28095a3e11e6a3ea', 'blockNumber': 15647639, 'transactionHash': HexBytes('0xe4502e017582a3786545d6b6a5b84c1e21a5c4fd1ac22266a4e304a9fa3a1853'), 'transactionIndex': 223, 'blockHash': HexBytes('0x273004c599db110263aa028ee287578d551d053e3de55fdf0e52dc68dd73c64c'), 'logIndex': 928, 'removed': False}), AttributeDict({'address': '0x0b15Ddf19D47E6a86A56148fb4aFFFc6929BcB89', 'topics': [HexBytes('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'), HexBytes('0x000000000000000000000000b4cdb76c29ae0386885b1b33e4f14db5b1d16fc2'), HexBytes('0x00000000000000000000000071e6de81381efe0aa98f56b3b43eb3727d640715')], 'data': '0x00000000000000000000000000000000000000000000000052ea296c744b9f98', 'blockNumber': 15647639, 'transactionHash': HexBytes('0xe4502e017582a3786545d6b6a5b84c1e21a5c4fd1ac22266a4e304a9fa3a1853'), 'transactionIndex': 223, 'blockHash': HexBytes('0x273004c599db110263aa028ee287578d551d053e3de55fdf0e52dc68dd73c64c'), 'logIndex': 929, 'removed': False}), AttributeDict({'address': '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56', 'topics': [HexBytes('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'), HexBytes('0x00000000000000000000000071e6de81381efe0aa98f56b3b43eb3727d640715'), HexBytes('0x000000000000000000000000b4cdb76c29ae0386885b1b33e4f14db5b1d16fc2')], 'data': '0x000000000000000000000000000000000000000000000000392d3033f9fbc844', 'blockNumber': 15647639, 'transactionHash': HexBytes('0xe4502e017582a3786545d6b6a5b84c1e21a5c4fd1ac22266a4e304a9fa3a1853'), 'transactionIndex': 223, 'blockHash': HexBytes('0x273004c599db110263aa028ee287578d551d053e3de55fdf0e52dc68dd73c64c'), 'logIndex': 930, 'removed': False}), AttributeDict({'address': '0x71E6de81381eFE0Aa98f56b3B43eB3727D640715', 'topics': [HexBytes('0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1')], 'data': '0x000000000000000000000000000000000000000000009acfcc3b83f75c34fd98000000000000000000000000000000000000000000006b05a98e48d56df52c61', 'blockNumber': 15647639, 'transactionHash': HexBytes('0xe4502e017582a3786545d6b6a5b84c1e21a5c4fd1ac22266a4e304a9fa3a1853'), 'transactionIndex': 223, 'blockHash': HexBytes('0x273004c599db110263aa028ee287578d551d053e3de55fdf0e52dc68dd73c64c'), 'logIndex': 931, 'removed': False}), AttributeDict({'address': '0x71E6de81381eFE0Aa98f56b3B43eB3727D640715', 'topics': [HexBytes('0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822'), HexBytes('0x00000000000000000000000010ed43c718714eb63d5aa57b78b54704e256024e'), HexBytes('0x000000000000000000000000b4cdb76c29ae0386885b1b33e4f14db5b1d16fc2')], 'data': '0x00000000000000000000000000000000000000000000000052ea296c744b9f9800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000392d3033f9fbc844', 'blockNumber': 15647639, 'transactionHash': HexBytes('0xe4502e017582a3786545d6b6a5b84c1e21a5c4fd1ac22266a4e304a9fa3a1853'), 'transactionIndex': 223, 'blockHash': HexBytes('0x273004c599db110263aa028ee287578d551d053e3de55fdf0e52dc68dd73c64c'), 'logIndex': 932, 'removed': False})], 'logsBloom': HexBytes('0x00200202000000100000000080000000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000108200000000000000000000000000008000000200000000000000000000000000000000000000000000000001000000000000000000000000000000004000010000000000000000000000000000000000000000000200000000000080010004000000000020000000000000000000000020000000000000100000000000008004000000000000002000000020000000000001000000000000000001000000004000000000012000000000000000000000000000000000000000000000000000000000000'), 'status': 1, 'to': '0x10ED43C718714eb63d5aA57B78B54704E256024E', 'transactionHash': HexBytes('0xe4502e017582a3786545d6b6a5b84c1e21a5c4fd1ac22266a4e304a9fa3a1853'), 'transactionIndex': 223, 'type': '0x0'})