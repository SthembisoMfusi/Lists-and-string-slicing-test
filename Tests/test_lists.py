import unittest
from Lists import *  # Assuming your assessment code is in a file named assessment.py

class TestAssessment(unittest.TestCase):

    def test_create_numbers_list(self):
        numbers = create_numbers_list()
        self.assertEqual(numbers, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Failed to create initial numbers list") 

    def test_add_eleven(self):
        numbers = create_numbers_list() # Start with a fresh list
        numbers = add_eleven(numbers)
        self.assertEqual(numbers, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "Failed to add 11 to the end")

    def test_insert_zero(self):
        numbers = create_numbers_list() # Start with a fresh list
        numbers = insert_zero(numbers)
        self.assertEqual(numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Failed to insert 0 at the beginning") 

    def test_remove_five(self):
        numbers = create_numbers_list() # Start with a fresh list
        numbers = add_eleven(numbers) # Ensure 5 is removed from a list that contained it
        numbers = insert_zero(numbers) # Ensure 5 is removed from a list that contained it
        numbers = remove_five(numbers)
        self.assertEqual(numbers, [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11], "Failed to remove 5 from the list ")

    def test_create_even_numbers(self):
        numbers = create_numbers_list() # Get a list to work with
        numbers = add_eleven(numbers)
        numbers = insert_zero(numbers)
        numbers = remove_five(numbers)
        even_numbers = create_even_numbers(numbers)
        self.assertEqual(even_numbers, [0, 2, 4, 6, 8, 10], "Failed to create even_numbers list ") 

    def test_create_squared_numbers(self):
        numbers = create_numbers_list() 
        numbers = add_eleven(numbers)
        numbers = insert_zero(numbers)
        numbers = remove_five(numbers)
        squared_numbers = create_squared_numbers(numbers)
        self.assertEqual(squared_numbers, [0, 1, 4, 9, 16, 36, 49, 64, 81, 100, 121], "Failed to create squared_numbers list") 
    def test_extract_hello(self):
        text = "Hello, World!"
        self.assertEqual(extract_hello(text), "Hello", "Failed to extract word") 

    def test_extract_world(self):
        text = "Hello, World!"
        self.assertEqual(extract_world(text), "World", "Failed to extract 'World'") 

    def test_reverse_string(self):
        text = "Hello, World!"
        self.assertEqual(reverse_string(text), '!dlroW ,olleH', "Failed to reverse the string") 

    def test_get_second_element_exists(self):
        test_list = [10,20,30,40,50]
        self.assertEqual(get_second_element(test_list), 20, "Failed to get the second element") 

    def test_get_second_element_not_exists(self):
        self.assertEqual(get_second_element([]), None, "Failed to return None if list is empty") 

    def test_get_last_three_elements_enough_elements(self):
        test_list = [10,20,30,40,50]
        self.assertEqual(get_last_three_elements(test_list), [30, 40, 50], "Failed to get the last three elements") 

    def test_get_last_three_elements_fewer_than_three(self):
        self.assertEqual(get_last_three_elements([10,20]),[10, 20], "Failed to get last three elements in smaller list") 

    def test_replace_element(self):
        test_list = [10,20,30,40,50] 
        replace_element(test_list, 2, 35)
        self.assertEqual(test_list, [10, 20, 35, 40, 50], "Failed to replace element in the list") 


if __name__ == '__main__':
    unittest.main()