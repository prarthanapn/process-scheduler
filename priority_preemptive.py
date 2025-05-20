def calculate_priority_p_data(arrival_times, burst_times, priorities):
    n = len(arrival_times)
    remaining_bt = burst_times[:]
    finish_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    complete = 0
    current_time = 0

    while complete < n:
        idx = -1
        highest_priority = float('inf')
        for i in range(n):
            if arrival_times[i] <= current_time and remaining_bt[i] > 0:
                if priorities[i] < highest_priority:
                    highest_priority = priorities[i]
                    idx = i
                elif priorities[i] == highest_priority:
                    # Tie breaker: earlier arrival
                    if arrival_times[i] < arrival_times[idx]:
                        idx = i

        if idx == -1:
            current_time += 1
            continue

        # Execute process for 1 unit
        remaining_bt[idx] -= 1
        current_time += 1

        if remaining_bt[idx] == 0:
            complete += 1
            finish_time[idx] = current_time
            turnaround_time[idx] = finish_time[idx] - arrival_times[idx]
            waiting_time[idx] = turnaround_time[idx] - burst_times[idx]

    avg_tat = sum(turnaround_time) / n
    avg_wt = sum(waiting_time) / n

    results = []
    for i in range(n):
        results.append({
            'Job': chr(ord('A') + i),
            'Arrival Time': arrival_times[i],
            'Burst Time': burst_times[i],
            'Priority': priorities[i],
            'Finish Time': finish_time[i],
            'Turnaround Time': turnaround_time[i],
            'Waiting Time': waiting_time[i]
        })

    return {
        'job_details': results,
        'average_turnaround_time': avg_tat,
        'average_waiting_time': avg_wt
    }
