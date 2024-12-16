data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    sum_num = 0
    sum_str = 0

    def recurse(things):
        nonlocal sum_num, sum_str
        if isinstance(things, list) or isinstance(things, tuple) or isinstance(things, set):
            for item in things:
                recurse(item)
        elif isinstance(things, dict):
            for value in things.values():
                recurse(value)
            for key in things.keys():
                recurse(key)
        elif isinstance(things, int) or isinstance(things, str):
            if isinstance(things, int):
                sum_num += things
            elif isinstance(things, str):
                sum_str += len(things)

    recurse(data_structure)
    return sum_num + sum_str


result = calculate_structure_sum(data_structure)
print(result)
