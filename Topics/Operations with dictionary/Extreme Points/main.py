# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
minimum = min(test_dict, key=test_dict.get)
maximum = max(test_dict, key=test_dict.get)

print(f"min: {minimum}")
print(f"max: {maximum}")
