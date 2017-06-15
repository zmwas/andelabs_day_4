def find_missing(first_list,second_list):

    if len(second_list)>len(first_list):
        for i in second_list:
            if i not in first_list:
                return i
    else:
        for i in first_list:
            if i not in second_list:
                return i

    return 0

print(find_missing([4, 6, 8], [4, 6, 8, 10]))