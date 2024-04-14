import re
import json
import sys

def extract_information(sql_file):
    with open(sql_file, 'r') as file:
        sql_content = file.read()

    # Regular expression patterns for extracting information
    pattern_procedure_name = re.compile(r'CREATE\s+PROCEDURE\s+(\S+)\s*\(', re.IGNORECASE)
    pattern_parameters = re.compile(r'@(\S+)\s+\S+', re.IGNORECASE)
    pattern_body = re.compile(r'BEGIN(.+?)END', re.IGNORECASE | re.DOTALL)
    
    procedures = []

    # Find all stored procedures
    for match in re.finditer(pattern_procedure_name, sql_content):
        procedure = {}
        procedure['name'] = match.group(1)
        
        # Extract parameters
        parameters = []
        for param_match in re.finditer(pattern_parameters, sql_content):
            parameters.append(param_match.group(1))
        procedure['parameters'] = parameters
        
        # Extract body
        body_match = re.search(pattern_body, sql_content)
        if body_match:
            procedure['body'] = body_match.group(1).strip()
        else:
            procedure['body'] = ""
        
        procedures.append(procedure)

    return procedures

def save_to_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extraction.py <sql_file>")
        sys.exit(1)

    sql_file = sys.argv[1]
    output_file = sql_file.replace('.sql', '.json')

    procedures = extract_information(sql_file)
    save_to_json(procedures, output_file)

    print(f"Extraction completed. Result saved in {output_file}")
