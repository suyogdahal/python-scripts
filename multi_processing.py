import multiprocessing
import time

NUM_CORES = 8
LEN_LIST = 10_000_000 # 10 million ;)

def calculate_large_sum(numbers):
    # simulating a long-running task
    return sum(n**2 for n in numbers)

# create a large list of numbers
numbers = list(range(LEN_LIST))

# record the start time
start_time = time.time()

# Using list comprehension
result = sum(n**2 for n in numbers)

# record the end time
end_time = time.time()

# print the time taken to complete the task
print(f"Time taken to complete the task using list comprehension: {end_time - start_time}")

# create a multiprocessing pool with NUM_CORES worker processes
pool = multiprocessing.Pool(processes=NUM_CORES)

# record the start time
start_time = time.time()

# map the calculate_large_sum function to the numbers list
# the function will be applied to each element of the list in parallel
result = pool.map(calculate_large_sum, [numbers[i::NUM_CORES] for i in range(NUM_CORES)])

# record the end time
end_time = time.time()

# print the time taken to complete the task
print(f"Time taken to complete the task using multiprocessing: {end_time - start_time}")
