def print_row(data, cell_sep=' | '):
    cols = len(data)
    result = []

    for col in range(cols):
        item = data[col].center(15)
        result.append(item)

    print(cell_sep.join(result))
