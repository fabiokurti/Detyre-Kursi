from simple_blockchain import block, block_1, block_2, generate_block_hash

def validate_blockchain(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]
        if current_block.previous_block_hash != previous_block.block_hash:
            return False
        if current_block.block_hash != generate_block_hash(current_block.block_id, current_block.previous_block_hash, current_block.timestamp, current_block.content):
            return False
    return True

blockchain = [block, block_1, block_2]
print(f"Is the blockchain valid? {validate_blockchain(blockchain)}")

print(f"Block Hash: {block.block_hash}")
print(f"Block 1 Hash: {block_1.block_hash}")
print(f"Block 2 Hash: {block_2.block_hash}")