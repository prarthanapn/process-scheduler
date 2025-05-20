from collections import deque

def calculate_rr_data(arrival_times, burst_times, quantum):
    n = len(arrival_times)
    remaining_bt = burst_times[:]
    finish_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    time = 0
    queue = deque()
    visited = [False] * n
    completed = 0

    # Enqueue processes that arrive at time 0
    for i in range(n):
        if arrival_times[i] == 0:
            queue.append(i)
            visited[i] = True

    while completed < n:
        if not queue:
            # If queue empty, jump to next arriving process
            time = min([arrival_times[i] for i in range(n) if not visited[i]])
            for i in range(n):
                if arrival_times[i] == time and not visited[i]:
                    queue.append(i)
                    visited[i] = True

        current = queue.popleft()

        exec_time = min(quantum, remaining_bt[current])
        remaining_bt[current] -= exec_time
        time += exec_time

        # Enqueue newly arrived processes during execution
        for i in range(n):
            if (arrival_times[i] <= time and not visited[i]):
                queue.append(i)
                visited[i] = True

        if remaining_bt[current] == 0:
            completed += 1
            finish_time[current] = time
            turnaround_time[current] = finish_time[current] - arrival_times[current]
            waiting_time[current] = turnaround_time[current] - burst_times[current]
        else:
            queue.append(current)

    avg_tat = sum(turnaround_time) / n
    avg_wt = sum(waiting_time) / n

    results = []
    for i in range(n):
        results.append({
            'Job': chr(ord('A') + i),
            'Arrival Time': arrival_times[i],
            'Burst Time': burst_times[i],
            'Finish Time': finish_time[i],
            'Turnaround Time': turnaround_time[i],
            'Waiting Time': waiting_time[i]
        })

    return {
        'job_details': results,
        'average_turnaround_time': avg_tat,
        'average_waiting_time': avg_wt
    }
