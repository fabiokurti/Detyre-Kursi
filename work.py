from simple_blockchain import block_2, generate_block_hash
import time

def mine_block(block, difficulty):
 
    prefix = '0' * difficulty  # Define the prefix based on difficulty
    start_time = time.time()   # Track the start time for performance measurement
    
    print(f"Mining block {block.block_id} with difficulty {difficulty}...")
    
    while not block.block_hash.startswith(prefix):
        block.timestamp += 1  # Increment the timestamp to change the hash
        block.block_hash = generate_block_hash(
            block.block_id,
            block.previous_block_hash,
            block.timestamp,
            block.content
        )
    
    end_time = time.time()  # Track the end time
    print(f"Block mined successfully in {end_time - start_time:.2f} seconds!")
    return block

# Set the mining difficulty
difficulty = 4

# Mine the block
mined_block = mine_block(block_2, difficulty)

# Print the mined block's hash
print(f"Mined block hash: {mined_block.block_hash}")