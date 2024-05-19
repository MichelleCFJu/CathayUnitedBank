def hollow_equilateral_triangle(side_length):
    # Loop through each row
    for i in range(side_length):
        # Print leading spaces
        print(" " * (side_length - i - 1), end="")
        
        # Print stars for the first and last rows
        if i == 0 or i == side_length - 1:
            print("* " * (i + 1))
        else:
            # Print stars for the inner rows
            print("*", end="")
            print(" " * (2 * i - 1), end="")
            print("*")

# Test the function with input 3
hollow_equilateral_triangle(3)
