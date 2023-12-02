# Read the content from the file
with open('perf_output_log.txt', 'r') as file:
    data = file.read()

# Split the content by the separator '===' to separate individual test case results
test_cases = data.split('=== Output for test file:')

# Extract the time elapsed for each test case
time_elapsed = {}
for case in test_cases[1:]:
    lines = case.split('\n')
    file_name = lines[0].strip().split(' ')[0]
    time_lines = [line for line in lines if 'seconds time elapsed' in line]
    if time_lines:
        time = time_lines[0].split()[0]
        time_elapsed[file_name] = float(time)

# Write the extracted time elapsed for each test case into a TSV file
output_file = 'test_cases_time.tsv'
with open(output_file, 'w') as tsvfile:
    tsvfile.write('Test Case\tTime Elapsed (seconds)\n')
    for file, time in time_elapsed.items():
        tsvfile.write(f'{file}\t{time}\n')

print(f'The test cases and their time elapsed have been saved in "{output_file}" file.')
