list_to_sort = [1,2,23, 89,4,5]

lenght = len(list_to_sort)

for i in range(lenght):
    for j in range(lenght - i - 1):
        if list_to_sort[j] > list_to_sort[j+1]:
            x = list_to_sort[j+1] 
            list_to_sort[j+1] = list_to_sort[j]
            list_to_sort[j] = x
print(list_to_sort)