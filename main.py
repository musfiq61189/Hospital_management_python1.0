import datetime


# Class Definitions
class Patient:
    def __init__(self, patient_id, name, age, gender, diagnosis):
        """Initialize Patient with ID, name, age, gender, and diagnosis."""
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis


class Staff:
    def __init__(self, staff_id, name, role, shift):
        """Initialize Staff with ID, name, role, and shift."""
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.shift = shift


class Doctor:
    def __init__(self, doctor_id, name, designation, phone):
        """Initialize Doctor with ID, name, designation, and phone."""
        self.doctor_id = doctor_id
        self.name = name
        self.designation = designation
        self.phone = phone


class Inventory:
    def __init__(self, item_id, item_name, quantity):
        """Initialize Inventory with ID, name, and quantity."""
        self.item_id = item_id
        self.item_name = item_name
        self.quantity = quantity


class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time):
        """Initialize Appointment with ID, patient ID, doctor ID, date, and time."""
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time


# Main Hospital Management System
class HospitalManagementSystem:
    def __init__(self):
        """Initialize lists for managing patients, staff, doctors, inventory, and appointments."""
        self.patients = []
        self.staff = []
        self.doctors = []
        self.inventory = []
        self.appointments = []
        self.admin_password = "12345"  # Default password for admin login

    # Utility: Display Decorated Header
    def display_header(self, text):
        """Display a styled header for section titles."""
        print("\n" + "=" * 50)
        print(f"{text.center(50)}")
        print("=" * 50)

    # Utility: Check for Duplicates
    def _check_duplicate(self, items, key, value):
        """Check if an item with the given key-value pair exists in a list."""
        return any(getattr(item, key) == value for item in items)

    # Patient Methods
    def add_patient(self, patient):
        """Add a new patient if the ID is unique."""
        if self._check_duplicate(self.patients, "patient_id", patient.patient_id):
            print("Error: Patient with this ID already exists!")
        else:
            self.patients.append(patient)
            print("\n✅ Patient added successfully!")

    def search_patient_by_name(self, name):
        """Search and display patients by name."""
        self.display_header(f"Search Results for '{name}'")
        found = [p for p in self.patients if name.lower() in p.name.lower()]
        if found:
            for patient in found:
                print(vars(patient))
        else:
            print("No patients found with that name.")

    def delete_patient(self, patient_id):
        """Delete a patient by ID."""
        self.patients = [p for p in self.patients if p.patient_id != patient_id]
        print("\n✅ Patient deleted successfully!")

    # Staff Methods
    def add_staff(self, staff):
        """Add a new staff member if the ID is unique."""
        if self._check_duplicate(self.staff, "staff_id", staff.staff_id):
            print("Error: Staff with this ID already exists!")
        else:
            self.staff.append(staff)
            print("\n✅ Staff added successfully!")

    def list_staff_by_role(self, role):
        """List all staff members with a specific role."""
        self.display_header(f"Staff Members with Role: {role}")
        found = [s for s in self.staff if s.role.lower() == role.lower()]
        if found:
            for staff in found:
                print(vars(staff))
        else:
            print(f"No staff members found with role '{role}'.")

    def delete_staff(self, staff_id):
        """Delete a staff member by ID."""
        self.staff = [s for s in self.staff if s.staff_id != staff_id]
        print("\n✅ Staff deleted successfully!")

    # Doctor Methods
    def add_doctor(self, doctor):
        """Add a new doctor if the ID is unique."""
        if self._check_duplicate(self.doctors, "doctor_id", doctor.doctor_id):
            print("Error: Doctor with this ID already exists!")
        else:
            self.doctors.append(doctor)
            print("\n✅ Doctor added successfully!")

    def delete_doctor(self, doctor_id):
        """Delete a doctor by ID."""
        self.doctors = [doc for doc in self.doctors if doc.doctor_id != doctor_id]
        print("\n✅ Doctor deleted successfully!")

    def edit_doctor(
        self, doctor_id, new_name=None, new_designation=None, new_phone=None
    ):
        """Edit doctor details."""
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

    def list_doctors_by_designation(self, designation):
        """List all doctors with a specific designation."""
        self.display_header(f"Doctors with Designation: {designation}")
        found = [
            d for d in self.doctors if d.designation.lower() == designation.lower()
        ]
        if found:
            for doctor in found:
                print(vars(doctor))
        else:
            print(f"No doctors found with designation '{designation}'.")

    # Inventory Methods
    def add_inventory(self, item):
        """Add a new inventory item if the ID is unique."""
        if self._check_duplicate(self.inventory, "item_id", item.item_id):
            print("Error: Inventory item with this ID already exists!")
        else:
            self.inventory.append(item)
            print("\n✅ Inventory item added successfully!")

    def update_inventory(self, item_id, new_quantity=None):
        """Update inventory item quantity."""
        for item in self.inventory:
            if item.item_id == item_id:
                if new_quantity is not None:
                    item.quantity = new_quantity
                print("\n✅ Inventory item updated successfully!")
                return
        print("\n❌ Inventory item not found!")

    def delete_inventory(self, item_id):
        """Delete an inventory item by ID."""
        self.inventory = [item for item in self.inventory if item.item_id != item_id]
        print("\n✅ Inventory item deleted successfully!")

    def list_low_stock_items(self, threshold):
        """List inventory items with stock below a certain threshold."""
        self.display_header(f"Inventory Items with Stock Below {threshold}")
        low_stock = [item for item in self.inventory if item.quantity < threshold]
        if low_stock:
            for item in low_stock:
                print(vars(item))
        else:
            print("No items found with low stock.")

    # Appointment Methods
    def add_appointment(self, appointment):
        """Add a new appointment if the ID is unique."""
        if self._check_duplicate(
            self.appointments, "appointment_id", appointment.appointment_id
        ):
            print("Error: Appointment with this ID already exists!")
        else:
            self.appointments.append(appointment)
            print("\n✅ Appointment added successfully!")

    def list_appointments(self):
        """Display all appointments."""
        self.display_header("List of Appointments")
        for appointment in self.appointments:
            print(vars(appointment))

    def cancel_appointment(self, appointment_id):
        """Cancel an appointment by ID."""
        self.appointments = [
            app for app in self.appointments if app.appointment_id != appointment_id
        ]
        print("\n✅ Appointment canceled successfully!")


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
        print("2. Search Patient by Name")
        print("3. Add Staff")
        print("4. List Staff by Role")
        print("5. Add Doctor")
        print("6. List Doctors by Designation")
        print("7. Add Inventory")
        print("8. List Low Stock Items")
        print("9. Add Appointment")
        print("10. Cancel Appointment")
        print("11. Exit")

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
            name = input("Enter patient name to search: ")
            hms.search_patient_by_name(name)

        elif choice == 3:
            staff_id = int(input("Enter staff ID: "))
            name = input("Enter staff name: ")
            role = input("Enter staff role: ")
            shift = input("Enter staff shift: ")
            hms.add_staff(Staff(staff_id, name, role, shift))

        elif choice == 4:
            role = input("Enter role to filter staff by: ")
            hms.list_staff_by_role(role)

        elif choice == 5:
            doctor_id = int(input("Enter doctor ID: "))
            name = input("Enter doctor name: ")
            designation = input("Enter doctor designation: ")
            phone = input("Enter doctor phone: ")
            hms.add_doctor(Doctor(doctor_id, name, designation, phone))

        elif choice == 6:
            designation = input("Enter designation to filter doctors by: ")
            hms.list_doctors_by_designation(designation)

        elif choice == 7:
            item_id = int(input("Enter item ID: "))
            item_name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            hms.add_inventory(Inventory(item_id, item_name, quantity))

        elif choice == 8:
            threshold = int(input("Enter stock threshold: "))
            hms.list_low_stock_items(threshold)

        elif choice == 9:
            appointment_id = int(input("Enter appointment ID: "))
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            hms.add_appointment(
                Appointment(appointment_id, patient_id, doctor_id, date, time)
            )

        elif choice == 10:
            appointment_id = int(input("Enter appointment ID to cancel: "))
            hms.cancel_appointment(appointment_id)

        elif choice == 11:
            print("\nExiting the system. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
