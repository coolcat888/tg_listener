from hexbytes import HexBytes
from web3.datastructures import AttributeDict
tx_data = AttributeDict({'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'blockNumber': 15734117, 'from': '0xFC0E59008D817FD57D90a7B1bAB6fFb92CbaDb07', 'gas': 768730, 'gasPrice': 5355000000, 'hash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'input': '0x791ac947000000000000000000000000000000000000000001f04ef12cb04cf158000000000000000000000000000000000000000000000000000000021b1ad1e9af0d3600000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000fc0e59008d817fd57d90a7b1bab6ffb92cbadb070000000000000000000000000000000000000000000000000000000062209b62000000000000000000000000000000000000000000000000000000000000000200000000000000000000000015104336cf1c5bb4281ed1e12fecc5a1197e5e36000000000000000000000000bb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c', 'nonce': 194, 'to': '0xcd3d4Eb34385A2DDF470aeD617378EAae53082D4', 'transactionIndex': 30, 'value': 0, 'type': '0x0', 'v': 148, 'r': HexBytes('0xcb199dea0eee4b39a630d36d8f275ddd5d014e55b60c3d35ee538d386e2c3d75'), 's': HexBytes('0x2e1e437bbec81f009bd28e84e00772bedb34ca4e236609a6d0d786fa8725927c')})
receipt_data = AttributeDict({'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'blockNumber': 15734117, 'contractAddress': None, 'cumulativeGasUsed': 2999740, 'from': '0xFC0E59008D817FD57D90a7B1bAB6fFb92CbaDb07', 'gasUsed': 545458, 'logs': [AttributeDict({'address': '0x15104336cf1C5BB4281eD1E12fecc5A1197e5E36', 'topics': [HexBytes('0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'), HexBytes('0x00000000000000000000000015104336cf1c5bb4281ed1e12fecc5a1197e5e36'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4')], 'data': '0x00000000000000000000000000000000000000000027b661e2a4394e2df54809', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 81, 'removed': False}), AttributeDict({'address': '0x15104336cf1C5BB4281eD1E12fecc5A1197e5E36', 'topics': [HexBytes('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'), HexBytes('0x00000000000000000000000015104336cf1c5bb4281ed1e12fecc5a1197e5e36'), HexBytes('0x0000000000000000000000009625a4f2f6bec1b507e6d112ba5073e70f6ed3d9')], 'data': '0x00000000000000000000000000000000000000000027b661e2a4394e2df54809', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 82, 'removed': False}), AttributeDict({'address': '0x15104336cf1C5BB4281eD1E12fecc5A1197e5E36', 'topics': [HexBytes('0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'), HexBytes('0x00000000000000000000000015104336cf1c5bb4281ed1e12fecc5a1197e5e36'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4')], 'data': '0x0000000000000000000000000000000000000000000000000000000000000000', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 83, 'removed': False}), AttributeDict({'address': '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c', 'topics': [HexBytes('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'), HexBytes('0x0000000000000000000000009625a4f2f6bec1b507e6d112ba5073e70f6ed3d9'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4')], 'data': '0x000000000000000000000000000000000000000000000000003d3d7c17c2b540', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 84, 'removed': False}), AttributeDict({'address': '0x9625A4F2F6BEc1b507E6d112bA5073E70f6ed3d9', 'topics': [HexBytes('0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1')], 'data': '0x00000000000000000000000000000000000000007e8b5822cb6b449c75cee2fc000000000000000000000000000000000000000000000000c37d756a79e4c380', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 85, 'removed': False}), AttributeDict({'address': '0x9625A4F2F6BEc1b507E6d112bA5073E70f6ed3d9', 'topics': [HexBytes('0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4')], 'data': '0x00000000000000000000000000000000000000000027b661e2a4394e2df5480900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003d3d7c17c2b540', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 86, 'removed': False}), AttributeDict({'address': '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c', 'topics': [HexBytes('0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4')], 'data': '0x000000000000000000000000000000000000000000000000003d3d7c17c2b540', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 87, 'removed': False}), AttributeDict({'address': '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c', 'topics': [HexBytes('0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4')], 'data': '0x0000000000000000000000000000000000000000000000000025f80a60a6cc88', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 88, 'removed': False}), AttributeDict({'address': '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c', 'topics': [HexBytes('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4'), HexBytes('0x000000000000000000000000602b873e953cfcd7b5ae77e450e6c5a4c4decf1f')], 'data': '0x0000000000000000000000000000000000000000000000000025f80a60a6cc88', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 89, 'removed': False}), AttributeDict({'address': '0x4d40fdC44608585f2Fb7e0d022ff8948b8AD478e', 'topics': [HexBytes('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'), HexBytes('0x000000000000000000000000602b873e953cfcd7b5ae77e450e6c5a4c4decf1f'), HexBytes('0x000000000000000000000000aba7e39111630342f720e44e6517240b67351e4c')], 'data': '0x00000000000000000000000000000000000000000000000001d63be1b1f332f5', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 90, 'removed': False}), AttributeDict({'address': '0x602b873E953CFCd7B5AE77E450E6c5A4C4decF1f', 'topics': [HexBytes('0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1')], 'data': '0x00000000000000000000000000000000000000000000001da39e7157598123330000000000000000000000000000000000000000000000022bff1d82528e1abb', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 91, 'removed': False}), AttributeDict({'address': '0x602b873E953CFCd7B5AE77E450E6c5A4C4decF1f', 'topics': [HexBytes('0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4'), HexBytes('0x000000000000000000000000aba7e39111630342f720e44e6517240b67351e4c')], 'data': '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000025f80a60a6cc880000000000000000000000000000000000000000000000000204bd958e1951500000000000000000000000000000000000000000000000000000000000000000', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 92, 'removed': False}), AttributeDict({'address': '0x15104336cf1C5BB4281eD1E12fecc5A1197e5E36', 'topics': [HexBytes('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'), HexBytes('0x000000000000000000000000fc0e59008d817fd57d90a7b1bab6ffb92cbadb07'), HexBytes('0x0000000000000000000000009625a4f2f6bec1b507e6d112ba5073e70f6ed3d9')], 'data': '0x000000000000000000000000000000000000000001bead72a838453f9c000000', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 93, 'removed': False}), AttributeDict({'address': '0x15104336cf1C5BB4281eD1E12fecc5A1197e5E36', 'topics': [HexBytes('0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'), HexBytes('0x000000000000000000000000fc0e59008d817fd57d90a7b1bab6ffb92cbadb07'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4')], 'data': '0xfffffffffffffffffffffffffffffffffffffffffe0fb10ed34fb30ea7ffffff', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 94, 'removed': False}), AttributeDict({'address': '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c', 'topics': [HexBytes('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'), HexBytes('0x0000000000000000000000009625a4f2f6bec1b507e6d112ba5073e70f6ed3d9'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4')], 'data': '0x00000000000000000000000000000000000000000000000002a6a4c4a79768b6', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 95, 'removed': False}), AttributeDict({'address': '0x9625A4F2F6BEc1b507E6d112bA5073E70f6ed3d9', 'topics': [HexBytes('0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1')], 'data': '0x0000000000000000000000000000000000000000804a059573a389dc11cee2fc000000000000000000000000000000000000000000000000c0d6d0a5d24d5aca', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 96, 'removed': False}), AttributeDict({'address': '0x9625A4F2F6BEc1b507E6d112bA5073E70f6ed3d9', 'topics': [HexBytes('0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4')], 'data': '0x000000000000000000000000000000000000000001bead72a838453f9c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002a6a4c4a79768b6', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 97, 'removed': False}), AttributeDict({'address': '0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c', 'topics': [HexBytes('0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65'), HexBytes('0x000000000000000000000000cd3d4eb34385a2ddf470aed617378eaae53082d4')], 'data': '0x00000000000000000000000000000000000000000000000002a6a4c4a79768b6', 'blockNumber': 15734117, 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'blockHash': HexBytes('0x09d18b1f71b6e8031d9df14f2aff4ca6671b8121b80dba730c2400c488f5f4a3'), 'logIndex': 98, 'removed': False})], 'logsBloom': HexBytes('0x00201000000000000000000088000000000000020000000000000000000000040008000000000000000000000000000000080000010000200200000000200000000000000000000000000008000000200000000000400000009400008000000000000100000000000000000040000000000000000000040000000010000000002000000001004000400000800000000000040001000000080000004000012000020000000000000000000000000000000000000000000000000000002040000000000026000000000000000000000000000000000000041000000002000280000010000000000000000000000000000000000000000000c40000040000000000'), 'status': 1, 'to': '0xcd3d4Eb34385A2DDF470aeD617378EAae53082D4', 'transactionHash': HexBytes('0x105e3130bf0027eceeeabaf52db3f63f4a08f7b4da4718c5326f26b56a1f97a4'), 'transactionIndex': 30, 'type': '0x0'})