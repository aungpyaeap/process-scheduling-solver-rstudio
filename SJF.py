import numpy as np
from tabulate import tabulate

ARRIVALS = np.array([0, 3, 4, 8, 12])
BURST = np.array([15, 2, 6, 2, 10])

n = len(ARRIVALS)
PROCESSES = [f'P{i+1}' for i in range(n)]

# Initialize arrays
START_TIME = np.zeros(n, dtype=int)
COMPLETION_TIME = np.zeros(n, dtype=int)
WAITING_TIME = np.zeros(n, dtype=int)
TURNAROUND_TIME = np.zeros(n, dtype=int)
completed = np.zeros(n, dtype=bool)

current_time = 0
completed_count = 0

while completed_count < n:
    # Find shortest job among arrived processes
    min_burst = float('inf')
    selected = -1
    
    for i in range(n):
        if not completed[i] and ARRIVALS[i] <= current_time:
            if BURST[i] < min_burst:
                min_burst = BURST[i]
                selected = i
            elif BURST[i] == min_burst and ARRIVALS[i] < ARRIVALS[selected]:
                selected = i
    
    # If no process available, jump to next arrival
    if selected == -1:
        current_time = min(ARRIVALS[~completed])
        continue
    
    # Execute selected process
    START_TIME[selected] = current_time
    COMPLETION_TIME[selected] = current_time + BURST[selected]
    TURNAROUND_TIME[selected] = COMPLETION_TIME[selected] - ARRIVALS[selected]
    WAITING_TIME[selected] = TURNAROUND_TIME[selected] - BURST[selected]
    
    current_time = COMPLETION_TIME[selected]
    completed[selected] = True
    completed_count += 1

# Prepare and display results
RESULTS = []
for i in range(n):
    RESULTS.append([PROCESSES[i], ARRIVALS[i], BURST[i], 
                    START_TIME[i], COMPLETION_TIME[i], 
                    WAITING_TIME[i], TURNAROUND_TIME[i]])

headers = ['P', 'AT', 'BT', 'ST', 'CT', 'WT', 'TT']
print(tabulate(RESULTS, headers=headers, tablefmt='grid'))

avg_waiting = np.mean(WAITING_TIME)
avg_turnaround = np.mean(TURNAROUND_TIME)

print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")