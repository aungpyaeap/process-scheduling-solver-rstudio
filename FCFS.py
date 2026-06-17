import numpy as np
from tabulate import tabulate

ARRIVALS = np.array([0, 3, 4, 8, 12])
BURST = np.array([15, 2, 6, 2, 10])

# Number of processes
n = len(ARRIVALS)

# Initialize arrays for results
PROCESSES = [f'P{i+1}' for i in range(n)]
START_TIME = np.zeros(n, dtype=int)
COMPLETION_TIME = np.zeros(n, dtype=int)
WAITING_TIME = np.zeros(n, dtype=int)
TURNAROUND_TIME = np.zeros(n, dtype=int)

# Calculate FCFS scheduling
current_time = 0

for i in range(n):
    # Start time is max of current time and arrival time
    START_TIME[i] = max(current_time, ARRIVALS[i])
    
    # Completion time = start time + burst time
    COMPLETION_TIME[i] = START_TIME[i] + BURST[i]
    
    # Turnaround time = completion time - arrival time
    TURNAROUND_TIME[i] = COMPLETION_TIME[i] - ARRIVALS[i]
    
    # Waiting time = turnaround time - burst time
    WAITING_TIME[i] = TURNAROUND_TIME[i] - BURST[i]
    
    # Update current time to completion time
    current_time = COMPLETION_TIME[i]

# Prepare results table
RESULTS = []
for i in range(n):
    RESULTS.append([
        PROCESSES[i],
        ARRIVALS[i],
        BURST[i],
        START_TIME[i],
        COMPLETION_TIME[i],
        WAITING_TIME[i],
        TURNAROUND_TIME[i]
    ])

# Print the table
headers = ['P', 'AT', 'BT', 'ST', 'CT', 'WT', 'TT']
print(tabulate(RESULTS, headers=headers, tablefmt='grid'))

# Calculate and print averages
avg_waiting = np.mean(WAITING_TIME)
avg_turnaround = np.mean(TURNAROUND_TIME)

print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")