test = ["a", "b", "c", "d"]
def generate_combinations(item_list, num_items):
    comb_list = []
    def comb(combinations, item_list, n):
        if n == 0:
            comb_list.append(combinations[:-1].split("|"))
        else:
            for i in range(len(item_list)):
                comb(combinations + item_list[i] + "|", item_list[i+1:], n-1)
    comb("", item_list, num_items)
    return comb_list

print(generate_combinations(test, 3))