alphabet_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alphabet_dict = dict()
for i in range(len(alphabet_list)):
    alphabet_dict[alphabet_list[i]] = i + 1

result = 0
current_index = 1
for alphabet in input():
    i_diff = abs(alphabet_dict[alphabet] - current_index)
    if i_diff > 13:
        result += (26-i_diff)
    else:
        result += i_diff
    current_index = alphabet_dict[alphabet]
print(result)