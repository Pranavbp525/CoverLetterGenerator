import yaml

def load_yaml_file(yaml_file_path):
    with open(yaml_file_path, 'r') as file:
        applicant_data = yaml.safe_load(file)
    return applicant_data
