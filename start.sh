#!/bin/bash
docker build . -t sql-coverage-test-suite-mysql5.7:v1.0

docker network create --gateway 172.100.9.253 --subnet 172.100.9.0/24 sql-coverage-test-suite
docker-compose -f docker-compose.yml up -d --force
#mysql
docker exec -it mysql-1 bash "/datainit.sh"
#middleware
docker exec -it middleware-server-1 bash "datainit.sh"



if [ $? -eq 0 ]
then
    echo "sql-coverage-test-suite start successfully!"
else
    echo "sql-coverage-test-suite failed to start!"
fi

cd src/features/test
behave test_case.feature
