import argparse
import multiprocessing
import random

def estimate_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return inside_circle

def main():
    parser = argparse.ArgumentParser(description="Estimate the value of 'pi' using Monte Carlo method with parallel processing.")
    parser.add_argument("num_points", type=int, help="Number of random points to generate")
    args = parser.parse_args()

    num_processes = multiprocessing.cpu_count()  # Number of available CPU cores
    points_per_process = args.num_points // num_processes

    pool = multiprocessing.Pool(processes=num_processes)
    
    results = pool.map(estimate_pi, [points_per_process] * num_processes)

    total_inside_circle = sum(results)
    estimated_pi = 4 * (total_inside_circle / args.num_points)

    print(f"Estimated value of 'pi' using {args.num_points} points: {estimated_pi}")

if __name__ == "__main__":
    main()