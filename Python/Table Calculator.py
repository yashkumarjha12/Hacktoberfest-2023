import time
user_calculates = True
while user_calculates:
    num = int(input("Tell me The Number for which tables you want.\n"))
    print("Here's Your Table!")
    print(f"{num} x 1 = {num * 1}")
    print(f"{num} x 2 = {num * 2}")
    print(f"{num} x 3 = {num * 3}")
    print(f"{num} x 4 = {num * 4}")
    print(f"{num} x 5 = {num * 5}")
    print(f"{num} x 6 = {num * 6}")
    print(f"{num} x 7 = {num * 7}")
    print(f"{num} x 8 = {num * 8}")
    print(f"{num} x 9 = {num * 9}")
    print(f"{num} x 10 = {num * 10}")
    user_choice = input("Do You Want to Calculate The Table Again?? [Y/N]: ")
    if user_choice == "y":
        user_calculates = True
    elif user_choice == "n":
        user_calculates = False
        break
    else:
        print("Invalid Command, Please Try Again...")
        time.sleep(5)
        user_calculates = False
