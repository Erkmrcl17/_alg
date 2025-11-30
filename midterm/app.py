from blockchain import Blockchain, Block
import time

my_coin = Blockchain(difficulty=3)

print("Mining block 1...")
my_coin.add_block(Block(1, time.time(), {"amount": 100}))

print("Mining block 2...")
my_coin.add_block(Block(2, time.time(), {"amount": 50}))

for block in my_coin.chain:
    print(f"Index: {block.index}, Hash: {block.hash}, Data: {block.data}")

print("Is blockchain valid?", my_coin.is_chain_valid())