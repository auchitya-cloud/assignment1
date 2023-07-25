import time
import matplotlib.pyplot as plt

def sort_list_time(elements):
    # Generate a list with random elements (for simplicity, we use a range of integers)
    data_list = list(range(elements))

    # Record start time
    start_time = time.time()

    # Sort the list
    sorted_list = sorted(data_list)

    # Record end time and calculate time taken
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken

# Number of elements in the list
elements_list = [5000, 10000, 15000, 20000, 25000]

# Measure the time taken for each list size
time_taken_list = []
for elements in elements_list:
    time_taken_list.append(sort_list_time(elements))

# Plot the graph
plt.plot(elements_list, time_taken_list, marker='o')
plt.xlabel('Number of Elements in the List')
plt.ylabel('Time Taken (seconds)')
plt.title('Sorting Time vs. List Size')
plt.grid(True)
plt.show()
