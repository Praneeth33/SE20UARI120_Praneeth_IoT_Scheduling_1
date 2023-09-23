def first_come_first_serve(processes, burst_times, arrival_times):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = max(0, waiting_time[i - 1] + burst_times[i - 1] - arrival_times[i])

    for i in range(n):
        turnaround_time[i] = burst_times[i] + waiting_time[i]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time

def shortest_job_first(processes, burst_times, arrival_times):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    burst_remaining = burst_times.copy()
    total_time = 0

    while True:
        min_burst = float('inf')
        shortest = -1
        for i in range(n):
            if arrival_times[i] <= total_time and burst_remaining[i] > 0 and burst_remaining[i] < min_burst:
                min_burst = burst_remaining[i]
                shortest = i

        if shortest == -1:
            total_time += 1
        else:
            waiting_time[shortest] = max(0, total_time - arrival_times[shortest])
            total_time += burst_remaining[shortest]
            burst_remaining[shortest] = 0

        if sum(burst_remaining) == 0:
            break

    for i in range(n):
        turnaround_time[i] = burst_times[i] + waiting_time[i]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time

def round_robin(processes, burst_times, arrival_times, quantum):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    remaining_burst = burst_times.copy()
    time = 0

    while True:
        done = True
        for i in range(n):
            if arrival_times[i] <= time and remaining_burst[i] > 0:
                done = False
                if remaining_burst[i] > quantum:
                    time += quantum
                    remaining_burst[i] -= quantum
                else:
                    time += remaining_burst[i]
                    waiting_time[i] = max(0, time - arrival_times[i] - burst_times[i])
                    remaining_burst[i] = 0

        if done:
            break

    for i in range(n):
        turnaround_time[i] = burst_times[i] + waiting_time[i]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time

def priority_scheduling(processes, burst_times, arrival_times, priorities):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if priorities[i] > priorities[j]:
                processes[i], processes[j] = processes[j], processes[i]
                burst_times[i], burst_times[j] = burst_times[j], burst_times[i]
                arrival_times[i], arrival_times[j] = arrival_times[j], arrival_times[i]
                priorities[i], priorities[j] = priorities[j], priorities[i]

    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = max(0, waiting_time[i - 1] + burst_times[i - 1] - arrival_times[i])

    for i in range(n):
        turnaround_time[i] = burst_times[i] + waiting_time[i]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time

processes = [1, 2, 3, 4]
burst_times = [24, 3, 3, 12]
arrival_times = [0, 4, 5, 6]
priorities = [3, 1, 4, 2]
quantum = 2

avg_waiting_fcfs, avg_turnaround_fcfs = first_come_first_serve(processes, burst_times, arrival_times)
avg_waiting_sjf, avg_turnaround_sjf = shortest_job_first(processes, burst_times, arrival_times)
avg_waiting_rr, avg_turnaround_rr = round_robin(processes, burst_times, arrival_times, quantum)
avg_waiting_priority, avg_turnaround_priority = priority_scheduling(processes, burst_times, arrival_times, priorities)

print("First Come First Serve:")
print("Average Waiting Time:", avg_waiting_fcfs)
print("Average Turnaround Time:", avg_turnaround_fcfs)

print("\nShortest Job First:")
print("Average Waiting Time:", avg_waiting_sjf)
print("Average Turnaround Time:", avg_turnaround_sjf)

print("\nRound Robin:")
print("Average Waiting Time:", avg_waiting_rr)
print("Average Turnaround Time:", avg_turnaround_rr)

print("\nPriority Scheduling:")
print("Average Waiting Time:", avg_waiting_priority)
print("Average Turnaround Time:", avg_turnaround_priority)
