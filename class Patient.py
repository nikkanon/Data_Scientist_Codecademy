class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  
  def estimated_insurance_costs(self):
    self.estimated_cost =  250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print("{name}'s estimated insurance costs is {estimated_cost} dollars.".format(name = self.name, estimated_cost = self.estimated_cost))
  
  def update_age(self, new_age):
    try:
      self.age = int(new_age)
      print("{name} is now {age} years old.".format(name = self.name, age = self.age))
      self.estimated_insurance_costs()
    except ValueError:
        print ("Non numeric value")
   
  
  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print("{name} has {num_of_children} child.".format(name = self.name, num_of_children = self.num_of_children))
      self.estimated_insurance_costs()
    elif self.num_of_children == 0:
      print("{name} have no children.".format(name = self.name))
      self.estimated_insurance_costs()
    else:
      print("{name} has {num_of_children} children.".format(name = self.name, num_of_children = self.num_of_children))
      self.estimated_insurance_costs()

  def patient_profile(self):
    self.patient_information = {self.name : [self.name, self.age, self.sex, self.bmi, self.num_of_children, self.smoker]}
    return self.patient_information

  
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
#print(patient1.name)
#print(patient1.age)
#print(patient1.sex)
#print(patient1.bmi)
#print(patient1.num_of_children)
#print(patient1.smoker)
#patient1.estimated_insurance_costs()
patient1.update_age("hej")
#patient1.update_num_children(1)
#print(patient1.patient_profile())