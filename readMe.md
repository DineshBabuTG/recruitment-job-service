Run the following docker command to run the job service container

docker run -d -p 8002:8002 -e dbhostname=<DB-Hostname> tgdinababu/jobapp:latest