import numpy as np
from tabulate import tabulate

ARRIVALS = np.array([0, 3, 4, 8, 12])
BURST = np.array([15, 2, 6, 2, 10])
PRIORITY = np.array([5, 1, 3, 4, 2])

# Number of processes
n = len(ARRIVALS)

# Create process list with all details
processes = []
for i in range(n):
    processes.append({
        'id': f'P{i+1}',
        'arrival': ARRIVALS[i],
        'burst': BURST[i],
        'priority': PRIORITY[i],
        'remaining': BURST[i],  # Remaining burst time for preemptive scheduling
        'start': None,
        'completion': None,
        'waiting': None,
        'turnaround': None
    })

# Preemptive Priority Scheduling (Lower priority number = higher priority)
time = 0
completed = 0
ready_queue = []

while completed < n:
    # Add arrived processes to ready queue
    for p in processes:
        if p['arrival'] <= time and p['remaining'] > 0 and p not in ready_queue:
            ready_queue.append(p)
    
    # If ready queue is empty, jump to next arrival
    if not ready_queue:
        time += 1
        continue
    
    # Select process with highest priority (lowest priority number)
    # If tie, select the one that arrived earlier
    current = min(ready_queue, key=lambda x: (x['priority'], x['arrival']))
    
    # If this is the first time the process is executing, set start time
    if current['start'] is None:
        current['start'] = time
    
    # Execute for 1 unit of time (preemptive)
    current['remaining'] -= 1
    time += 1
    
    # If process is completed
    if current['remaining'] == 0:
        current['completion'] = time
        current['turnaround'] = current['completion'] - current['arrival']
        current['waiting'] = current['turnaround'] - current['burst']
        ready_queue.remove(current)
        completed += 1

# Prepare results table
RESULTS = []
for p in processes:
    RESULTS.append([
        p['id'],
        p['arrival'],
        p['burst'],
        p['priority'],
        p['start'],
        p['completion'],
        p['waiting'],
        p['turnaround']
    ])

headers = ['P', 'AT', 'BT', 'P*', 'ST', 'CT', 'WT', 'TT']
print(tabulate(RESULTS, headers=headers, tablefmt='grid'))

# Calculate and print averages
avg_waiting = sum(p['waiting'] for p in processes) / n
avg_turnaround = sum(p['turnaround'] for p in processes) / n

print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")