class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        
        # Check for custom delimiter
        delimiter = ","
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)
            delimiter = delimiter_line[2:]  # Extract the delimiter (everything after //)
        
        # Replace newlines with the delimiter
        numbers = numbers.replace("\n", delimiter)
        
        # Split by delimiter and sum
        if delimiter in numbers:
            parts = numbers.split(delimiter)
            return sum(int(num) for num in parts)
        return int(numbers) 