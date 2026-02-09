def get_numbers(word_length):
    numbers = []
    for i in range(word_length):
        num = int(input(f"Enter number {i + 1}:"))
        numbers.append(num)
    return numbers

def average(numbers):
    return sum(numbers) / len(numbers)

def compare(word, avg_value):
    if len(word) > avg_value:
        return f"The length of the word '{word}' is greater than the average."
    elif len(word) < avg_value:
        return f"The length of the word '{word}' is less than the average."
    else:
        return f"The length of the word '{word}' is equal to the average."

word = input("Enter a word:")
numbers = get_numbers(len(word))
avg_value = average(numbers)

print(numbers)
print("The length of the word is", len(word))
print("The average of the numbers is", avg_value)
print(compare(word, avg_value))
