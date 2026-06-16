# Process Scheduling Solver

Pyton and R code for classic CPU scheduling algorithms to compute Average Waiting Time (WT) and Average Turnaround Time (TT).

## Algorithms in repository
- **`FCFS.R`** **`FCFS.py`**: First Come First Serve / FCFS
- **`SJF.R`** **`SJF.py`**: Shortest Job First / SJF (non-preemptive)
- **`PREEMPTIVE-PRIORITY.R.R`** **`PP.py`**: Preemptive Priority
- **`ROUND-ROBIN.R`** **`RR.py`**: Round-Robin / RR

## Equations
$$\text{Start Time with different arrival time}=\max(\underbrace{ST + EXT}_{\text{previous}(i-1)} , \underbrace{AT}_{\text{current}(i)})$$

$\text{Completion Time}=\text{Start Time}+\text{Execution Time}$

$\text{Waiting Time}=\text{Start Time}+\text{Arrival Time}$

$\text{Turnaround Time}=\text{Completion Time}+\text{Arrival Time}$

$\text{Remaining Execution Time}= \text{Execution Time}(a) – (\text{Start Time}(b) – \text{Start Time}(a))$

Note that counting starts from remaining blocks.

Use
$\text{Waiting Time} = (\text{Completion Time} – \text{Arrival Time}) – \text{Execution Time}$

for a process with prevented blocks. Applicable for Preemptive Priority and Round-Robin.

$\text{Average Waiting Time} \quad WT = \frac{1}{n} \sum_{i=1}^n WT_i, \quad i=1,2,\cdots,n$

$\text{Average Turnaround Time} \quad TT = \frac{1}{n} \sum_{i=1}^n TT_i, \quad i=1,2,\cdots,n$

![Visualisation of process scheduling](scheduling.png "Visualisation of process scheduling")