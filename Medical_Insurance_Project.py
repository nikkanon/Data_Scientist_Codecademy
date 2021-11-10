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


def average_age(age_list): #return average age of age list
  total_age = 0
  for age in age_list:
    total_age += int(age)
  average_age = round(total_age/len(age_list)) 
  return average_age

def occur_origin_dict(origin_list): #returns dictionary with {region : occurances of region in data}
  region_popular_dict = {}
  for region in origin_list:
    region_popular_dict.update({region : origin_list.count(region)})
  return region_popular_dict

def most_popular_region(occur_dict): #returns most popular region from dict {region : occurances of region in data}
  popular_region = ""
  amount_of_ppl = 0
  for key in occur_dict:
    if occur_dict[key] > amount_of_ppl:
      amount_of_ppl = occur_dict[key]
      popular_region = key
    else:
      continue
  return popular_region

def average_cost_smoker(smoker_list, charges_list): #returns average cost for smokers in the data set
  total_cost_smoker = 0
  amount_of_smokers = 0
  for i in range(len(smoker_list)):
    if smoker_list[i] == "yes":
      total_cost_smoker += round(float(charges_list[i]))
      amount_of_smokers += 1
    else:
      continue
  return total_cost_smoker/amount_of_smokers

def average_cost_non_smoker(smoker_list, charges_list): #returns average cost for non-smokers in the data set
  total_cost_nonsmoker = 0
  amount_of_non_smokers = 0
  for i in range(len(smoker_list)):
    if smoker_list[i] == "no":
      total_cost_nonsmoker += round(float(charges_list[i]))
      amount_of_non_smokers += 1
    else:
      continue
  return total_cost_nonsmoker/amount_of_non_smokers

#use csv to import data using DictReader then iterate through csv-file and add data into organized grosslists per column to allow combination of data for analytics to solve our project scope.
with open("insurance.csv", newline = "") as insurance_csv: 
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
#Solution idea: build the average_age function above that returns average age. Then do a print statement.

insurance_average_age = average_age(age_data_grosslist)
print("The average age in the U.S. Medical Insurance data set is {insurance_average_age} years".format(insurance_average_age = insurance_average_age))

#Second task from scope: Analyze where a majority of the individuals are from. We can use our region_data_grosslist for that.
#Solution idea/discussion: build a function that builds a dictionary key = region, value = occurance in region_data_grosslist. Use dictionary to identify most popular place of origin - and dictionary can be used later for other analysis.
region_occur_dict = occur_origin_dict(region_data_grosslist)
#print(region_occur_dict)

most_popular_region = most_popular_region(region_occur_dict)
print("Majority of the individuals are from {most_popular_region} region a total of {amount_of_ppl} people in the data set".format(most_popular_region = most_popular_region, amount_of_ppl = region_occur_dict[most_popular_region]))

#Third task from scope: Look at the different costs between smokers vs. non-smokers.
#Solution idea/discussions: Hard to isolate the cost impact for only smoking - the cost per individual is aggregated result of all parameters. However a indication can be given by doing a average difference value accross data set
#smoker vs non-smoker. Build function (or functions?) returning average cost for smoker and average cost for non-smoker; utilize the result from the functions to visualize the impact on the cost if you choose 
#to be a smoker

average_cost_smoking = round(average_cost_smoker(smoker_data_grosslist, charges_data_grosslist))
#print(average_cost_smoking)
average_cost_non_smoking = round(average_cost_non_smoker(smoker_data_grosslist, charges_data_grosslist))
#print(average_cost_non_smoking)



