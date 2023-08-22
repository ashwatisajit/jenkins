**Code to collect build times of various jobs on Jenkins**

build_time.py

The build_time.py code collects the build times of various jobs of a LOB from Jenkins. The code reads the information from the config file jenkins_config.ini to connect to the Jenkins server. It then reads the build information of each job and calculates the average build time for the particular job and the consolidated average of all jobs. It prints the data and exports it to an Excel file.

jenkins_config.py

The config file for saving the username and password of the Jenkins server, the file path to the Excel sheet where the results are to be stored, the server_name which is the link to the Jenkins server, and the name of the LOB whose project build times are to be collected.

**Code to collect code coverage of various projects on SonarQube**

code_cov.py

The code_cov.py code collects the code coverages of various projects on SonarQube. The code reads the information from the config file jenkins_config2.ini to connect to the SonarQube server. It gets all the project names and for each project, it gets their code coverage and prints the data. It calculates the consolidated average of all code coverages and exports all the data to an Excel file. This code only collects the code coverages of the projects with a value for code coverage and ignores the other projects.

jenkins_config2.py

The config file for saving the username and password of the SonarQube server, the file path to the Excel sheet where the results are to be stored, and the server_name which is the link to the SonarQube server.
