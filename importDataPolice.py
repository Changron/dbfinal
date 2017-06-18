import psycopg2
import codecs

def importPolice(cur):

    fileaddress = "Police Station"
    file = codecs.open(fileaddress,"r","utf-8")

    #skip first line
    file.readline()
    
    for line in file:
        values = line.rstrip('\n').split('\t')
       
        #set strings
        stringindex = [0,1,2,3,4]
        for index in stringindex:
            values[index]='\''+values[index]+'\''

        #Create Police_Station
        SQLstatement= """INSERT INTO Police_Station 
        (Chinese_name_of_the_center, English_name_of_the_center, Zip_code, Address, Phone_number) 
        VALUES ("""
        SQLstatement += ', '.join(values[:-2]) 
        SQLstatement += ')'
        SQLstatement += ' RETURNING Police_station_id'
        
        print (SQLstatement)
        cur.execute(SQLstatement)
        policeStationId = cur.fetchone()[0]

        #Create Location
        SQLstatement= """INSERT INTO Location 
        (Latitude,Longitude) 
        VALUES ("""
        SQLstatement += ', '.join(values[-2:]) 
        SQLstatement += ')'
        SQLstatement += ' RETURNING Location_id'

        print (SQLstatement)
        cur.execute(SQLstatement)
        locationId = cur.fetchone()[0]

        #Create Police_Station_Located_at
        SQLstatement= """INSERT INTO Police_Station_Located_at 
        (Police_station_id, Location_id)
        VALUES ("""
        SQLstatement += str(policeStationId)
        SQLstatement += ' ,'
        SQLstatement += str(locationId)
        SQLstatement += ')'

        cur.execute(SQLstatement)

def importHealthCenter(cur):
    #check name
    fileaddress = "Health Center"
    file = codecs.open(fileaddress,"r","utf-8")

    #skip first line
    file.readline()
    
    for line in file:

        allvalues = line.rstrip('\n').split('\t')


        #set strings
        #5, 6 coordinates
        useindex = [1,3,4,5,6,7,9,10]
        stringindex = [0,1,3,4,5]
        values = []
        location = []

        for index in useindex:
            if index==6 or index==7:
                location.append(allvalues[index])
            else:
                values.append(allvalues[index])
        print(values)
        print(location)

        for index in stringindex:
            values[index]='\''+values[index]+'\''

        #Create Health_Center
        SQLstatement= """INSERT INTO Health_Center 
        (Health_center_name, Region, Zip_code, Address, Phone_number, URL) 
        VALUES ("""
        SQLstatement += ', '.join(values) 
        SQLstatement += ')'
        SQLstatement += ' RETURNING Health_center_id'
        
        print (SQLstatement)
        cur.execute(SQLstatement)
        healthCenterId = cur.fetchone()[0]

        #Create Location
        SQLstatement= """INSERT INTO Location 
        (Latitude,Longitude) 
        VALUES ("""
        SQLstatement += ', '.join(location) 
        SQLstatement += ')'
        SQLstatement += ' RETURNING Location_id'

        print (SQLstatement)
        cur.execute(SQLstatement)
        locationId = cur.fetchone()[0]

        #Create Health_Center_Located_at
        SQLstatement= """INSERT INTO Health_Center_Located_at 
        (Health_center_id, Location_id)
        VALUES ("""
        SQLstatement += str(healthCenterId)
        SQLstatement += ' ,'
        SQLstatement += str(locationId)
        SQLstatement += ')'

        cur.execute(SQLstatement)

if __name__ == "__main__":

    conn = None
    # connects to db
    try:
        conn = psycopg2.connect("dbname='db3' user='db3' host='140.114.77.23' password='db003'")
    except:
        print ("I am unable to connect to the database")

    # cursor to work with
    cur = conn.cursor() 

    #importPolice(cur)
    importHealthCenter(cur)

    # commit
    conn.commit()