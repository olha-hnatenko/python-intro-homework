numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
while True:
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    
    # option 5: Quit
    choice = input("Choose an option (1-5): ")
    if choice == "5":
        print("Goodbye!")
        break

    # option 1: Find minimum 
    elif choice == "1":
        smallest = numbers[0]
        for num in numbers: 
            if num < smallest:
                smallest = num
        print(f"Minimum number: {smallest}")
       
    # option 2: Find maximum
    elif choice == '2':
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        print(f"Maximum: {largest}")


    
    # option 3: Search for a number
    elif choice == "3":
        target = int(input("Enter a number to search for: "))
        for i in range(len(numbers)):
            if numbers[i] == target:
                index = i
                print(f"Found {target} at index {index}.")
                break
        
        else:
            print(f"{target} is not in the list.")  



    # option 4: Sort the list
    elif choice == "4":
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    #swap adjusment element
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True
        print(f"Sorted list: {numbers}")