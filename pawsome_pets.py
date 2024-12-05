import sqlite3

#start connection to SQLite database
conn = sqlite3.connect('pawsome_pets.db')

#make cursor object for query execution
cursor = conn.cursor()

print("-----------------------------------------------------------------------------------------------------")
print("CSC 423 - Pawsome Pets Database Project")
print("Authors: Matthew Elpus, Eddy Boris\n")
print("-----------------------------------------------------------------------------------------------------")

#PART A 
#Make all relations in the database

#create Clinic relation
query = """
    CREATE TABLE IF NOT EXISTS Clinic (
        clinicNo INTEGER PRIMARY KEY
            CHECK(clinicNo BETWEEN 00000 AND 99999),
        name TEXT NOT NULL UNIQUE,
        street TEXT NOT NULL,
        buildingInfo TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL 
            CHECK(LENGTH(state) = 2),
        ZIPcode TEXT NOT NULL 
            CHECK(LENGTH(ZIPcode) = 5),
        telephone TEXT NOT NULL UNIQUE 
            CHECK(LENGTH(telephone) = 10),
        staffNo INTEGER,
        FOREIGN KEY (staffNo) 
            REFERENCES Staff (staffNo) 
            ON DELETE SET DEFAULT
        );
        """
cursor.execute(query)
conn.commit()

#create Staff relation
query = """
    CREATE TABLE IF NOT EXISTS Staff (
        staffNo INTEGER PRIMARY KEY 
            CHECK(staffNo BETWEEN 0100000 AND 9999999),
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        street TEXT,
        buildingInfo TEXT,
        city TEXT,
        state TEXT 
            CHECK(LENGTH(state) = 2),
        ZIPcode TEXT 
            CHECK(LENGTH(ZIPcode) = 5),
        telephone TEXT UNIQUE NOT NULL 
            CHECK(LENGTH(telephone) = 10),
        DOB DATE,
        position TEXT NOT NULL,
        salary REAL NOT NULL 
            CHECK(salary > 0),
        clinicNo INTEGER,
        FOREIGN KEY (clinicNo) 
            REFERENCES Clinic (clinicNo) 
            ON DELETE SET DEFAULT
        );
        """
cursor.execute(query)
conn.commit()

#create Owner relation
query = """
    CREATE TABLE IF NOT EXISTS Owner (
        ownerNo INTEGER PRIMARY KEY 
            CHECK(ownerNo BETWEEN 440000000 AND 999999999),
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        street TEXT NOT NULL,
        buildingInfo TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL 
            CHECK(LENGTH(state) = 2),
        ZIPcode TEXT NOT NULL 
            CHECK(LENGTH(ZIPcode) = 5),
        telephone TEXT UNIQUE NOT NULL 
            CHECK(LENGTH(telephone) = 10)
        );
        """
cursor.execute(query)
conn.commit()

#create Pet relation
query = """
    CREATE TABLE IF NOT EXISTS Pet (
        petNo INTEGER PRIMARY KEY 
            CHECK(petNo BETWEEN 1000000000 AND 6599999999),
        petName TEXT NOT NULL,
        DOB DATE,
        species TEXT NOT NULL,
        breed TEXT,
        color TEXT,
        ownerNo INTEGER NOT NULL,
        clinicNo INTEGER NOT NULL,
        FOREIGN KEY (ownerNo) 
            REFERENCES Owner (ownerNo) 
            ON DELETE CASCADE,
        FOREIGN KEY (clinicNo) 
            REFERENCES Clinic (clinicNo)
            ON DELETE CASCADE
        );
        """
cursor.execute(query)
conn.commit()

#create Examination relation
query = """
    CREATE TABLE IF NOT EXISTS Examination (
        examNo INTEGER PRIMARY KEY 
            CHECK(examNo BETWEEN 00000000000 AND 99999999999),
        chiefComplaint TEXT NOT NULL,
        description TEXT NOT NULL,
        dateSeen DATE NOT NULL,
        actionsTaken TEXT NOT NULL,
        petNo INTEGER NOT NULL,
        staffNo INTEGER NOT NULL,
        FOREIGN KEY (petNo) 
            REFERENCES Pet (petNo) 
            ON DELETE CASCADE,
        FOREIGN KEY (staffNo) 
            REFERENCES Staff (staffNo) 
            ON DELETE SET NULL
        );
        """
cursor.execute(query)
conn.commit()

print("Successful Table Creation")
print("---------------------------------------------------------------------------------------------")

#PART B 
#Create all tupes

# tuples for Clinic
query = """
    INSERT INTO Clinic 
        (clinicNo, name, street, buildingInfo, city, state, ZIPcode, telephone)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
cursor.executemany(query, [
    (10001, "University Pet Clinic", "100 Ponce de Leon Blvd", "Suite 101", "Miami", "FL", "33101", "3051234567"),
    
    (10002, "Miami Beach Pet Clinic", "25 Ocean Dr", "Suite 201A", "Miami Beach", "FL", "33139", "3059876543"),

    (10003, "Miller Veterinarian", "350 Miller Dr", "Suite 300", "Coral Gables", "FL", "33146", "3052345678"),

    (10004, "Miami's Best Pet Clinic", "5000 San Amaro Dr", "Office 404", "Miami", "FL", "33125", "3058765432"),

    (10005, "Tropical Vet", "1995 Albenga Ave", "Suite 1", "Miami", "FL", "33010", "3056543210")
    ])
conn.commit()

print("Clinic relation filled.")
print("Showing contents of Clinic:\n")
query = "SELECT * FROM Clinic;"
cursor.execute(query)
contents = cursor.fetchall()
print("(CLINIC NUMBER, NAME, STREET, BUILDING INFO, CITY, STATE, ZIP CODE, TELEPHONE, MANAGER NUMBER)")
for row in contents:
    print(row)
print("--------------------------------------------------------------------------------------------")

# tuples for Staff
query = """
    INSERT INTO Staff 
        (staffNo, firstName, lastName, street, buildingInfo, city, state, ZIPcode, telephone, DOB, position, salary, clinicNo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
cursor.executemany(query, [
    (1000001, "Johnny", "Appleseed", "123 Biscayne Blvd", "Building 6", "Miami", "FL", "33131", "3055551234", "1985-06-15", "Manager", 75000, 10001),
    
    (1000002, "Sarah", "Burger", "456 Brickell Ave", "Apartment 2Y", "Miami", "FL", "33129", "3055555678", "1990-02-25", "Veterinarian", 45000, 10002),
    
    (1000003, "Rick", "Sanchez", "789 Flagler St", "Unit 3B", "Miami", "FL", "33130", "3055551212", "1988-09-10", "Manager", 40000, 10003),
    
    (1000004, "LeBron", "James", "101 Coral Way", "Unit 23", "Miami", "FL", "33145", "3055551313", "1995-12-20", "Nurse", 35000, 10003),
    
    (1000005, "Morty", "Johnson","202 Little Havana Blvd", "Floor 5", "Miami", "FL", "33135", "3055551414", "1980-04-30", "Manager", 80000, 10002)
    ])
conn.commit()

print("Staff relation filled.")
print("Showing contents of Staff:\n")
query = "SELECT * FROM Staff;"
cursor.execute(query)
contents = cursor.fetchall()
print("(STAFF NUMBER, FIRST NAME, LAST NAME, STREET, BUILDING INFO, CITY, STATE, ZIP, PHONE, DOB, POSITION, SALARY, CLINIC NUMBER)")
for row in contents:
    print(row)
print("--------------------------------------------------------------------------------------------")

# tuples for Owner
query = """
    INSERT INTO Owner 
        (ownerNo, firstName, lastName, street, buildingInfo, city, state, ZIPcode, telephone)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
cursor.executemany(query, [
    (440000001, "Adam", "Black", "789 Ponce De Leon", "Apt 2", "Miami", "FL", "33133", "7863334444"),

    (440000002, "Samantha", "Red", "456 Animal St", "House", "Miami", "FL", "33132", "7865556666"),

    (440000003, "Stephen", "Green", "123 Palm Rd", "Apt 3", "Miami", "FL", "33156", "7867778888"),

    (440000004, "Alex", "Gray", "456 Juniper Cv", "Unit 5", "Miami", "FL", "33176", "7869990000"),

    (440000005, "Jerry", "Red", "789 Cedar Ct", "House", "Miami", "FL", "33186", "7861122233")
    ])
conn.commit()

print("Owner relation filled.")
print("Showing contents of Owner:\n")
query = "SELECT * FROM Owner;"
cursor.execute(query)
contents = cursor.fetchall()
print("(OWNER NUMBER, FIRST NAME, LAST NAME, STREET, BUILDINGINFO, CITY, STATE, ZIP, TELEPHONE)")
for row in contents:
    print(row)
print("--------------------------------------------------------------------------------------------")

# tuples for Pet
query = """ 
    INSERT INTO Pet 
        (petNo, petName, 
            DOB, species, breed, color,
            ownerNo, clinicNo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
cursor.executemany(query, [
    (1000000001, "Caleb", "2020-05-01", "Cat", "Persian", "White", 440000001, 10001),

    (1000000002, "JD", "2018-09-12", "Dog", "Golden Retriever", "Golden", 440000002, 10002),

    (1000000003, "Drake", "2019-06-15", "Dog", "Beagle", "Tricolor", 440000003, 10003),

    (1000000004, "MP", "2021-07-21", "Cat", "Siamese", "Brown", 440000004, 10004),

    (1000000005, "Bo", "2017-11-11", "Dog", "Labrador", "Fawn", 440000005, 10005)
    ])
conn.commit()

print("Pet relation filled")
print("Showing contents of Pet:\n")
query = "SELECT * FROM Pet;"
cursor.execute(query)
contents = cursor.fetchall()
print("(PET NUMBER, NAME, DOB, SPECIES, BREED, COLOR, OWNER NUMBER, CLINIC NUMBER")
for row in contents:
    print(row)
print("--------------------------------------------------------------------------------------------")

# tuples for Examination
query = """
    INSERT INTO Examination 
        (examNo, chiefComplaint, 
            description, dateSeen, actionsTaken,
            petNo, staffNo)
    VALUES (?, ?, ?, ?, ?, ?, ?);
        """
cursor.executemany(query, [
    (10000000001, "Fever", "Flu Test", "2024-01-01", "Prescribed meds", 1000000001, 1000001),

    (10000000002, "Physicial Checkup", "Routine Physical Exam", "2024-01-15", "All clear", 1000000002, 1000002),

    (10000000003, "Congestion", "Chest X-ray", "2024-02-01", "Prescribed meds", 1000000003, 1000003),

    (10000000004, "Vomiting", "Stomach Pump", "2024-02-10", "Dietary advice", 1000000004, 1000004),

    (10000000005, "Limping", "Leg X-ray", "2024-02-15", "Bandage applied", 1000000005, 1000005)
    ])
conn.commit()

print("Examination relation filled")
print("Showing contents of Examination:\n")
query = "SELECT * FROM Examination;"
cursor.execute(query)
contents = cursor.fetchall()
print("(EXAM NUMBER, CHIEF COMPLAINT, DESCRIPTION, DATE SEEN, ACTIONS TAKEN, PET NUMBER, STAFF NUMBER)")
for row in contents:
    print(row)
print("--------------------------------------------------------------------------------------------")
print("All relations filled")
print("--------------------------------------------------------------------------------------------")


#PART C 
#5 different transactions

#transaction 1

print("Transaction 1: Open a new Clinic\n")
query = """
    INSERT INTO Clinic (clinicNo, name, street, buildingInfo, city, state, ZIPcode, telephone)
    VALUES (10006, "MyPet Clinic", "500 Main St", "Suite 105", "Miami", "FL", "33101", "3058889999");
        """
cursor.execute(query)
conn.commit()

print("After transaction 1...\n")

query = "SELECT * FROM Clinic;"
cursor.execute(query)
conn.commit()

transaction1 = cursor.fetchall()
print("(CLINIC NUMBER, CLINIC NAME, STREET, BUILDINGINFO, CITY, STATE, ZIP, TELEPHONE)")
for row in transaction1:
    print(row)
conn.commit()

print("--------------------------------------------------------------------------------------------")

# transaction 2

print("Transaction 2: Register a new Pet to an existing Owner.\n")
query = """
        INSERT INTO Pet (petNo, petName, DOB, species, breed, color, ownerNo, clinicNo)
        VALUES (1000000006, "Bella", "2022-03-15", "Dog", "Bulldog", "White", 440000003, 10003);
    """
cursor.execute(query)
conn.commit()

print("After transaction 2...\n")

query = "SELECT * FROM Pet;"
cursor.execute(query)
conn.commit()

transaction2 = cursor.fetchall()
print("(PET NUMBER, PET NAME, DOB, SPECIES, BREED, COLOR, OWNER NUMBER, CLINIC NUMBER)")
for row in transaction2:
    print(row)
conn.commit()

print("--------------------------------------------------------------------------------------------")

# transaction 3

print("Transaction 3: Retrieve Staff information from a specific Clinic.\n")
query = """
    SELECT staffNo, firstName, lastName, position, clinicNo FROM Staff WHERE clinicNo = 10003;
        """
cursor.execute(query)
conn.commit()

print("After transaction 3...\n")

query = "SELECT staffNo, firstName, lastName, position, clinicNo FROM Staff WHERE clinicNo = 10003;"
cursor.execute(query)
conn.commit() 

transaction3 = cursor.fetchall()
print("(STAFF NUMBER, FIRST NAME, LAST NAME, POSITION, CLINIC NUMBER)")
for row in transaction3:
    print(row)
conn.commit()
print("--------------------------------------------------------------------------------------------")

# transaction 4
print("Transaction 4: Make a report of all Examinations for a specific Pet\n")
query = """ 
    SELECT * FROM Examination WHERE petNo = 1000000005;
        """
cursor.execute(query)
conn.commit() 

print("After transaction 4...\n")

query = "SELECT * FROM Examination WHERE petNo = 1000000005;"
cursor.execute(query)
conn.commit()

transaction4 = cursor.fetchall()
print("(EXAM NUMBER, CHIEF COMPLAINT, DESCRIPTION, DATE SEEN, ACTIONS TAKEN, PET NUMBER, STAFF NUMBER)")
for row in transaction4:
    print(row)
conn.commit()
print("--------------------------------------------------------------------------------------------")

# transaction5
print("Transaction 5: List all Managers for every Clinic\n")
query = """
        SELECT * FROM Staff 
        WHERE Staff.position = 'Manager';
    """
cursor.execute(query)
conn.commit()

print("After transaction 5...\n")

query = """
        SELECT * FROM Staff 
        WHERE Staff.position = 'Manager';
    """
cursor.execute(query)
conn.commit()

transaction5 = cursor.fetchall()
print("(STAFF NUMBER, FIRST NAME, LAST NAME, STREET, BUILDING INFO, CITY, STATE, ZIP, PHONE, DOB, POSITION, SALARY, CLINIC NUMBER)")
for row in transaction5:
    print(row)
conn.commit()
print("============================================================================================")

