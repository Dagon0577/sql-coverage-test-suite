import pymysql
import os
import logging

host = "172.100.9.2"
user = "root"
password = "123456"
port = 3306

middleware_host = "172.100.9.1"
middleware_user = "root"
middleware_password = "123456"
middleware_port = 3306


def compareSQLResult(sql_path):
    db = pymysql.connect(host=host, user=user, password=password, port=port)
    middleware = pymysql.connect(host=middleware_host, user=middleware_user,
                                 password=middleware_password, port=middleware_port)
    cur = db.cursor()
    middlewareCur = middleware.cursor()
    logging.info(sql_path)
    sqlFiles = os.listdir(sql_path)
    for sqlFile in sqlFiles:
        if not os.path.isdir(sqlFile):
            f = open(sql_path+"/"+sqlFile, 'r', encoding='utf-8', errors='ignore')
            for str in f:
                str = str.strip()
                if len(str) == 0:
                    continue
                if str[0] == '#':
                    continue
                elif str.startswith('/*'):
                    continue
                logging.info(str)
                sql = str.split(';')
                command = sql[0]
                if not command.isspace() or command == '':
                    try:
                        cur.execute(command)
                        middlewareCur.execute(command)
                        try:
                            assert cur.rowcount == middlewareCur.rowcount
                        except:
                            logging.error(
                                "result set rowcount is not same!")
                            return 0
                        result = cur.fetchall()
                        middlewareResult = middlewareCur.fetchall()
                        if sql[1] == '1':
                            try:
                                for index in range(len(result)):
                                    assert result[index] == middlewareResult[index]
                            except:
                                logging.error(
                                    "result set is not same in number %d column!" % index)
                                return 0
                        elif sql[1] == '' and checkType(sql[0]) == 0 and len(result) > 0:
                            logging.info("Compare with sorted result set. ")
                            ascOrDesc = False
                            # ASC
                            mapNone = {}
                            for j in range(len(result[0])):
                                mapNone[j] = 1
                            for i in range(len(result)):
                                for j in range(len(result[0])):
                                    if result[i][j] == None:
                                        mapNone[j] = 0
                            for j in range(len(result[0])):
                                if mapNone[j] == 0:
                                    continue
                                result = sorted(result, key=lambda x: x[j],
                                                reverse=ascOrDesc)
                                middlewareResult = sorted(middlewareResult, key=lambda x: x[j],
                                                          reverse=ascOrDesc)
                            try:
                                for index in range(len(result)):
                                    assert result[index] == middlewareResult[index]
                            except:
                                logging.error(
                                    "Sorted result set is not same in number %d column!" % index)
                                return 0
                        else:
                            continue
                    except Exception as msg:
                        logging.info(sqlFile + " fail sql is " + command)
                        logging.error(msg)
                        return 0
                logging.info('sql pass.')
            f.close()
    db.commit()
    db.close()
    middleware.commit()
    middleware.close()
    return 1


def executeSQL(sql_path):
    #db = pymysql.connect(host=host, user=user, password=password, port=port)
    middleware = pymysql.connect(host=middleware_host, user=middleware_user,
                                 password=middleware_password, port=middleware_port)
    #cur = db.cursor()
    middlewareCur = middleware.cursor()
    logging.info(sql_path)
    sqlFiles = os.listdir(sql_path)
    for sqlFile in sqlFiles:
        if not os.path.isdir(sqlFile):
            f = open(sql_path+"/"+sqlFile, 'r', encoding='utf-8', errors='ignore')
            for str in f:
                str = str.strip()
                if len(str) == 0:
                    continue
                if str[0] == '#':
                    continue
                elif str.startswith('/*'):
                    continue
                logging.info(str)
                sql = str.split(';')
                command = sql[0]
                if not command.isspace() or command == '':
                    try:
                        #cur.execute(command)
                        middlewareCur.execute(command)
                    except Exception as msg:
                        logging.info(sqlFile + " fail sql is " + command)
                        logging.error(msg)
                        return 0
            f.close()
            logging.info(' sql pass.')
    #db.commit()
    #db.close()
    middleware.commit()
    middleware.close()
    return 1


def checkType(sql):
    # 0:select, -1:empty, 1:others
    tokens = sql.split()
    if len(tokens) > 0:
        if tokens[0].lower() == "select" or tokens[0].lower() == "(select":
            return 0
        else:
            return 1
    else:
        return -1
