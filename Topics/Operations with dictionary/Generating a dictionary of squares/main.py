# Importing necessary library
import sys


def generate_dict(N):
    # Use dictionary comprehension to create a dictionary
    # Remember, the key is the number and the value is the square of that number
    # Write your code here
    return {i: i ** 2 for i in list(range(1, N + 1))}


# Main function handling the input/output
def main():
    N = int(sys.stdin.readline().strip())
    result = generate_dict(N)
    print(result)


if __name__ == "__main__":
    main()
