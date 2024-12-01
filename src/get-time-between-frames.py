def process_file(file_path):
    try:
        # Read the file and process the lines
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Ignore the first line and process the rest
        numbers = [float(line.strip()) for line in lines[1:]]
        
        # Calculate the differences between consecutive numbers
        differences = [numbers[i+1] - numbers[i] for i in range(len(numbers) - 1)]
        
        # Reverse the order of the differences
        reversed_differences = differences[::-1]
        
        return reversed_differences
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
file_path = 'timestamps.txt'  # Replace with your .txt file path
result = process_file(file_path)
if result is not None:
    print("Reversed differences:", result)
