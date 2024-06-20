while True:
    try:
      user_input = input("Enter a number between 1 and 10: ")
      number = int(user_input)

      if 1<= number <= 10:
        print(f"The square of {number} is {number ** 2}")
        break
      else:
        print("Error: Invalid Input. Please enter a number between 1 and 10.")

    except ValueError:
      print("Error: Invalid input. Please enter a number between 1 and 10.")