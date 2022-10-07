# import time

# start = time.time()

# alternatif yang lebih cepat
# def print_max_min_list(arr):
#     print(f'Terbesar : {max(arr)}, terkecil : {min(arr)}')

def print_max_min_list(arr):
    min_num = max_num = arr[0]
    for index in range(1, len(arr)):
        if min_num > arr[index]:
            min_num = arr[index]
        
        if max_num < arr[index]:
            max_num = arr[index]
    print(f'Terbesar : {max_num}, terkecil : {min_num}')

# format input -> 1 6 3 2 10 16 -100
list_of_num = list(map(int, input().split()))
print_max_min_list(list_of_num)

# with open('test_file.txt', 'r') as f:
#     list_of_num = list(map(int, f.readline().split(' ')))
#     print_max_min_list(list_of_num)
#     print(time.time() - start)