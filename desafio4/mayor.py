import sys

first_num = int(sys.argv[1])
second_num = int(sys.argv[2])
third_num = int(sys.argv[3])

if first_num > second_num & first_num > third_num:
    print(first_num)
elif second_num > third_num:
    print(second_num)
else:
    print(third_num)