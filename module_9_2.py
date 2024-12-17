first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >= 5]
second_result = [(name1, name2) for name1 in first_strings for name2 in second_strings if len(name1) == len(name2)]
third_result = {name: len(name) for name in first_strings + second_strings if not len(name) % 2}

print(first_result)
print(second_result)
print(third_result)
