import sys
import psycopg2
import psycopg2.extras
import urllib

global DB_HOST, DB_NAME, DB_USER, DB_PASS
DB_HOST = "localhost"
DB_NAME = "MIC_PROJECT_PARKING"
DB_USER = "postgres"
DB_PASS = "admin"
conn = None

try:
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
except:
    print('UNKNOW ERROR while creating database connection::::', sys.exc_info()[0])

def checkAdminLogin():
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    except:
        print('UNKNOW ERROR while creating database connection::::', sys.exc_info()[0])
    if conn is not None:
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute('select * from users')
                tup = (cur.fetchall())
                print(tup)
                return tup;
        conn.close()
    else:
        print('Cant insert values, DB connection not created!')

def insertNewEmp():
    # print(conn)
    empid = "11";
    firstname = 'Adam'
    lastname = 'james'
    vechnu = 'gfs'
    query = "insert into emp_vec_details values ('" + empid + "', '" + firstname + "', '" + lastname + "', '" + vechnu + "');"
    print(query)
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    except:
        print('UNKNOW ERROR while creating database connection::::', sys.exc_info()[0])
    if conn is not None:
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(query)
        conn.close()
    else:
        print('Cant insert values, DB connection not created!')


def down():
    import requests

    Picture_request = requests.get("http://192.168.2.107/picture.jpeg")
    if Picture_request.status_code == 200:
        with open("D:\sdf.jpg", 'wb') as f:
            f.write(Picture_request.content)

def htrtr():
    import urllib.request
    with urllib.request.urlopen('http://192.168.2.107/picture.jpeg') as f:
        html = f.read().decode('utf-8')

down()