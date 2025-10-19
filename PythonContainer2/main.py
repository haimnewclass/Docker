import time
import random
from datetime import datetime

log_path = "output.log"

for i in range(1, 6):  # Loop 5 times
    rand_num = random.randint(1000, 9999)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"Loop iteration: {i} | Random: {rand_num} | Time: {timestamp}"
    
    # Print to console
    print(message, flush=True)
    
    # Append to log file
    with open(log_path, "a") as f:
        f.write(message + "\n")
    
    time.sleep(1)

# Script completed
print("Script completed!", flush=True)
