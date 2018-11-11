list_of_nums = list(map(int, input('Enter integers separated by spaces: ').split()))

sorted_list = sorted(list_of_nums)
min_number = sorted_list[0]
max_number = sorted_list[-1]

print(max_number - min_number)

