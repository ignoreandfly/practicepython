input_str = input("Enter the string you want to reverse ")
list_str = input_str.split()
reverse_list_str = []
for i in range(1, len(list_str)+1):
    reverse_list_str.append(list_str[-i])

reverse_str = ' '.join(reverse_list_str)
print(reverse_str)