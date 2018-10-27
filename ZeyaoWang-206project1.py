import os
import filecmp
import csv
import operator
import datetime

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.
	with open(file, 'r') as fin:
		return [dict(row) for row in csv.DictReader(fin)]


#Sort based on key/column
def mySort(data, col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	top = sorted(data, key=lambda item: item[col])[0]
	return top['First'] + ' ' + top['Last']


#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	sizes = {}
	for item in data:
		ClassName = item['Class']
		if ClassName not in sizes:
			sizes[ClassName] = 0
		sizes[ClassName] += 1
	sizes = list(sizes.items())
	return sorted(sizes, key=lambda item: item[1], reverse=True)


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	days = [0] * 32
	for item in a:
		days[int(item['DOB'].split('/')[1])] += 1
	return days.index(max(days))


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest 
# integer.  You will need to work with the DOB to find the current age in years.
	DOBs = [item['DOB'].split('/') for item in a]
	DOBs = [datetime.date(int(year), int(month), int(day)) for month, day, year in DOBs]
	# DOBs = [datetime.date(*date) for date in DOBs]
	today = datetime.date.today()
	ages = [(today - DOB).days for DOB in DOBs]
	return sum(ages) // 365 // len(ages) - 1

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	a = sorted(a, key=lambda item: item[col])
	values = [
		','.join(list(item.values())[:3])
		for item in a
	]
	with open(fileName, 'w', newline='') as fout:
		fout.writelines('\n'.join(values))
		fout.writelines('\n')


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
	total += test(type(data),type([]),40)

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
	print(filecmp.cmp('outfile.csv', 'results.csv'))
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

