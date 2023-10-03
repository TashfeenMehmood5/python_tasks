import mysql.connector

class HospitalManagementSystem:
    def __init__(self):
        # Initialize the MySQL connection
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="hms"
        )
        self.cursor = self.db.cursor()

        # Create tables if they don't exist
        self.create_patients_table()
        self.create_doctors_table()

    def create_patients_table(self):
        # Create the patients table if it doesn't exist
        create_query = '''DELETE FROM patients WHERE patient_ID = 9 '''
        
        # ''' 
        #        UPDATE patients SET Address = 'abcdefghgsh' WHERE patient_ID  = 1

        #   '''
         
        # '''INSERT INTO patients 
        #      (Department, DoctorName, Name, Age, Gender, Address, RoomNumber)
        #      VALUES 
        #      ('Oncologist', 'Dr. Molly', ' Ricky ',53, 'male', '162 Main St', '44')
        #    '''
        
        # '''
        # CREATE TABLE IF NOT EXISTS patients (
        #     patient_ID INT AUTO_INCREMENT PRIMARY KEY,
        #     Department VARCHAR(255),
        #     DoctorName VARCHAR(255),
        #     Name VARCHAR(255),
        #     Age INT,
        #     Gender VARCHAR(10),
        #     Address VARCHAR(255),
        #     RoomNumber VARCHAR(20)
        # )
        # '''
        self.cursor.execute(create_query)
        self.db.commit()

    def create_doctors_table(self):
        # Create the doctors table if it doesn't exist
        create_query = '''
               UPDATE doctors SET Address ='Islamabad' WHERE doctor_ID  = 2

          '''
        
        # ''' INSERT INTO doctors (Department, Name, Address)
        #                      VALUES ('Oncologist', 'Dr. Moly', '549 Oak St')
        #                   '''
        # '''
        # CREATE TABLE IF NOT EXISTS doctors (
        #     doctor_ID INT AUTO_INCREMENT PRIMARY KEY,
        #     Department VARCHAR(255),
        #     Name VARCHAR(255),
        #     Address VARCHAR(255)
        # )
        # '''
        self.cursor.execute(create_query)
        self.db.commit()

    def add_patient(self):
        # Gather patient data
        department = input("Enter Department: ")
        doctor_name = input("Enter Doctor's Name: ")
        name = input("Enter Patient's Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        address = input("Enter Address: ")
        room_number = input("Enter Room Number: ")

        # Insert patient data into the database
        insert_query = '''
        INSERT INTO patients (Department, DoctorName, Name, Age, Gender, Address, RoomNumber)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        patient_data = (department, doctor_name, name, age, gender, address, room_number)
        self.cursor.execute(insert_query, patient_data)
        self.db.commit()
        print("Patient added successfully!")

    def display_patient(self, patient_ID):
        # Fetch patient data based on patient_ID
        select_query = "SELECT * FROM patients WHERE patient_ID = %s"
        self.cursor.execute(select_query, (patient_ID,))
        patient = self.cursor.fetchone()

        if patient:
            print("Patient Details:")
            print("Patient ID:", patient[0])
            print("Department:", patient[1])
            print("Doctor's Name:", patient[2])
            print("Name:", patient[3])
            print("Age:", patient[4])
            print("Gender:", patient[5])
            print("Address:", patient[6])
            print("Room Number:", patient[7])
        else:
            print("Patient not found")

    def close(self):
        # Close the MySQL connection
        self.cursor.close()
        self.db.close()

if __name__ == "__main__":
    hospital_system = HospitalManagementSystem()
    print("Welcome to Quaid-e-Azam Hospital Management System")

    while True:
        print("1. Add Patient")
        print("2. Display Patient")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hospital_system.add_patient()
        elif choice == "2":
            patient_ID = input("Enter patient ID: ")
            hospital_system.display_patient(patient_ID)
        elif choice == "3":
            hospital_system.close()
            print("Goodbye stay fit stay healthy!")
            break
        else:
            print("Invalid choice. Please try again.")




















    # def display_all_patients(self):
    #     # Fetch all patients from the database
    #     select_query = "SELECT * FROM patients"
    #     self.cursor.execute(select_query)
    #     patients_data = self.cursor.fetchall()

    #     if patients_data:
    #         print("Patients List:")
    #         for patient in patients_data:
    #             print("Patient ID:", patient[0])
    #             print("Department:", patient[1])
    #             print("Doctor Name:", patient[2])
    #             print("Name:", patient[3])
    #             print("Age:", patient[4])
    #             print("Gender:", patient[5])
    #             print("Address:", patient[6])
    #             print("Room Number:", patient[7])
    #             print("-" * 40)
    #     else:
    #         print("No patients found.")
    
    # def display_all_doctors(self):
    #     # Fetch all doctors from the database
    #     select_query = "SELECT * FROM doctors"
    #     self.cursor.execute(select_query)
    #     doctors_data = self.cursor.fetchall()

    #     if doctors_data:
    #         print("Doctors List:")
    #         for doctor in doctors_data:
    #             print("Doctor ID:", doctor[0])
    #             print("Department:", doctor[1])
    #             print("Name:", doctor[2])
    #             print("Address:", doctor[3])
    #             print("-" * 40)
    #     else:
    #         print("No doctors found.")