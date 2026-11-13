numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
def find_min(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def find_max(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1



def bubble_sort(numbers):
    sorted_numbers = numbers.copy()

    for _ in range(len(sorted_numbers) - 1):
        for index in range(len(sorted_numbers) - 1):
            if sorted_numbers[index] > sorted_numbers[index + 1]:
                sorted_numbers[index], sorted_numbers[index + 1] = (
                    sorted_numbers[index + 1],
                    sorted_numbers[index],
                )

    return sorted_numbers


def show_menu():
    print("Menu:")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    return input("Choose an option (1–5): ")

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            print("Minimum:", find_min(numbers))
        elif choice == "2":
            print("Maximum:", find_max(numbers))
        elif choice == "3":
            target = int(input("Enter the number to search for: "))
            index = search(numbers, target)
            if index != -1:
                print(f"Found at index {index}")
            else:
                print("Not found")
        elif choice == "4":
            print("Sorted numbers:", bubble_sort(numbers))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
