
'''
	This script finds the numbers in a set that add up to one hundred million.
	This puzzle is taken from the OpenGarden hiring webpage.

	http://opengarden.com/we_are_hiring.html
'''

import math

censusCounts = [18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833, 3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]

#	Divide the odd and even numbers into two buckets.
evenCounts = list()
oddCounts = list()

#	Original Numbers
originalPair = dict()

#	Count the number of odds/even
numberOfOddCensusResults = 0
numberOfEvenCensusResults = 0


#	unique even list
uniqueEvenList = list()

#	Numbers sorted by last digit
numberSortedByLastDigit = dict()

#	
#	Add the evens
#

def prepareNumbersForSummation():
	for count in censusCounts:

		if (count % 2 == 1):
			oddCounts.append(count)
		else:
			evenCounts.append(count)


	numberOfOddCensusResults = len(oddCounts)
	numberOfEvenCensusResults = len(evenCounts)

	print str(numberOfOddCensusResults) + " odd numbers"
	print str(numberOfEvenCensusResults) + " even numbers"

	#	Combine the odd numbers into pairs
	for i in range(numberOfOddCensusResults):
		for j in xrange(i, numberOfOddCensusResults):
			combination = oddCounts[i] + oddCounts[j]
			evenCounts.append(combination)
			originalPair[combination] = [oddCounts[i], oddCounts[j]]

	#	Count the evens again because we've changed them
	numberOfEvenCensusResults = len(evenCounts)

	print "There are " + str(numberOfEvenCensusResults) + " evens after consolidating odds."

#	This function adds groups of evens to try and find a sum of 10 million
def findCombinationsOfTenMillion():
	for i in range(numberOfOddCensusResults):
		for j in range(i, numberOfOddCensusResults):
			pass

#	Sort into buckets
def sortIntoBuckets():
	for number in evenCounts:
		lastDigit = number % 10

		if not lastDigit in numberSortedByLastDigit:
			numberSortedByLastDigit[lastDigit] = list()

		numberSortedByLastDigit[lastDigit].append(number)

def sortIntoFinalBuckets():
	evenBases = [0, 2, 4, 6, 8]




def main():
	#prepareNumbersForSummation()
	#sortIntoBuckets()

	#for key in numberSortedByLastDigit:
	#	print "[" + str(key) + "] : " + str(numberSortedByLastDigit[key])

	sumOfAll = 0
	average = 0

	for number in censusCounts:
		sumOfAll += number

	average = sumOfAll / len(censusCounts)

	print average

main()


			