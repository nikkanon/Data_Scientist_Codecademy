#Scope of the project is to look into U.S. Medical Insurance data and answer the following questions and present the findings:
#Find out the average age of the patients in the dataset.
#Analyze where a majority of the individuals are from.
#Look at the different costs between smokers vs. non-smokers.
#Figure out what the average age is for someone who has at least one child in this dataset.
#Data logic from CSV File
#age,sex,bmi,children,smoker,region,charges
#19,female,27.9,0,yes,southwest,16884.924
#18,male,33.77,1,no,southeast,1725.5523
#28,male,33,3,no,southeast,4449.462
#33,male,22.705,0,no,northwest,21984.47061
#32,male,28.88,0,no,northwest,3866.8552
#31,female,25.74,0,no,southeast,3756.6216 ...

import csv 


def average_age(age_list):
  total_age = 0
  for age in age_list:
    total_age += int(age)
  average_age = round(total_age/len(age_list)) 
  return average_age

  

with open("insurance.csv", newline = "") as insurance_csv: #use csv to import data into organized grosslists per column
  insurance_reader = csv.DictReader(insurance_csv)
  age_data_grosslist = []
  sex_data_grosslist = []
  bmi_data_grosslist = []
  children_data_grosslist = []
  smoker_data_grosslist = []
  region_data_grosslist = []
  charges_data_grosslist = []
  for row in insurance_reader:
    age_data_grosslist.append(row["age"])
    sex_data_grosslist.append(row["sex"])
    bmi_data_grosslist.append(row["bmi"])
    children_data_grosslist.append(row["children"])
    smoker_data_grosslist.append(row["smoker"])
    region_data_grosslist.append(row["region"])
    charges_data_grosslist.append(row["charges"])
  #Below are print tests that lists came out as expected
  #print(age_data_grosslist)
  #print(sex_data_grosslist)
  #print(bmi_data_grosslist)
  #print(children_data_grosslist)
  #print(smoker_data_grosslist)
  #print(region_data_grosslist)
  #print(charges_data_grosslist)

#First task from scope: to identify average age, we will use the age-gross-list extracted above and we 
#build the average_age function above

insurance_average_age = average_age(age_data_grosslist)
print("The average age in the U.S. Medical Insurance data set is {insurance_average_age} years".format(insurance_average_age = insurance_average_age))

#Second task from scope: Analyze where a majority of the individuals are from.