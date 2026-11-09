name_list=["James", "Olivia", "William", "Emma", "Benjamin", "Sophia", "Lucas", "Charlotte", "Henry", "Amelia"]
name=input("Enter a name to search for: ")
find=-1
for i in range(len(name_list)):
    if name_list[i] == name:
      print(f"Found {name} at index {i}.")
      find=0
      break
            
if find == -1:
      print(f"{name} was not found in the list.")
