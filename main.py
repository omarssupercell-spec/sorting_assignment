import random
import time
import sys
import matplotlib.pyplot as plt
sys.setrecursionlimit(100000)



#BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

#QUICK SORT
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1] #use last index of array as the pivot

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

#TESTING

small = random.sample(range(1, 10_000), 100)
medium = random.sample(range(1, 100_000), 1_000)
large = random.sample(range(1, 1_000_000), 5_000)

sets = [
    ("Small  (100 elements)", small),
    ("Medium  (1000 elements)", medium),
    ("Large  (10000 elements)", large),
]

NUM_TRIALS = 5

for label, number in sets:

#bubble sort
    total = 0
    for _ in range(NUM_TRIALS):
        copy = number.copy()
        start = time.perf_counter()
        bubble_sort(copy)
        end = time.perf_counter()
        total += end - start
    avg = total / NUM_TRIALS
    print(f"{'Bubble Sort':<20} {label:<25} {avg:.6f}")

#quick sort
    total = 0
    for _ in range(NUM_TRIALS):
        copy = number.copy()
        start = time.perf_counter()
        quick_sort(copy)
        end = time.perf_counter()
        total += end - start
    avg = total / NUM_TRIALS
    print(f"{'Quick Sort':<20} {label:<25} {avg:.6f}")

    print("-" * 55)




# GRAPH CODE (AI HELP FOR THE ACTUAL GRAPH AND PNG)

sizes = [100, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 4000, 5000]

bubble_times = []
quick_times = []

print("\nRunning graph tets...")

for size in sizes:
    data = random.sample(range(1, 1_000_000), size)

    #bubble sort timing
    total = 0
    for _ in range(NUM_TRIALS):
        copy = data.copy()
        start = time.perf_counter()
        bubble_sort(copy)
        end = time.perf_counter()
        total += end - start
    bubble_times.append(total / NUM_TRIALS)

    #quick sort timing
    total = 0
    for _ in range(NUM_TRIALS):
        copy = data.copy()
        start = time.perf_counter()
        quick_sort(copy)
        end = time.perf_counter()
        total += end - start
    quick_times.append(total / NUM_TRIALS)

    print (f"Done: {size} elements")

#plot results on graph( AI HELP)
plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort', color='red')
plt.plot(sizes, quick_times, marker='o', label='Quick Sort', color='blue')

plt.title("Bubble Sort vs Quick Sort - Time Complexity")
plt.xlabel("Dataset size (elements)")
plt.ylabel("Average Time (seconds)")
plt.legend()
plt.grid(True)

plt.savefig("sorting_results.png")
plt.show()

print("\nGraph saved as sorting_results.png")


















