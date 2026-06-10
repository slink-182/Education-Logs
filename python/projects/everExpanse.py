import time

n = 1

# How long to run (seconds)
run_time = 60

# How fast to expand (seconds between doublings)
delay = 1

start = time.time()

while time.time() - start < run_time:
    n *= 2
    print(n)
    time.sleep(delay)

print("Stopped after 1 minute.")