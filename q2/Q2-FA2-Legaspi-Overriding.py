class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount
    
class SeniorPatient(Patient):
    discount_rate = 0.20

    def calculate_bill(self):
        return super().calculate_bill() * (1 - self.discount_rate)


class PhilHealthPatient(Patient):
    discount_rate = 0.15

    def calculate_bill(self):
        return super().calculate_bill() * (1 - self.discount_rate)

regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Penduko", 15000)

patients = [regular_patient, senior_patient, philhealth_patient]

print("\nHospital Billing System\n")
print("--------------------------\n")

for people in patients:
    print(f"Patient Name: {people.get_name()}")
    print(f"Original Bill: {people.get_bill_amount():,.2f}")
    print(f"Final Bill: {people.calculate_bill():,.2f}\n")