def print_triangle(height, char='*'):
    """
    Prints a right-angled triangle of a specified height using a given character.

    Args:
        height: The height of the triangle (number of rows). Must be a positive integer.
        char: The character to use for printing the triangle. Defaults to '*'.
    """
    if not isinstance(height, int) or height <= 0:
        print("Error: Height must be a positive integer.")
        return  # Exit the function if the height is invalid

    for i in range(1, height + 1):
        print(char * i)

def print_upside_down_triangle(height, char='*'):
    """
    Prints an upside-down right-angled triangle.

    Args:
        height: The height of the triangle (number of rows).
        char: The character to use.
    """
    if not isinstance(height, int) or height <= 0:
        print("Error: Height must be a positive integer.")
        return
    for i in range(height, 0, -1):
        print(char * i)

def print_isosceles_triangle(height, char='*'):
    """
    Prints an isosceles triangle.

    Args:
        height: The height of the triangle.
        char: The character to use.
    """
    if not isinstance(height, int) or height <= 0:
        print("Error: Height must be a positive integer.")
        return

    for i in range(1, height + 1):
        spaces = height - i
        stars = 2 * i - 1
        print(" " * spaces + char * stars)

def print_centered_triangle(height, char='*'):
    """Prints a centered triangle.

       Args:
           height: The height of the triangle
           char: The character to use for printing.
    """
    if not isinstance(height, int) or height <= 0:
        print("Error: Height must be a positive integer.")
        return

    for i in range(1, height + 1):
        # Calculate the number of spaces before the stars
        spaces = height - i
        # Calculate the number of stars in the current row
        stars = 2 * i - 1
        # Print the spaces and the stars
        print(' ' * spaces + char * stars)
def main():
    """
    Main function to demonstrate the triangle printing functions.
    """
    print("Right-angled triangle:")
    print_triangle(5)  # Prints a right-angled triangle of height 5 using '*'

    print("\nRight-angled triangle with different character:")
    print_triangle(4, '#')  # Prints a right-angled triangle of height 4 using '#'

    print("\nUpside-down right-angled triangle:")
    print_upside_down_triangle(5)

    print("\nIsosceles triangle:")
    print_isosceles_triangle(4, 'X')

    print("\nCentered triangle:")
    print_centered_triangle(5)
    print("\nCentered triangle:")
    print_centered_triangle(6, '$')

if __name__ == "__main__":
    main()

i
