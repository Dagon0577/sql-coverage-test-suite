#!/bin/bash
service mysql start
USERNAME="root"
PORT="3306"
HOSTNAME="localhost"


execSql="USE mysql;GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;FLUSH PRIVILEGES;"

echo "Initializing MySQL."
mysql -u${USERNAME} -h${HOSTNAME} -P${PORT} -e "${execSql}"

if [ $? -eq 0 ]
then
    echo "Initializing MySQL success!"
else 
    echo "Initializing MySQL error failed!"
fi
