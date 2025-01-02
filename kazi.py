import datetime

# Class Definitions
class Patient:
    def __init__(self, patient_id, name, age, gender, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

class Staff:
    def __init__(self, staff_id, name, role, shift):
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.shift = shift

class Doctor:
    def __init__(self, doctor_id, name, designation, phone):
        self.doctor_id = doctor_id
        self.name = name
        self.designation = designation
        self.phone = phone

class Inventory:
    def __init__(self, item_id, item_name, quantity):
        self.item_id = item_id
        self.item_name = item_name
        self.quantity = quantity

class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

# Main Hospital Management System
class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.staff = []
        self.doctors = []
        self.inventory = []
        self.appointments = []
        self.admin_password = "12345"

    # Utility: Display Decorated Header
    def display_header(self, text):
        print("\n" + "=" * 50)
        print(f"{text.center(50)}")
        print("=" * 50)

    # Patient Methods
    def add_patient(self, patient):
        if self._check_duplicate(self.patients, "patient_id", patient.patient_id):
            print("Error: Patient with this ID already exists!")
        else:
            self.patients.append(patient)
            print("\n✅ Patient added successfully!")

    def delete_patient(self, patient_id):
        self.patients = [p for p in self.patients if p.patient_id != patient_id]
        print("\n✅ Patient deleted successfully!")

    # Staff Methods
    def add_staff(self, staff):
        if self._check_duplicate(self.staff, "staff_id", staff.staff_id):
            print("Error: Staff with this ID already exists!")
        else:
            self.staff.append(staff)
            print("\n✅ Staff added successfully!")

    def delete_staff(self, staff_id):
        self.staff = [s for s in self.staff if s.staff_id != staff_id]
        print("\n✅ Staff deleted successfully!")

    # Doctor Methods
    def add_doctor(self, doctor):
        if self._check_duplicate(self.doctors, "doctor_id", doctor.doctor_id):
            print("Error: Doctor with this ID already exists!")
        else:
            self.doctors.append(doctor)
            print("\n✅ Doctor added successfully!")

    def delete_doctor(self, doctor_id):
        self.doctors = [doc for doc in self.doctors if doc.doctor_id != doctor_id]
        print("\n✅ Doctor deleted successfully!")

    def edit_doctor(self, doctor_id, new_name=None, new_designation=None, new_phone=None):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                if new_name:
                    doctor.name = new_name
                if new_designation:
                    doctor.designation = new_designation
                if new_phone:
                    doctor.phone = new_phone
                print("\n✅ Doctor details updated successfully!")
                return
        print("\n❌ Doctor not found!")

    # Inventory Methods
    def add_inventory(self, item):
        if self._check_duplicate(self.inventory, "item_id", item.item_id):
            print("Error: Inventory item with this ID already exists!")
        else:
            self.inventory.append(item)
            print("\n✅ Inventory item added successfully!")

    def update_inventory(self, item_id, new_quantity=None):
        for item in self.inventory:
            if item.item_id == item_id:
                if new_quantity is not None:
                    item.quantity = new_quantity
                print("\n✅ Inventory item updated successfully!")
                return
        print("\n❌ Inventory item not found!")

    def delete_inventory(self, item_id):
        self.inventory = [item for item in self.inventory if item.item_id != item_id]
        print("\n✅ Inventory item deleted successfully!")

    # Appointment Methods
    def add_appointment(self, appointment):
        if self._check_duplicate(self.appointments, "appointment_id", appointment.appointment_id):
            print("Error: Appointment with this ID already exists!")
        else:
            self.appointments.append(appointment)
            print("\n✅ Appointment added successfully!")

    def list_appointments(self):
        self.display_header("List of Appointments")
        for appointment in self.appointments:
            print(vars(appointment))

    # Utility Methods
    def _check_duplicate(self, items, key, value):
        return any(getattr(item, key) == value for item in items)

    def show_all(self):
        self.display_header("Patients")
        for patient in self.patients:
            print(vars(patient))

        self.display_header("Staff")
        for staff in self.staff:
            print(vars(staff))

        self.display_header("Doctors")
        for doctor in self.doctors:
            print(vars(doctor))

        self.display_header("Inventory")
        for item in self.inventory:
            print(vars(item))

# Main Function with Login
def main():
    hms = HospitalManagementSystem()
    hms.display_header("Welcome to the Hospital Management System")

    # Login Process
    for _ in range(3):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "jadu" and password == hms.admin_password:
            print("\n✅ Login successful!")
            break
    else:
        print("\n❌ Too many failed attempts. Exiting.")
        return

    # Main Menu
    while True:
        hms.display_header("Main Menu")
        print("1. Add Patient")
        print("2. Add Staff")
        print("3. Add Doctor")
        print("4. Add Inventory")
        print("5. Add Appointment")
        print("6. Show All Information")
        print("7. List All Appointments")
        print("8. Delete Patient")
        print("9. Delete Staff")
        print("10. Edit Doctor")
        print("11. Update Inventory")
        print("12. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            hms.display_header("Add Patient")
            patient_id = int(input("Enter patient ID: "))
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            diagnosis = input("Enter patient diagnosis: ")
            hms.add_patient(Patient(patient_id, name, age, gender, diagnosis))

        elif choice == 2:
            hms.display_header("Add Staff")
            staff_id = int(input("Enter staff ID: "))
            name = input("Enter staff name: ")
            role = input("Enter staff role: ")
            shift = input("Enter staff shift: ")
            hms.add_staff(Staff(staff_id, name, role, shift))

        elif choice == 3:
            hms.display_header("Add Doctor")
            doctor_id = int(input("Enter doctor ID: "))
            name = input("Enter doctor name: ")
            designation = input("Enter doctor designation: ")
            phone = input("Enter doctor phone: ")
            hms.add_doctor(Doctor(doctor_id, name, designation, phone))

        elif choice == 4:
            hms.display_header("Add Inventory")
            item_id = int(input("Enter item ID: "))
            item_name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            hms.add_inventory(Inventory(item_id, item_name, quantity))

        elif choice == 5:
            hms.display_header("Add Appointment")
            appointment_id = int(input("Enter appointment ID: "))
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            hms.add_appointment(Appointment(appointment_id, patient_id, doctor_id, date, time))

        elif choice == 6:
            hms.show_all()

        elif choice == 7:
            hms.list_appointments()

        elif choice == 8:
            hms.display_header("Delete Patient")
            patient_id = int(input("Enter patient ID to delete: "))
            hms.delete_patient(patient_id)

        elif choice == 9:
            hms.display_header("Delete Staff")
            staff_id = int(input("Enter staff ID to delete: "))
            hms.delete_staff(staff_id)

        elif choice == 10:
            hms.display_header("Edit Doctor")
            doctor_id = int(input("Enter doctor ID to edit: "))
            new_name = input("Enter new name (leave blank to skip): ")
            new_designation = input("Enter new designation (leave blank to skip): ")
            new_phone = input("Enter new phone (leave blank to skip): ")
            hms.edit_doctor(doctor_id, new_name, new_designation, new_phone)

        elif choice == 11:
            hms.display_header("Update Inventory")
            item_id = int(input("Enter inventory item ID to update: "))
            new_quantity = int(input("Enter new quantity: "))
            hms.update_inventory(item_id, new_quantity)

        elif choice == 12:
            print("\nExiting the system. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
