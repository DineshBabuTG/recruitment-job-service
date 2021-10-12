"""Service to manage jobs

How to use:

    firefly service.method

"""
import json
import logging
import job_dao

logger = logging.getLogger('job_service')

def addJob(clientname, jobprofile, jobrequirements):
    print("In Add Job API")
    logger.info("In Add Job API")

    logger.info("clientname " + str(clientname) + " jobprofile " + str(jobprofile) + " jobrequirements " + str(jobrequirements))
    print("clientname " + str(clientname) + " jobprofile " + str(jobprofile) + " jobrequirements " + str(jobrequirements))

    job_dao.addjobDAO(clientname, jobprofile, jobrequirements)

    return "Successfully added the job"

def getAllJobs():
    print("In Get All Jobs API")
    logger.info("In Get All Jobs API")
    ## Sample Test Recort to create as dicitionary
    ##job = dict({'jobid': '123', 'clientname': 'testjob', 'jobprofile': 'MTS-3', 'jobrequirements': '5 yrs experience in Java'})
    jobList = []
    jobsFromDB = job_dao.getJobsDAO()
    for row in jobsFromDB:
        job = dict({'jobid': row[0], 'clientname': row[1], 'jobprofile': row[2], 'jobrequirements': row[3]})
        jobList.append(job)
    data = json.dumps(jobList)
    logger.info("Get jobs from DB is " + str(data))
    return data