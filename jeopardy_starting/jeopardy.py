
#We’ve provided a csv file containing data about the game show Jeopardy! in a file named jeopardy.csv. Load the data into a DataFrame and investigate its contents. Try to print out specific columns.
#Note that in order to make this project as “real-world” as possible, we haven’t modified the data at all — we’re giving it to you exactly how we found it. As a result, this data isn’t as “clean” 
#as the datasets you normally find on Codecademy. More specifically, there’s something odd about the column names. After you figure out the problem with the column names, you may want to rename them 
#to make your life easier the rest of the project.
#In order to disply the full contents of a column, we’ve added this line of code to the top of your file:
import re
import pandas as pd
pd.set_option('display.max_colwidth', None)

#clean up the datafram
jeopardy_df = pd.read_csv('jeopardy.csv')
#print(jeopardy_df.count())
#print(jeopardy_df.head())
dict_columns = {'Show Number': 'show_number', ' Air Date': 'air_date', ' Round': 'round', ' Category': 'category', ' Value': 'value', ' Question': 'question', ' Answer': 'answer'}
jeopardy_df.rename(columns=dict_columns, inplace=True)
#print(jeopardy_df.head())


#Write a function that filters the dataset for questions that contains all of the words in a list of words. For example, when the list ["King", "England"] was passed to our function, 
#the function returned a DataFrame of 152 rows. Every row had the strings "King" and "England" somewhere in its " Question".
#Note that in this example, we found 152 rows by filtering the entire dataset. You can download the entire dataset at the start or end of this project. 
#The dataset used on Codecademy is only a fraction of the dataset so you won’t find as many rows.
#Test your function by printing out the column containing the question of each row of the dataset.

#Solution idea: do lamba function that takes a list of words and check if they exist in sentence - use all()-function in combition with word in question for word in list

words_list = ["King", "England"]
words_in_quest_series = jeopardy_df.question.apply(lambda question: question if all(word in question for word in words_list) else None)
remove_none_words_in_question = words_in_quest_series.dropna()
#print(remove_none_words_in_question.count())

#Test your original function with a few different sets of words to try to find some ways your function breaks. Edit your function so it is more robust.
#For example, think about capitalization. We probably want to find questions that contain the word "King" or "king".
#You may also want to check to make sure you don’t find rows that contain substrings of your given words. For example, our function found a question that 
#didn’t contain the word "king", however it did contain the word "viking" — it found the "king" inside "viking". Note that this also comes with some 
#drawbacks — you would no longer find questions that contained words like "England's".

#Solution idea: improved function to also capture lower and upper case scenarios - idea; transform the questions in the lambda fuction to lower case and change input list to 
#lower case words

words_list_2 = ["king", "england"]
words_in_quest_series_2 = jeopardy_df.question.apply(lambda question: question if all(word in question.lower() for word in words_list_2) else None)
remove_none_words_in_question_2 = words_in_quest_series_2.dropna()
#print(remove_none_words_in_question_2.count())


#We may want to eventually compute aggregate statistics, like .mean() on the " Value" column. But right now, the values 
#in that column are strings. Convert the " Value" column to floats. If you’d like to, you can create a new column with the float values.
#Now that you can filter the dataset of question, use your new column that contains the float values of each question to find the “difficulty” 
#of certain topics. For example, what is the average value of questions that contain the word "King"?
#Make sure to use the dataset that contains the float values as the dataset you use in your filtering function.
#Solution idea first question: create new column 'float_value' by applying a lambda function utilizing RegEx and the \D to return match where the string DOES NOT contain digits. Weak point; RegEx most likely not fastest compute.
#seems to be 'None' values as well in the data hence casting float does not work directly. Need to add if statement handling those Final Jeopardy! questions setting their value to 0.
jeopardy_df['float_value'] = jeopardy_df.value.apply(lambda value: float(re.sub('\D', '', value)) if value != "None" else 0)
#print(jeopardy_df.head())

#Solution idea second question: filter out the rows which have king in the question. Then after that calculate mean of float_value column
filtered_jeopoday_df = jeopardy_df[(jeopardy_df.question == words_in_quest_series_2)]
mean_value_filtered = filtered_jeopoday_df.float_value.mean()
print(mean_value_filtered)





