**Code to collect build times of various jobs on Jenkins**

**build_time.py**

The build_time.py code collects the build times of various jobs of a LOB from Jenkins. The user must input details like the username and password of the Jenkins server, the file path to the Excel sheet where the results are to be stored, the server_name which is the link to the Jenkins server, and the name of the LOB whose job build times are to be collected, into the code variables. Using the information provided by the user, the code will be able to connect to the Jenkins server. It then reads the build information of each job and calculates the average build time for the particular job and the consolidated average of all jobs. It prints the data and exports it to an Excel file.

**Code to collect code coverage of various projects on SonarQube**

**code_cov.py**

The code_cov.py code collects the code coverages of various projects on SonarQube. The user must input the authentication token as a parameter when running the code in the Terminal. The user must input details like the file path to the Excel sheet where the results are to be stored, and the server_name which is the link to the SonarQube server, into the code variables. Using the information provided by the user, the code will be able to connect to the SonarQube server. It gets all the project names and for each project, it gets their code coverage and prints the data. It calculates the consolidated average of all code coverages and exports all the data to an Excel file. This code only collects the code coverages of the projects with a value for code coverage and ignores the other projects.
