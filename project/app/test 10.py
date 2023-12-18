def combine_lists(list1, list2):
    return [
        (x if i < len(x)
             else ‘N/A’, y if i < len(y)
    else ‘N/A’)
    for i, (x, y)
    in enumerate(zip(list1, list2))
    ]

map(lambda x: print(reduce(add, x)), izip(*[iter(range(10))] * 2))