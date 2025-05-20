def calculate_fcfs_data(arrival_times, burst_times):
    n = len(arrival_times)
    jobs = list(range(n))
    start_time = [0] * n
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    sorted_jobs = sorted(zip(jobs, arrival_times, burst_times), key=lambda x: x[1])
    sorted_job_indices = [job[0] for job in sorted_jobs]
    sorted_arrival_times = [job[1] for job in sorted_jobs]
    sorted_burst_times = [job[2] for job in sorted_jobs]

    current_time = 0
    gantt_chart = []  # To store Gantt chart blocks

    for i in range(n):
        job_index = sorted_job_indices[i]
        arrival = sorted_arrival_times[i]
        burst = sorted_burst_times[i]

        start_time[job_index] = max(current_time, arrival)
        finish_time[job_index] = start_time[job_index] + burst
        turnaround_time[job_index] = finish_time[job_index] - arrival
        waiting_time[job_index] = turnaround_time[job_index] - burst
        current_time = finish_time[job_index]


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
        'average_turnaround_time': round(avg_tat, 2),
        'average_waiting_time': round(avg_wt, 2),
        
    }
