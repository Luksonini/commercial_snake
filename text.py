import time

start_time = time.time()
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time > 5:
        start_time = time.time()
        print("the time passed")

# your code


