def calculate_sjf_data(arrival_times, burst_times):
    n = len(arrival_times)
    completed = [False] * n
    current_time = 0
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    completed_count = 0

    while completed_count < n:
        # find process with shortest burst that arrived <= current_time and not completed
        idx = -1
        min_burst = float('inf')
        for i in range(n):
            if arrival_times[i] <= current_time and not completed[i]:
                if burst_times[i] < min_burst:
                    min_burst = burst_times[i]
                    idx = i
        if idx == -1:
            current_time += 1  # no process ready, advance time
            continue
        current_time += burst_times[idx]
        finish_time[idx] = current_time
        turnaround_time[idx] = finish_time[idx] - arrival_times[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_times[idx]
        completed[idx] = True
        completed_count += 1

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
