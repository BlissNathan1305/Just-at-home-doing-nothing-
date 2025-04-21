def print_rectangle(width, height):
    # Print top border
    print("*" * width)
    
    # Print sides
    for _ in range(height - 2):
        print("*" + " " * (width - 2) + "*")
    
    # Print bottom border (if height > 1)
    if height > 1:
        print("*" * width)

# Example usage:
width = 10
height = 5
print_rectangle(width, height)
