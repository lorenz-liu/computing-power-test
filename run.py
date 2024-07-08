import multiprocessing
import time

import numpy as np


# Function to perform a heavy computation
def heavy_computation(n):
    x = np.random.rand(n, n)
    y = np.random.rand(n, n)
    result = np.dot(x, y)
    return result


# Function to measure single-threaded computation power
def measure_single_threaded_power():
    start_time = time.time()
    heavy_computation(500)
    end_time = time.time()
    return end_time - start_time


# Function to measure multi-threaded (parallel) computation power
def measure_multi_threaded_power():
    start_time = time.time()
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    pool.map(heavy_computation, [500] * multiprocessing.cpu_count())
    pool.close()
    pool.join()
    end_time = time.time()
    return end_time - start_time


# Calculate the computing power score
def calculate_score(single_threaded_time, multi_threaded_time):
    # Normalize the scores
    single_threaded_score = max(1, 50 / single_threaded_time)
    multi_threaded_score = max(1, 50 / multi_threaded_time)
    total_score = single_threaded_score + multi_threaded_score
    return min(total_score, 100)  # Cap the score at 100


# Main function
if __name__ == "__main__":
    print("Measuring single-threaded computation power...")
    single_threaded_time = measure_single_threaded_power()
    print(f"Single-threaded computation time: {single_threaded_time:.2f} seconds")

    print("Measuring multi-threaded computation power...")
    multi_threaded_time = measure_multi_threaded_power()
    print(f"Multi-threaded computation time: {multi_threaded_time:.2f} seconds")

    score = calculate_score(single_threaded_time, multi_threaded_time)
    print(f"Computing Power: {score:.2f} out of 100")
