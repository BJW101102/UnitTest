import unittest

def bubble_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Input should be a list.")
    # Ensure all elements are numbers (int or float)
    if len(arr) > 0 and not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements in the list must be numbers (int or float).")
    
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

class TestBubbleSort(unittest.TestCase):

    # Positive Case: Typical array with numbers (integers and floats)
    def test_typical_case(self):
        arr = [5.5, 3, 8.8, 4, 2.2]
        sorted_arr = bubble_sort(arr)
        self.assertEqual(sorted_arr, [2.2, 3, 4, 5.5, 8.8])

    # Negative Case: Non-list input
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            bubble_sort("not a list")
    
    # Negative Case: Non-number elements in list (string in this case)
    def test_invalid_input_non_number(self):
        with self.assertRaises(TypeError):
            bubble_sort([1, 2.2, 'string'])  # Includes a string, not a number

    # Performance Case: Large array with numbers
    def test_large_array(self):
        large_array = [float(i) for i in range(1000, 0, -1)]  # Large array in reverse order
        sorted_large_array = bubble_sort(large_array)
        self.assertEqual(sorted_large_array, list(map(float, range(1, 1001))))

    # Boundary Case: Edge cases
    def test_boundary_cases(self):
        # Empty array
        self.assertEqual(bubble_sort([]), [])
        
        # Single element
        self.assertEqual(bubble_sort([42]), [42])
        
        # Array with duplicate values
        self.assertEqual(bubble_sort([4, 2.2, 4, 3.3, 2.2]), [2.2, 2.2, 3.3, 4, 4])
        
        # Already sorted array
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        
        # Reverse sorted array
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    # Idempotency Case: Sorting an already sorted array
    def test_idempotency(self):
        arr = [1.1, 2, 3.3, 4, 5.5]
        sorted_arr = bubble_sort(arr)
        
        # Running bubble sort again on the sorted array
        sorted_again = bubble_sort(sorted_arr)
        self.assertEqual(sorted_arr, sorted_again)

if __name__ == "__main__":
    unittest.main()
