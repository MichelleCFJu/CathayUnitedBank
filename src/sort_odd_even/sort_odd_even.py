def sort_odd_even(input_str):
    # Convert the string to a list of integers
    num_list = [int(num) for num in input_str]
    
    # Separate odd and even numbers
    odd_nums = [num for num in num_list if num % 2 != 0]
    even_nums = [num for num in num_list if num % 2 == 0]
    
    # Sort odd numbers in descending order
    odd_nums.sort(reverse=True)
    # Sort even numbers in ascending order
    even_nums.sort()
    
    # Merge odd and even numbers
    sorted_nums = odd_nums + even_nums
    
    # Convert the list of integers to a string
    sorted_str = ''.join(map(str, sorted_nums))
    
    return sorted_str

# Test the function
input_str = '417324689435'
output_str = sort_odd_even(input_str)
print(output_str)  # Output expected result: '975331244468'
