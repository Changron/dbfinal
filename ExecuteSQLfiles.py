import psycopg2

def show_table(cursor, table_name):
    SQL = """SELECT * from """ + table_name
    cur.execute(SQL)
    # fetch [variable?]
    rows = cur.fetchall()
    print ("\nShow me the databases:")
    for row in rows:
        
        print ("   ", row)

# https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
if __name__ == "__main__":

    #fileaddress = "DeleteTables.sql"
    fileaddress = "CreateStatements2.sql"
    reader = open(fileaddress,'r')

    conn = None
    # connects to db
    try:
        conn = psycopg2.connect("dbname='db3' user='db3' host='140.114.77.23' password='db003'")
    except:
        print ("I am unable to connect to the database")

    # cursor to work with
    cur = conn.cursor()
    # execute query
    #show_table(cur, "test")    

    # must use single quote
    for statement in reader:
        cur.execute(statement)

    #show_table(cur, "test")  
    
    # commit
    conn.commit()
