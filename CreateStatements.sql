CREATE TABLE Accident_Event(Accident_id int Primary Key, Accident_status varchar(40), 
	Item_NO text, Road_id int, Road_type varchar(40), Road_section_name varchar(40), 
	Road_direction varchar(40), Milage int)
CREATE TABLE Location (Location_id serial Primary Key, Latitude Float, Longitude Float)
CREATE TABLE Happened_at (Happened_at_id serial Primary Key, 
	Accident_event_id int REFERENCES Accident_Event(Accident_id), 
	Location_id int REFERENCES Location(Location_id))
CREATE TABLE Detected_at (Detectyed_at_id serial Primary Key, 
	Accident_event_id int REFERENCES Accident_Event(Accident_id), 
	Location_id int REFERENCES Location(Location_id))
CREATE TABLE Health_Center (Health_center_id serial Primary Key, 
	Health_center_name varchar(40), Region varchar(40), Zip_code int, Address varchar(40), 
	Phone_number varchar(40), URL varchar(40))
CREATE TABLE Health_Center_Located_at (Located_at_id serial, 
	Health_center_id int Primary Key REFERENCES Health_Center(Health_center_id), 
	Location_id int REFERENCES Location(Location_id))
CREATE TABLE Police_station (Police_station_id serial Primary Key, 
	Chinese_name_of_the_center varchar(40), English_name_of_the_center varchar(40), 
	Zip_code int, Address varchar(40), Phone_number varchar(40))
CREATE TABLE Police_Station_Located_at (Located_at_id serial, 
	Police_station_id serial Primary Key REFERENCES Police_Station(Police_Station_id), 
	Location_id int REFERENCES Location(Location_id))
CREATE TABLE Assigned_to (Response_id serial Primary Key, 
	Happened_at_id int REFERENCES Happened_at(Happened_at_id), 
	Response_police_stations int REFERENCES Police_Station_Located_At(Police_station_id), 
	Response_health_stations int REFERENCES Health_Center_Located_At(Health_center_id))
CREATE VIEW Accident_Process_Report as SELECT Accident_id, Accident_status FROM Accident_Event