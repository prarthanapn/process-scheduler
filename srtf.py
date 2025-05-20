def calculate_srtf_data(arrival_times, burst_times):
    n = len(arrival_times)
    remaining_bt = burst_times[:]
    complete = 0
    current_time = 0
    min_bt = float('inf')
    shortest = -1
    finish_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    check = False

    while complete != n:
        min_bt = float('inf')
        shortest = -1
        check = False

        for i in range(n):
            if (arrival_times[i] <= current_time and
                remaining_bt[i] < min_bt and remaining_bt[i] > 0):
                min_bt = remaining_bt[i]
                shortest = i
                check = True

        if not check:
            current_time += 1
            continue

        # Execute process for 1 unit of time
        remaining_bt[shortest] -= 1
        current_time += 1

        if remaining_bt[shortest] == 0:
            complete += 1
            finish_time[shortest] = current_time
            turnaround_time[shortest] = finish_time[shortest] - arrival_times[shortest]
            waiting_time[shortest] = turnaround_time[shortest] - burst_times[shortest]

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
