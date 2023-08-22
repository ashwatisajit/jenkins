import jenkins
import pandas as pd
import configparser, itertools
file_path=''
server_name=''
lob=''
def read_config_file(config_file_path):
    #TODO: read input from the config file
    config = configparser.ConfigParser()
    config.read(config_file_path)
    if 'Jenkins' in config:
        username = config.get('Jenkins', 'username')
        password = config.get('Jenkins', 'password')
        file_path = config.get('Jenkins', 'file_path')
        server_name = config.get('Jenkins', 'server_name')
        lob = config.get('Jenkins', 'lob')
        return username, password, file_path, server_name, lob
    else:
        raise ValueError("Invalid or missing [Jenkins] section in the config file")

class DurationMetrics:
    username = ''
    password = ''
    totalBuildDuration = 0.0
    jobBuildDuration= 0.0
    jobnumberOfBuilds = 0.0
    totalnumberOfBuilds = 0.0
    jobbuildDurations=[]
    jobnames=[]
    averageDuration = 0.0
    server = None

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def calculateAverageDuration(self):
        #TODO: calculate average duration
        self.averageDuration = (self.totalBuildDuration / self.totalnumberOfBuilds) / 60000
        return self.averageDuration
    
    def calculateJobDuration(self):
        #TODO: calculate job duration
        jobDuration = (self.jobBuildDuration / self.jobnumberOfBuilds) / 60000
        self.jobbuildDurations.append(jobDuration)
        return jobDuration

    def getJobDuration(self):
        # TODO: get job duration
        jenkinsJobs = self.server.get_all_jobs()
        for job in jenkinsJobs:
            if lob in job['name']:
                self.jobnames.append(job['name'])
                myJob = self.server.get_job_info(job['name'], 0, True)
                myJobBuilds = myJob.get('builds')
                for build in myJobBuilds:
                    buildNumber = build.get('number')
                    buildInfo = self.server.get_build_info(job['name'], buildNumber)
                    if(buildInfo['result']=='SUCCESS'):
                        buildDuration = buildInfo.get('duration')
                        self.jobBuildDuration += buildDuration
                        self.jobnumberOfBuilds += 1.0
                print(f"Build Duration for job {job['name']}: {durationMetrics.calculateJobDuration():.2f} minutes")
                self.totalBuildDuration += self.jobBuildDuration
                self.totalnumberOfBuilds += self.jobnumberOfBuilds
                self.jobBuildDuration = 0.0
                self.jobnumberOfBuilds = 0.0

    def connectToJenkins(self):
        # TODO: connect to Jenkins server
        timeout_value = 30
        self.server = jenkins.Jenkins(server_name, username=self.username, password=self.password,timeout=timeout_value)

    def export(self):
        # TODO: export the data to an Excel sheet
        data={'Job name':self.jobnames,'Job Build Duration':self.jobbuildDurations}
        df=pd.DataFrame(data)
        last_row = {'Job name':'Average','Job Build Duration':self.averageDuration}
        df1=df._append(last_row,ignore_index=True)
        df1.to_excel(file_path, index=False)

if __name__ == "__main__":
    config_file_path = 'jenkins_config.ini'
    try:
        username, password, file_path, server_name, lob = read_config_file(config_file_path)
        durationMetrics = DurationMetrics(username, password)
        durationMetrics.connectToJenkins()
        durationMetrics.getJobDuration()
        print("Build Average Duration: %.2f minutes" % durationMetrics.calculateAverageDuration())
        durationMetrics.export()
    except ValueError as e:
        print(f"Error: {e}")
    
