import re

input_file = 'amphoe.sql'  
output_file = 'dataA.txt' 

def extract_data(file_path):
    data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            
            match = re.search(r"INSERT INTO\s+`amphoe`\s*\(.*?\)\s*VALUES\s*\(\s*(\d+),\s*'([^']+)'", line)
            if match:
                code, name = match.groups()
                data.append(f'{code}, {name}')
                
    return data

def out_data(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))
        

a = extract_data(input_file)
b = out_data(a, output_file)