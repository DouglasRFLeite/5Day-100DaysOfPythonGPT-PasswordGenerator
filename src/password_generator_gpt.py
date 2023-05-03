import sys
from os.path import abspath, dirname

# Add the parent directory of the current file to sys.path
sys.path.append(abspath(dirname(dirname(__file__))))

from include import gpt

def generate_password():
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    prompt = f"""
Generate a random and strong password with {nr_letters} letters, {nr_numbers} numbers
and {nr_symbols} symbols. Return just the password.
    """

    password = gpt.get_completion(prompt)
    return password

if __name__ == "__main__":
    print(generate_password())