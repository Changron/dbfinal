import psycopg2

#view_name = "testview"
view_name = "accident_status_information"

def show_table(cursor, table_name):
    SQL = """SELECT * from """ + table_name
    cur.execute(SQL)
    # fetch [variable?]
    rows = cur.fetchall()
    print "\nShow me the databases:"
    for row in rows:
        print "   ", row

# called when new accident warning event is detected
def create_accident_event(cur, remote_cur):
    print('create')
    new_row_sql = "SELECT * FROM " + view_name + " Where accident_status = 'not clear'"
    remote_cur.execute(new_row_sql)
    rows = remote_cur.fetchall()
    # rows contains all unclear accident status info
    # accident_status_information:
    # accident_id, item_no, sensor_latitude,
    # sensor_longtitude, accident_status, road_id,
    # road_direction, milage, road_type,
    # road_section_name
    for row in rows:
        print "   ", row
        insert_row_sql = "INSERT INTO accident_event VALUES (" +\
                            str(row[0]) + "," +\
                            "'" + str(row[4]) + "'" + "," +\
                            "'" + str(row[1]) + "'" + "," +\
                            str(row[5]) + "," +\
                            "'" + str(row[8]) + "'" + "," +\
                            "'" + str(row[9]) + "'" + "," +\
                            "'" + str(row[6]) + "'" + "," +\
                            str(row[7]) + ")"
                            # actuall location null
        cur.execute(insert_row_sql)

    show_table(cur, 'accident_event')

# https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
if __name__ == "__main__":
    conn = None
    # connects to db
    try:
        conn = psycopg2.connect("dbname='db3' user='db3' host='140.114.77.23' password='db003'")
        remote_conn = psycopg2.connect("dbname='db4' user='db3' host='140.114.77.23' password='db003'")
    except:
        print "I am unable to connect to the database"

    # cursor to work with
    cur = conn.cursor()
    # cursor to work with
    remote_cur = remote_conn.cursor()
        #cur.execute("CONNECT TO \"db4\"")

    view_sql = "SELECT COUNT(*) FROM " + view_name

    remote_cur.execute(view_sql)

    # initial rows
    # first row, first column
    # to get initial row count
    row_count = remote_cur.fetchall()[0][0]

    # infinite loop to check if new row is created in accident warning event
    while True:
        remote_cur.execute(view_sql)
        rows = remote_cur.fetchall()
        # if same as previous loop, do nothing
        if rows[0][0] == row_count:
            pass
        # do stuff if new row detected
        else:
            print('new row')
            row_count = rows[0][0]
            create_accident_event(cur, remote_cur)
            conn.commit()

    # commit
    #conn.commit()
