## Hi there 👋

<!--
**RehanH786/RehanH786** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

-->
if __name__ == "__main__":
    name = input("Greetings! How shall I call you? ")

    current_year = int(input("What is the current year? "))
    birth_year = int(input("What year were you born? "))

    age = current_year - birth_year

    print(f"Hello, {name}! This year you will be {age} years old!")