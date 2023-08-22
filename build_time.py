import jenkins
import pandas as pd

#TODO: input the details
username='<username>'
password='<password>'
file_path='<file path of the Excel sheet>'
server_name='<link to the jenkins server>'
lob='<name of lob to calculate the build time>'

class DurationMetrics:
    totalBuildDuration = 0.0
    jobBuildDuration= 0.0
    jobnumberOfBuilds = 0.0
    totalnumberOfBuilds = 0.0
    jobbuildDurations=[]
    jobnames=[]
    averageDuration = 0.0
    server = None

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
        self.server = jenkins.Jenkins(server_name, username, password, timeout=timeout_value)

    def export(self):
        # TODO: export the data to an Excel sheet
        data={'Job name':self.jobnames,'Job Build Duration':self.jobbuildDurations}
        df=pd.DataFrame(data)
        last_row = {'Job name':'Average','Job Build Duration':self.averageDuration}
        df1=df._append(last_row,ignore_index=True)
        df1.to_excel(file_path, index=False)

if __name__ == "__main__":
    try:
        durationMetrics = DurationMetrics()
        durationMetrics.connectToJenkins()
        durationMetrics.getJobDuration()
        print("Build Average Duration: %.2f minutes" % durationMetrics.calculateAverageDuration())
        durationMetrics.export()
    except ValueError as e:
        print(f"Error: {e}")
    
