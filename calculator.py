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
        
        # Split by delimiter and convert to integers
        if delimiter in numbers:
            parts = numbers.split(delimiter)
            nums = [int(num) for num in parts]
        else:
            nums = [int(numbers)]
        
        # Check for negative numbers
        negatives = [num for num in nums if num < 0]
        if negatives:
            message = "negatives not allowed: " + ", ".join(map(str, negatives))
            raise ValueError(message)
        
        return sum(nums) 