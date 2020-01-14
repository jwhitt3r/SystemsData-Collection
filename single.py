import psutil
import matplotlib.pyplot as plt
import time

start_time = time.time()

pid1 = int(8914)
process1 = psutil.Process(pid1)
duration = 5
log1 = {'cpu': [], 'times': [], 'memory' : [], 'virtual' : []}
while True:
    current_time = time.time()
    process1_current_cpu = process1.cpu_percent(interval=1)
    process1_current_mem = process1.memory_info()
    process1_current_mem_real = process1_current_mem.rss / 1024. ** 2
    process1_current_mem_virtual = process1_current_mem.vms / 1024. ** 2


    if current_time - start_time < duration:
        log1['times'].append(current_time-start_time)
        log1['cpu'].append(process1_current_cpu)
        log1['memory'].append(process1_current_mem_real)
        log1['virtual'].append(process1_current_mem_virtual)

    else:
        break



fig = plt.figure(figsize=(10,5))

p1_ax1 = fig.add_subplot(2,1,1)
p1_ax1.plot(log1['times'], log1['cpu'], '-', lw=1, color='r')
p1_ax1.set_ylabel('CPU (%)', color='r')
p1_ax1.set_xlabel('Time (s)')
p1_ax1.set_ylim(0.0, max(log1['cpu'])* 1.2)

p1_ax2 = p1_ax1.twinx()
p1_ax2.plot(log1['times'], log1['memory'], '-', lw=1, color='b')
p1_ax2.set_ylabel('Real Memory (MB)', color='b')
p1_ax2.set_ylim(0.0, max(log1['memory'])* 1.2)
p1_ax2.grid()

plt.tight_layout()
plt.savefig('plot.png', dpi=600)
