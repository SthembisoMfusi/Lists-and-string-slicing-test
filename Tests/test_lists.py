import unittest
from Lists import *  # Assuming your assessment code is in a file named assessment.py

class TestAssessment(unittest.TestCase):

    def test_part1(self):
       
        numbers = [] # Reset the list before each test

        numbers = create_numbers_list() #Added to re-create initial list
        self.assertEqual(numbers, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Failed to create initial numbers list")

        add_eleven() # function to add eleven to the end
        self.assertEqual(numbers, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "Failed to add 11 to the end")

        insert_zero() # function to insert 0 at the beginning
        self.assertEqual(numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "Failed to insert 0 at the beginning")

        remove_five() # function to remove 5 from the list
        self.assertEqual(numbers, [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11], "Failed to remove 5 from the list")


    def test_part2(self):
        # Test List Comprehension

        numbers = [] # Reset the list before each test
        numbers = create_numbers_list() #Added to re-create initial list
        add_eleven() #Add eleven so it is in list
        insert_zero() #Add zero so it is in the list
        remove_five() #Removes five so the list is the same for the         
        self.even_numbers = create_even_numbers()
        self.assertEqual(self.even_numbers, [0, 2, 4, 6, 8, 10], "Failed to create even_numbers list")

        self.squared_numbers = create_squared_numbers()
        self.assertEqual(self.squared_numbers, [0, 1, 4, 9, 16, 36, 49, 64, 81, 100, 121], "Failed to create squared_numbers list")


    def test_part3(self):
        # Test String Slicing
        text = "Hello, World!"
        self.assertEqual(extract_hello(text), "Hello", "Failed to extract 'Hello'")
        self.assertEqual(extract_world(text), "World", "Failed to extract 'World'")
        self.assertEqual(reverse_string(text), "!dlroW ,olleH", "Failed to reverse the string")

    def test_part4(self):
        #Test More List Operations
        test_list = [10,20,30,40,50]

        self.assertEqual(get_second_element(test_list), 20, "Failed to get the second element")
        self.assertEqual(get_second_element([]), None, "Failed to return None if list is empty")

        self.assertEqual(get_last_three_elements(test_list), [30,40,50], "Failed to get the last three elements")
        self.assertEqual(get_last_three_elements([10,20]), [10,20], "Failed to get last three elements in smaller list")

        replace_element(test_list, 2, 35)
        self.assertEqual(test_list, [10,20,35,40,50], "Failed to replace element in the list")


if __name__ == '__main__':
    unittest.main()