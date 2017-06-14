import psycopg2

def show_table(cursor, table_name):
    SQL = """SELECT * from """ + table_name
    cur.execute(SQL)
    # fetch [variable?]
    rows = cur.fetchall()
    print "\nShow me the databases:"
    for row in rows:
        print "   ", row

# called when new accident warning event is detected
def create_accident_event():
    print('create')

# https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
if __name__ == "__main__":
    conn = None
    # connects to db
    try:
        conn = psycopg2.connect("dbname='db3' user='db3' host='140.114.77.23' password='db003'")
    except:
        print "I am unable to connect to the database"

    # cursor to work with
    cur = conn.cursor()
    
    view_name = "testview"
    view_sql = "SELECT COUNT(*) FROM " + view_name
    cur.execute(view_sql)
    # initial rows
    # first row, first column
    # to get initial row count
    row_count = cur.fetchall()[0][0]

    # infinite loop to check if new row is created in accident warning event
    while True:
        cur.execute(view_sql)
        rows = cur.fetchall()
        # if same as previous loop, do nothing
        if rows[0][0] == row_count:
            pass        
        # do stuff if new row detected
        else:
            row_count = rows[0][0]
            print(rows[0][0])
            print(row_count)
            create_accident_event()
            conn.commit()

    # commit
    #conn.commit()
