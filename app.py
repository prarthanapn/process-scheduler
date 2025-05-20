from flask import Flask, render_template, request

# Import algorithm functions from their respective folders
from fcfs import calculate_fcfs_data
from rr import calculate_rr_data
from sjf import calculate_sjf_data
from srtf import calculate_srtf_data
from priority_nonpreemptive import calculate_priority_np_data
from priority_preemptive import calculate_priority_p_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/output', methods=['POST'])
def output():
    algorithm = request.form['algorithm']
    arrival_times_str = request.form['arrival']
    burst_times_str = request.form['burst']

    try:
        arrival_times = [int(x) for x in arrival_times_str.strip().split()]
        burst_times = [int(x) for x in burst_times_str.strip().split()]
    except ValueError:
        return "Please enter only integers for Arrival and Burst times."

    if len(arrival_times) != len(burst_times):
        return "Number of arrival times and burst times must be the same."

    if algorithm == 'fcfs':
        results = calculate_fcfs_data(arrival_times, burst_times)
        algo_name = "First Come First Serve"

    elif algorithm == 'roundrobin':
        try:
            quantum = int(request.form['quantum'])
        except (ValueError, KeyError):
            return "Please enter a valid integer for Time Quantum."
        results = calculate_rr_data(arrival_times, burst_times, quantum)
        algo_name = "Round Robin"

    elif algorithm == 'sjf':
        results = calculate_sjf_data(arrival_times, burst_times)
        algo_name = "Shortest Job First (Non-Preemptive)"

    elif algorithm == 'srtf':
        results = calculate_srtf_data(arrival_times, burst_times)
        algo_name = "Shortest Remaining Time First (Preemptive)"

    elif algorithm == 'priority_np':
        try:
            priority_str = request.form['priority']
            priorities = [int(x) for x in priority_str.strip().split()]
        except (ValueError, KeyError):
            return "Please enter valid integer priorities."
        if len(priorities) != len(arrival_times):
            return "Number of priorities must match number of processes."
        results = calculate_priority_np_data(arrival_times, burst_times, priorities)
        algo_name = "Priority Scheduling (Non-Preemptive)"

    elif algorithm == 'priority_p':
        try:
            priority_str = request.form['priority']
            priorities = [int(x) for x in priority_str.strip().split()]
        except (ValueError, KeyError):
            return "Please enter valid integer priorities."
        if len(priorities) != len(arrival_times):
            return "Number of priorities must match number of processes."
        results = calculate_priority_p_data(arrival_times, burst_times, priorities)
        algo_name = "Priority Scheduling (Preemptive)"

    else:
        return "Invalid algorithm selected."

    return render_template('output.html', results=results, algorithm_name=algo_name)

if __name__ == '__main__':
    app.run(debug=True)
