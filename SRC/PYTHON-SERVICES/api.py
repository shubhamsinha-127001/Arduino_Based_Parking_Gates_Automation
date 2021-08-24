import psycopg2
import psycopg2.extras
from flask import Flask, request
import sys

print(sys.path)
app = Flask(__name__)


@app.route('/result', methods=['GET', 'POST'])
def result(id, firstName, lastName, vechNumber):
    if request.method == 'GET':
        userName = request.args.get('user', None)
        passWord = request.args.get('pass', None)

        DB_HOST = "localhost"
        DB_NAME = "MIC_PROJECT_PARKING"
        DB_USER = "postgres"
        DB_PASS = "admin"
        try:
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        except:
            print('UNKNOW ERROR while creating database connection::::', sys.exc_info()[0])
        if conn is not None:
            with conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute('INSERT INTO EMP_VECH_DETAILS VALUES("%s", "%s", "%s")' %(id, firstName, lastName, vechNumber))
                    tup = (cur.fetchall())
                    print("<fdwfewfwet", tup[0][0])
                    # return tup;
            conn.close()
        else:
            print('Cant insert values, DB connection not created!')


        if userName == tup[0][0] and  passWord == tup[0][1]:
            return "gseg"
        return "Invalid Login!!!!!!!"

def fetchResult():
    if request.method == 'GET':
        userName = request.args.get('user', None)
        passWord = request.args.get('pass', None)

        DB_HOST = "localhost"
        DB_NAME = "MIC_PROJECT_PARKING"
        DB_USER = "postgres"
        DB_PASS = "admin"
        try:
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        except:
            print('UNKNOW ERROR while creating database connection::::', sys.exc_info()[0])
        if conn is not None:
            with conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute('select vechNumber from EMP_VECH_DETAILS')
                    tup = (cur.fetchall())
                    print("<fdwfewfwet", tup[0][0])
                    # return tup;
            conn.close()
        else:
            print('Cant get values, DB connection not created!')


        if userName == tup[0][0] and  passWord == tup[0][1]:
            return "gseg"
        return "Invalid Login!!!!!!!"
if __name__ == '__main__':
    app.run(debug=True)
