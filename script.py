# 1) Create constructor for a Patient class.
class Patient:
    def __init__(self, name, age, sex, bmi, num_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_children = num_children
        self.smoker = smoker

    # 3) Create first method estimated_insurance_cost()
    # which takes our instance’s parameters (representing our patient’s info) and returns their expected yearly medical fees.
    # formula -> estimated_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500
    def estimated_insurance_cost(self):
        estimated_cost = (250 * self.age) - (128 * self.sex) + (370 * self.bmi) + (425 * self.num_children) + (24000 * self.smoker) - 12500 
        print(f"{self.name}'s estimated insurance costs is {estimated_cost} dollars.")
    
    # 5) create an update_age() method.
    def update_age(self, new_age):
        self.age = new_age
        print(f"{self.name} is now {self.age} years old.")
        # 7) Check if estimated_insurance_cost changes because of new age
        self.estimated_insurance_cost()
    
    # 8) update method that modifies the num_of_children parameter
    def update_num_children(self, new_num_children):
        self.num_children = new_num_children
        # 10) Make print statement grammaticaly correct
        if self.num_children == 1:
            print(f"{self.name} has {self.num_children} child.")
        else:
            print(f"{self.name} has {self.num_children} children.")
        # 11) Check estimated_insurance_cost after change in num_children
        self.estimated_insurance_cost()
    
    # 12) Define a method that builds a dictionary called patient_information to hold all of our patient’s information.
    def patient_profile(self):
        patient_information = {"Name": self.name,
                               "Age": self.age,
                               "Sex": self.sex,
                               "BMI": self.bmi,
                               "Number Of Children": self.num_children,
                               "Smoker": self.smoker}
        return patient_information

# 2) Test constructor for a Patient
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
# 4) Test estimated_insurance_cost method
patient1.estimated_insurance_cost()
# 6) Test update_age() method
patient1.update_age(26)
# 9) Test update_num_children method
patient1.update_num_children(1)
# 13) Test patient_profile method
print(patient1.patient_profile())