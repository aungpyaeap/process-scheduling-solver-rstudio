import numpy as np
from tabulate import tabulate

ARRIVALS = np.array([0, 3, 4, 8, 12])
BURST = np.array([15, 2, 6, 2, 10])
Q = 2

n = len(ARRIVALS)
processes = [f'P{i+1}' for i in range(n)]

# Initialize arrays
remaining = BURST.copy()
start_time = [-1] * n
completion_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n

# Ready queue and step tracking
ready_queue = []
time = 0
completed = 0
step_allocation = []

# Sort processes by arrival time for initial queue
process_order = sorted(range(n), key=lambda i: ARRIVALS[i])

# Add first process to ready queue
idx = 0
while idx < n and ARRIVALS[process_order[idx]] <= time:
    ready_queue.append(process_order[idx])
    idx += 1

# Round Robin scheduling
while completed < n:
    if not ready_queue:
        # No process ready, jump to next arrival
        if idx < n:
            time = ARRIVALS[process_order[idx]]
            while idx < n and ARRIVALS[process_order[idx]] <= time:
                ready_queue.append(process_order[idx])
                idx += 1
        continue
    
    # Get next process from queue
    current = ready_queue.pop(0)
    
    # Set start time if first time
    if start_time[current] == -1:
        start_time[current] = time
    
    # Execute for Q or remaining time
    if remaining[current] <= Q:
        # Process will complete
        step_allocation.append([processes[current], time, time + remaining[current], remaining[current], 0])
        time += remaining[current]
        remaining[current] = 0
        completion_time[current] = time
        completed += 1
        
        # Add newly arrived processes to queue
        while idx < n and ARRIVALS[process_order[idx]] <= time:
            ready_queue.append(process_order[idx])
            idx += 1
    else:
        # Process will use full quantum
        step_allocation.append([processes[current], time, time + Q, Q, remaining[current] - Q])
        time += Q
        remaining[current] -= Q
        
        # Add newly arrived processes to queue
        while idx < n and ARRIVALS[process_order[idx]] <= time:
            ready_queue.append(process_order[idx])
            idx += 1
        
        # Add current process back to queue
        ready_queue.append(current)

# Calculate waiting and turnaround times
for i in range(n):
    turnaround_time[i] = completion_time[i] - ARRIVALS[i]
    waiting_time[i] = turnaround_time[i] - BURST[i]

# Prepare results table
RESULTS = []
for i in range(n):
    RESULTS.append([
        processes[i],
        ARRIVALS[i],
        BURST[i],
        start_time[i],
        completion_time[i],
        waiting_time[i],
        turnaround_time[i]
    ])

headers = ['P', 'AT', 'BT', 'ST', 'CT', 'WT', 'TT']
print(tabulate(RESULTS, headers=headers, tablefmt='grid'))

# Calculate and print averages
avg_waiting = np.mean(waiting_time)
avg_turnaround = np.mean(turnaround_time)
print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")

# Print allocation table
print("\nAllocation:")
step_headers = ['PROCESS', 'START', 'END', 'Q', 'LEFT']
print(tabulate(step_allocation, headers=step_headers, tablefmt='grid'))