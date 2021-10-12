from flask import Flask, abort, request
import logging.config
import job_service
app = Flask(__name__)

logging.config.fileConfig('logging.conf')
# create logger
logger = logging.getLogger('job_service_app')

@app.route('/', methods=["GET"])
def candidate_service_home():
    return "Job Service App..."

@app.route('/jobservice/addjob', methods=["POST"])
def add_candidate():
    if not request.json:
        logger.info('The Request Body is not the JSON Type... Hence throwing 400 error code...')
        abort(400)
    logger.info('JSON Request: ' + str(request.json))
    print(request.json)
    data = request.json
    clientname = data['clientname']
    logger.info('clientname: ' + clientname)
    print('clientname: ' + clientname)
    jobprofile = data['jobprofile']
    jobrequirements = data['jobrequirements']

    logger.info('Going to call add job API...')
    jobAdded =  job_service.addJob(clientname=clientname, jobprofile=jobprofile, jobrequirements=jobrequirements)
    print("Job Added " + str(jobAdded))
    return str(jobAdded)

@app.route('/jobservice/getalljobs', methods=["GET"])
def get_All_Candidates():
    jobsList = job_service.getAllJobs()

    return jobsList

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8002)