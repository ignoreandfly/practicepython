#ListRemoveDuplicates
original_list =  ["Michele", "Robin", "Sara", "Michele"]


#Using for loop
def for_loop(l):
    #With List Comprehension
    # without_duplicate = [original_list[i] for i in range(len(original_list)) if original_list[i] not in original_list[i+1: ]]
    # return(without_duplicate)

    #Without List Comprehension, in this method they appear in the same order as they do in the original list.
    without_duplicate = []

    for i in range(len(l)):
        if original_list[i] not in without_duplicate:
            without_duplicate.append(original_list[i])
    return without_duplicate

def set_method(l):
    return list(set(l))

print(for_loop(original_list))


