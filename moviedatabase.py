import sqlite3

conn = sqlite3.connect('movie.db')
conn.execute('''CREATE TABLE MOVIE
         (ID INT PRIMARY KEY     NOT NULL,
         Movie_name           TEXT    NOT NULL,
         Lead_actor            TEXT     NOT NULL,
         Lead_actress        TEXT       NOT NULL,
         Year_of_release        INT     NOT NULL,
         Director_name      TEXT        NOT NULL);''')

conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (1, 'Chichhore', 'Sushant Singh Rajput', 'Shraddha Kapoor', 2019, 'Nitesh Tiwari')");

conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (2, 'Gangubai Kathiawadi', 'Shantanu Maheswari', 'Alia Bhatt', 2022, 'Sanjay Leela Bhansali')");

conn.execute("INSERT INTO MOVIE (ID,Movie_name,Lead_actor,Lead_actress,Year_of_release,Director_name) \
      VALUES (3, 'Rab ne banadi jodi', 'Shahruk Khan', 'Anushka Sharma', 2008, 'Anita Chopra')");

conn.commit()
#conn.close()


print(" 1. Chichhore \n 2. Gangubai kathiawadi 2\n 3. Rab ne bana di")
choice = int(input("Enter your choice: "))

val = conn.execute("SELECT * from MOVIE WHERE ID is "+str(choice))
for v in val:
    movie_id= v[0]
    movie_name= v[1]
    Lead_actor= v[2]
    Lead_actress= v[3]
    Year_of_release= v[4]
    Director = v[5]
print("Movie ID      : ",movie_id)
print("Movie Name    : ",movie_name)
print("Lead Actor    : ",Lead_actor)
print("Lead Actress  : ",Lead_actress)
print("Released Year : ",Year_of_release)
print("Director      : ",Director)
            
