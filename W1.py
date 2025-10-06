if __name__ == "__main__":
    name = input("Greetings! How should I call you? ")

    current_year = int(input("What year is it? "))
    birth_year = int(input("What year were you born? "))

    age = current_year - birth_year

    print(f"Hello, {name}! This year you will be {age} years old!")
    