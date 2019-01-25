import unittest


def merge_ranges(meetings):

	scheduleTimes = [False, False, False, False, False, False, False, False, False, False, False, False, False]
	
	for x in meetings:
		startTime = x[0]
		endTime = x[1]
		
		for x in range(startTime, endTime):
			#print(x)
			scheduleTimes[x] = True

	i = 0	

	for x in scheduleTimes:
	#	print(i, False)
		if(x == False):
			print("hello")
			
		i += 1
			
	a = 2
	b = 3
	
	my_tuple = [(a,b),(b,a),(a,b)]
	print([my_tuple[0], my_tuple[1], my_tuple[2]])
	
	#print(startTime)
	#print(endTime)
	
	
	
	print(scheduleTimes)
		
    # Merge meeting ranges
	#print(meetings[1][1])
	
	return meetings[0], meetings[1]




firstset = (1,4), (5,8)

test = merge_ranges(firstset)

#print(test)


# # Tests

# class Test(unittest.TestCase):

    # def test_meetings_overlap(self):
        # actual = merge_ranges([(1, 3), (2, 4)])
        # expected = [(1, 4)]
        # self.assertEqual(actual, expected)

    # def test_meetings_touch(self):
        # actual = merge_ranges([(5, 6), (6, 8)])
        # expected = [(5, 8)]
        # self.assertEqual(actual, expected)

    # def test_meeting_contains_other_meeting(self):
        # actual = merge_ranges([(1, 8), (2, 5)])
        # expected = [(1, 8)]
        # self.assertEqual(actual, expected)

    # def test_meetings_stay_separate(self):
        # actual = merge_ranges([(1, 3), (4, 8)])
        # expected = [(1, 3), (4, 8)]
        # self.assertEqual(actual, expected)

    # def test_multiple_merged_meetings(self):
        # actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        # expected = [(1, 8)]
        # self.assertEqual(actual, expected)

    # def test_meetings_not_sorted(self):
        # actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        # expected = [(1, 4), (5, 8)]
        # self.assertEqual(actual, expected)

    # def test_sample_input(self):
        # actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        # expected = [(0, 1), (3, 8), (9, 12)]
        # self.assertEqual(actual, expected)


# unittest.main(verbosity=2)