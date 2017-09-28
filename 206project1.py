<<<<<<< HEAD
##Katarina Mazanka, katmazan, https://github.com/katmazan/206-1.git ##trying to add more things to git
import os
import filecmp
=======
import os
>>>>>>> 0fe91fb2932188c92939fafa45abb5f06d645ce5

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
<<<<<<< HEAD

	list = []
	dict = {}
	file_object = open(file, "r")
	for w in file_object:
		list += w.split()
	string = list[0]
	
	list1 = string.split(',')
	dict_list = []
	temp_dic = {}
	i = 0
	j = 1
	##for item in list[j]:
	for line in list[1:]:
		item = line
		temp_list = item.split(',')
		i = 0
		for thing in list1:
		##item = list[1]
			temp_string = temp_list[i]
	
	##temp_list = item.split(',')
	
			temp_dic[thing] = temp_string
			i = i + 1

		dict_list.append(temp_dic.copy())
			
		j = j + 1
	return dict_list
	
	


		

	
=======
	pass
>>>>>>> 0fe91fb2932188c92939fafa45abb5f06d645ce5

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
<<<<<<< HEAD
	
	#Your code here:
	
	newlist = sorted(data, key=lambda k: k[col])
	return str(newlist[0]['First']) + " "  + str(newlist[0]['Last'])
=======

	#Your code here:
	pass

>>>>>>> 0fe91fb2932188c92939fafa45abb5f06d645ce5
#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
<<<<<<< HEAD
	senior_count = 0
	junior_count = 0
	soph_count = 0
	fresh_count = 0
	#Your code here:
	for item in data:
		if item['Class'] == 'Senior':
			senior_count = senior_count + 1
		if item['Class'] == 'Junior':
			junior_count = junior_count + 1
		if item['Class'] == 'Sophomore':
			soph_count = soph_count + 1
		if item['Class'] == 'Freshman':
			fresh_count = fresh_count + 1
	class_list = []
	senior_tuple = ('Senior', senior_count)
	junior_tuple = ('Junior', junior_count)
	soph_tuple = ('Sophomore', soph_count)
	fresh_tuple = ('Freshman', fresh_count)
	class_list.append(senior_tuple)
	class_list.append(junior_tuple)
	class_list.append(soph_tuple)
	class_list.append(fresh_tuple)
	newlist = sorted(class_list, key=lambda k: k[1], reverse = True)
	return newlist
=======

	#Your code here:
	pass


>>>>>>> 0fe91fb2932188c92939fafa45abb5f06d645ce5

# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
<<<<<<< HEAD
	
	#Your code here:
	list_days = []
	for item in a:
		s = str(item['DOB'])
		s = s.partition('/')[-1].rpartition('/')[0]
		s = int(s)
		list_days.append(s)
	
 	
	return(max(set(list_days), key=list_days.count))
=======

	#Your code here:
	pass

>>>>>>> 0fe91fb2932188c92939fafa45abb5f06d645ce5

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
<<<<<<< HEAD
	item_total = 0
	age_total = 0
	import datetime
	now = datetime.datetime.now()
	age_list = []
	for item in a:
		age_year = str(item['DOB'][-4:])
		
		age = int(now.year) - int(age_year)
	
		age_list.append(age)
		item_total = item_total + 1
	for item in age_list:
		age_total = age_total + item
	age_avereage = 0
	age_avereage = age_total / item_total
	
	return (round(age_avereage))


	##print(age_list)
=======
	pass
>>>>>>> 0fe91fb2932188c92939fafa45abb5f06d645ce5

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
<<<<<<< HEAD
	
	newlist = sorted(a, key=lambda n: n[col])
	file_object = open(fileName, "w")
	for item in newlist:
		for col in item:
			if col == 'First':
				wr_item = str(item[col])
				wr_item = wr_item + ','
			
				file_object.write(wr_item)
			if col == 'Last':
				wr_item = str(item[col])
				wr_item = wr_item + ','
				file_object.write(wr_item)
			if col == 'Email':
				wr_item = str(item[col])
				
				file_object.write(wr_item)
			
		file_object.write('\n')
	print(file_object)
	
	file_object.close()
	print(file_object)
	



=======
	pass
>>>>>>> 0fe91fb2932188c92939fafa45abb5f06d645ce5



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
<<<<<<< HEAD
	total += test(type(data),type([]),40)
=======
	total += test(type(data),type([]),35)
>>>>>>> 0fe91fb2932188c92939fafa45abb5f06d645ce5
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

