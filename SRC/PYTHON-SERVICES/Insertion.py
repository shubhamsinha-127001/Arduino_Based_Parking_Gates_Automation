import sys
import psycopg2
import psycopg2.extras


class DBConnections:
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

    def checkAdminLogin(self):
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

    def insertNewEmp(self):
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


obj = DBConnections();
obj.checkAdminLogin();