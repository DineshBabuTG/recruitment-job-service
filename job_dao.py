import random

import mysql.connector
import logging
import random
import os
from mysql.connector import Error

logger = logging.getLogger('job_dao')

def getMySQLConnection():
    try:
        dbhostname = os.environ['dbhostname']
        print("Database hostname is " + dbhostname)
        logger.info("Database hostname is " + dbhostname)

        connection_config_dict = {
            'user': 'edureka',
            'password': 'edureka',
            'host': dbhostname,
            'port': '3306',
            'database': 'dinasys',
            'raise_on_warnings': True
        }
        connection = mysql.connector.connect(**connection_config_dict)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            logger.info("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            logger.info("You're connected to database: ", record)
        else:
            logger.info("MySQL not connected")
        return connection
    except Error as e:
        logger.info("Error while connecting to MySQL", e)
        print("Error while connecting to MySQL", e)
    finally:
        logger.info("In Finally of DB Connection")
        print("In Finally of DB Connection")
        # if connection.is_connected():
        #     cursor.close()
        #     connection.close()
        #     print("MySQL connection is closed")

def executeDBInsertQuery(connection, statement, data):
    cursor = connection.cursor()
    try:
        result = cursor.execute(statement, data)
        connection.commit()
        logger.info(f"Query executed successfully {statement}")
        return result
    except Error as e:
        logger.info(f"Query execution error '{e}' occurred")

def executeDBExecuteQuery(connection, statement):
    cursor = connection.cursor()
    try:
        cursor.execute(statement)
        logger.info(f"Query executed successfully {statement}")
        return cursor.fetchall()
    except Error as e:
        logger.info(f"Query execution error '{e}' occurred")

def addjobDAO(clientname, jobprofile, jobrequirements):
    print("In Add Job DAO Service")
    logger.info("In Add Job DAO Service")
    jobid = random.randint(1,999999)
    logger.info(
        "jobid " + str(jobid) + " clientname " + str(clientname) + " jobprofile " + str(jobprofile) + " jobrequirements " + str(jobrequirements))
    print(
        "jobid " + str(jobid) + " clientname " + str(clientname) + " jobprofile " + str(jobprofile) + " jobrequirements " + str(jobrequirements))

    insert_stmt = (
        "INSERT INTO jobs (jobid, clientname, jobprofile, jobrequirements) "
        "VALUES (%s, %s, %s, %s)"
    )
    data = (jobid, clientname, jobprofile, jobrequirements)
    #mySql_Add_Job_insert_Query = "insert into jobs values(" + str(jobid) + "," + clientname + "," +  jobprofile + "," + jobrequirements + ")"
    logger.info(insert_stmt, data)
    connection = getMySQLConnection()
    executeDBInsertQuery(connection, insert_stmt, data)

    logger.info("Successfully inserted the job entry for the id " + str(jobid))
    return "Successfully inserted the job entry for the id " + str(jobid)

def getJobsDAO():
    print("In Gets Jobs DAO Service")
    logger.info("In Add Job DB Service")

    mySql_Get_Jobs_Select_Query = "select * from jobs"
    connection = getMySQLConnection()
    result = executeDBExecuteQuery(connection, mySql_Get_Jobs_Select_Query)
    logger.info("Successfully get the jobs " + str(result))
    return result