filenames = ['1.txt', '2.txt']
files = dict()


def sort_by_values_len(x: dict) -> dict:
    dict_len = {key: len(value) for key, value in x.items()}
    import operator
    sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1))
    sorted_dict = dict()

    for item in sorted_key_list:
        sorted_dict[item[0]] = x[item[0]]
    return sorted_dict


with open('output.txt', 'w') as outfile:
    for name in filenames:
        with open(name) as infile:
            files[name] = infile.readlines()

    files = sort_by_values_len(files)

    for key in files.keys():
        outfile.write(key + f'\n{len(files[key])}\n')
        outfile.writelines(files[key])
        outfile.write('\n')

