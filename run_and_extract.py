import subprocess
import os
import re
import csv

folder_path = "file-dimacs-aim/" 

output_list = {}

for filename in os.listdir(folder_path):
    if filename.endswith(".cnf"):
        filepath = os.path.join(folder_path, filename)
        command = f"perf stat -d -d -d ./solver < {filepath}"
        
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            output_list[filename] = output
        except subprocess.CalledProcessError as e:
            output_list[filename] = "error"

output_file_path = "output.txt"

with open(output_file_path, "w") as file:
    # file.write("\n".join(output_list.values()))
    for filename in output_list:
        file.write(f"{filename} \n {output_list[filename]} \n ")


# print(f"Output has been written to {output_file_path}")

all_metrics = {}

# print(output_list)
for filename in output_list:
    text = output_list[filename]
    # print()
    stuff = repr(text).split('#')
    dict_stuff = {}
    for item in stuff[1:]:
        content = item.split()
        dict_stuff[content[-1]] = content

    # for item in dict_stuff:
    #     print(f'{item}: {dict_stuff[item]}')

    # print('\n')
    # text = " ".join(dict_stuff['/proc/sys/kernel/nmi_watchdog\\n"'])
    # print(re.search(r'\d+\.\d+ seconds time elapsed', text).group().split()[0])
    # break

    # seconds_time_elapsed = re.search(r'seconds time elapsed\n\n\s+(\d+\.\d+)', text).group(1)
    # l1_dcache_loads = re.search(r'L1-dcache-loads\n\s+([\d,]+)', text).group(1).replace(',', '')
    # l1_dcache_loads_misses = re.search(r'L1-dcache-load-misses\n\s+([\d,]+)', text).group(1).replace(',', '')
    # l1_dcache_access_percentage = re.search(r'L1-dcache-load-misses\n\s+(\d+\.\d+)% of all L1-dcache accesses', text).group(1)

    # text = " ".join(dict_stuff['/proc/sys/kernel/nmi_watchdog\\n"'])

    seconds_time_elapsed = re.search(r'\d+\.\d+ seconds time elapsed', text).group().split()[0]
    l1_dcache_loads = dict_stuff['L1-dcache-loads'][-2]
    l1_dcache_loads_misses = dict_stuff['L1-dcache-load-misses'][-2]
    l1_dcache_access_percentage = dict_stuff['LLC-loads'][0][:-1]

    all_metrics[filename] = {
        "seconds_time_elapsed": seconds_time_elapsed,
        "l1_dcache_loads": l1_dcache_loads,
        "l1_dcache_loads_misses": l1_dcache_loads_misses,
        "l1_dcache_access_percentage": l1_dcache_access_percentage
    }

csv_filename = "metrics_output.csv"
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['Filename', 'Seconds time elapsed', 'L1-dcache loads', 'L1-dcache load misses', '% of all L1-dcache accesses']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for filename, metrics in all_metrics.items():
        writer.writerow({
            'Filename': filename,
            'Seconds time elapsed': metrics['seconds_time_elapsed'],
            'L1-dcache loads': metrics['l1_dcache_loads'],
            'L1-dcache load misses': metrics['l1_dcache_loads_misses'],
            '% of all L1-dcache accesses': metrics['l1_dcache_access_percentage']
        })

print(f"Metrics have been written to {csv_filename}")
