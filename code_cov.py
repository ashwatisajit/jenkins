from sonarqube import SonarQubeClient
import pandas as pd
import configparser, itertools

SONARQUBE_URL = ''
USERNAME = ''
PASSWORD = ''

project_keys = []
project_names = []
coverage_values= []
average= 0.0
total= 0.0
numberofproj= 0.0
file_path=''
i= 0

def read_config_file(config_file_path):
    #TODO: read input from the config file
    config = configparser.ConfigParser()
    config.read(config_file_path)
    if 'Sonar' in config:
        username = config.get('Sonar', 'username')
        password = config.get('Sonar', 'password')
        file_path = config.get('Sonar', 'file_path')
        server_name = config.get('Sonar', 'server_name')
        return username, password, file_path, server_name
    else:
        raise ValueError("Invalid or missing [Sonar] section in the config file")

def get_all_project_names():
    #TODO: get project names
    try:
        projects = sonar.projects.search_projects()
        for project in projects['components']:
            project_keys.append(project['key'])
        return project_keys
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_project_code_coverage(project_key):
    #TODO: get project code coverage
    try:
        flag=0
        str=''
        code_coverage_result = sonar.measures.get_component_with_specified_measures(
            component=project_key,
            metricKeys="coverage"
        )
        project_names.append(code_coverage_result['component']['name'])
        for num in code_coverage_result['component']['measures']:
            if(num['metric']=='coverage'):
                code_coverage=float(num['value'])
                flag=1
                break 
        if(flag):
            print(f"Code Coverage for project {project_names[i]}: {code_coverage}%")
        else:
            #print(f"Code Coverage for project {project_names[i]}: ND")
            str= project_names.pop()
            code_coverage=-1
        return code_coverage

    except Exception as e:
        print(f"Error: {e}")
        return None

def calculateAverage():
        #TODO: calculate average code coverage
        global average
        average = (total/numberofproj)
        print(f"Average code coverage: {average}%")
    
def export():
        #TODO: export the data to an Excel sheet
        data={'Job name':project_names,'Code Coverage':coverage_values}
        df=pd.DataFrame(data)
        last_row = {'Job name':'Average','Code Coverage':average}
        df1=df._append(last_row,ignore_index=True)
        df1.to_excel(file_path, index=False)

if __name__ == "__main__":
    config_file_path = 'jenkins_config2.ini'
    USERNAME, PASSWORD, file_path, SONARQUBE_URL = read_config_file(config_file_path)
    sonar = SonarQubeClient(sonarqube_url=SONARQUBE_URL, username=USERNAME, password=PASSWORD)
    project_keys = get_all_project_names()
    for key in project_keys:
        coverage_value = get_project_code_coverage(key)
        if(coverage_value!=-1):
            numberofproj+=1
            total+=coverage_value
            i=i+1
            coverage_values.append(coverage_value)
    calculateAverage()
    export()
