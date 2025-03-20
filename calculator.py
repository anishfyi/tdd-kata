class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        
        # Replace newlines with commas
        numbers = numbers.replace("\n", ",")
        
        if "," in numbers:
            parts = numbers.split(",")
            return sum(int(num) for num in parts)
        return int(numbers) 