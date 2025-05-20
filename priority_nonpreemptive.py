def calculate_priority_np_data(arrival_times, burst_times, priorities):
    """
    Non-Preemptive Priority Scheduling

    Args:
        arrival_times (list): Arrival times of processes
        burst_times (list): Burst times of processes
        priorities (list): Priorities of processes (lower number = higher priority)

    Returns:
        dict: job details with Completion Time, Turnaround Time, Waiting Time,
              plus average turnaround and waiting times
    """
    n = len(arrival_times)
    processes = list(range(n))
    completed = [False] * n
    current_time = 0
    completed_count = 0

    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    while completed_count < n:
        # Select process with highest priority among arrived and not completed
        eligible = [i for i in range(n) if (arrival_times[i] <= current_time and not completed[i])]
        if not eligible:
            current_time += 1
            continue
        # Process with lowest priority number
        idx = min(eligible, key=lambda x: priorities[x])

        # Execute process
        start_time = current_time
        current_time += burst_times[idx]
        completion_time[idx] = current_time
        turnaround_time[idx] = completion_time[idx] - arrival_times[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_times[idx]
        completed[idx] = True
        completed_count += 1

    results = []
    for i in range(n):
        results.append({
            'Job': chr(ord('A') + i),
            'Arrival Time': arrival_times[i],
            'Burst Time': burst_times[i],
            'Priority': priorities[i],
            'Completion Time': completion_time[i],
            'Turnaround Time': turnaround_time[i],
            'Waiting Time': waiting_time[i]
        })

    average_tat = sum(turnaround_time) / n
    average_wt = sum(waiting_time) / n

    return {
        'job_details': results,
        'average_turnaround_time': average_tat,
        'average_waiting_time': average_wt
    }
