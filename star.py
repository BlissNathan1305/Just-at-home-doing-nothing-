def print_star():
    """Prints a single star character to the console."""
    print("*")

def print_stars(number):
    """Prints a specified number of stars on the same line

       Args:
          number: The number of stars to print.
    """
    if not isinstance(number, int) or number < 0:
        print("Error: Number must be a non-negative integer")
        return
    print("*" * number)

def main():
    """
    Main function to demonstrate the star printing functions.
    """
    print("Printing a single star:")
    print_star()  # Calls the function to print a single star.

    print("\nPrinting five stars:")
    print_stars(5) # Prints 5 stars on the same line

    print("\nPrinting zero stars")
    print_stars(0)

if __name__ == "__main__":
    main()

