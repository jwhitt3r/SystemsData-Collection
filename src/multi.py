import psutil
import matplotlib.pyplot as plt
import time

"""
multi.py monitors two processes specified within pid1 and pid2, to show systems usage (CPU, Real Memory, and Virtual Memory) 
usage over a period of time. The collected data is then visualised onto a graph via matplotlib and saved as plot.png
"""

start_time = time.time()

pid1 = int(8914) # Place the process you want to monitor, e.g., 8914
pid2 = int(9662) # Place the process you want to monitor, e.g., 8914
process1 = psutil.Process(pid1)
process2 = psutil.Process(pid2)
duration = 61 # Define how long you would like to capture the data for, in this case a minute.
log1 = {'cpu': [], 'times': [], 'memory' : [], 'virtual' : []}
log2 = {'cpu': [], 'times': [], 'memory' : [], 'virtual' : []}


"""
Capture the data for the processes
"""

while True:
    current_time = time.time()

    process1_current_cpu = process1.cpu_percent(interval=1)
    process1_current_mem = process1.memory_info()
    process1_current_mem_real = process1_current_mem.rss / 1024. ** 2
    process1_current_mem_virtual = process1_current_mem.vms / 1024. ** 2

    process2_current_cpu = process2.cpu_percent(interval=1)
    process2_current_mem = process2.memory_info()
    process2_current_mem_real = process2_current_mem.rss / 1024. ** 2
    process2_current_mem_virtual = process2_current_mem.vms / 1024. ** 2

    """
    For the duration of the test, append data to the dictionary.
    """

    if current_time - start_time < duration:
        
        log1['times'].append(current_time-start_time)
        log1['cpu'].append(process1_current_cpu)
        log1['memory'].append(process1_current_mem_real)
        log1['virtual'].append(process1_current_mem_virtual)

        log2['times'].append(current_time-start_time)
        log2['cpu'].append(process2_current_cpu)
        log2['memory'].append(process2_current_mem_real)
        log2['virtual'].append(process2_current_mem_virtual)
    else:
        break

fig = plt.figure(figsize=(10,5))

"""
Define the structure of the plot for process 1.
"""

p1_ax1 = fig.add_subplot(2,1,1)
p1_ax1.title.set_text('CPU Usage and Real Memory Usage over a ' + str(duration-1) + ' second duration \n for the Process: ' + process1.name())
p1_ax1.plot(log1['times'], log1['cpu'], '-', lw=1, color='r')
p1_ax1.set_ylabel('CPU (%)', color='r')
p1_ax1.set_xlabel('Time (s)')
p1_ax1.set_ylim(0.0, max(log1['cpu'])* 1.2)

p1_ax2 = p1_ax1.twinx()
p1_ax2.plot(log1['times'], log1['memory'], '-', lw=1, color='b')
p1_ax2.set_ylabel('Real Memory (MB)', color='b')
p1_ax2.set_ylim(0.0, max(log1['memory'])* 1.2)
p1_ax2.grid()

"""
Define the structure of the plot for process 2.
"""

p2_ax1 = fig.add_subplot(2,1,2)
p2_ax1.title.set_text('CPU Usage and Real Memory Usage over a ' + str(duration-1) + ' second duration \n for the Process: ' + process2.name())
p2_ax1.plot(log2['times'], log2['cpu'], '-', lw=1, color='r')
p2_ax1.set_ylabel('CPU (%)', color='r')
p2_ax1.set_ylim(0.0, max(log2['cpu'])* 1.2)
p2_ax1.set_xlabel('Time (s)')
p2_ax2 = p2_ax1.twinx()
p2_ax2.plot(log2['times'], log2['memory'], '-', lw=1, color='b')
p2_ax2.set_ylabel('Real Memory (MB)', color='b')
p2_ax2.set_ylim(0.0, max(log2['memory'])* 1.2)
p2_ax2.grid()

"""
Output and save the figure combining both process 1 and process 2's data.
"""

plt.tight_layout()
plt.savefig('plot.png', dpi=600)
