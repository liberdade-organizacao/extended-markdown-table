from sys import argv


def _get_fields(line):
    return [
        x.strip()
        for x in line.strip("|").split("|")
    ]


def _parse_operations(line):
    clean_line = line[1:].strip()
    name, operation = (f.strip() for f in clean_line.split("="))
    return (name, eval(operation))


def _get_operations(lines):
    return [
        _parse_operations(line)
        for line in lines
        if line[0] == ":"
    ]


def _get_table(lines):
    headers = _get_fields(lines[0])
    return [
        {
            x[0]: x[1]
            for x in zip(headers, _get_fields(line))
        }
        for line in lines[2:]
        if line[0] != ":"
    ]


def extend(table, operations):
    for i, row in enumerate(table):
        for name, operation in operations:
            row[name] = operation(table, row, i)
        table[i] = row
    return table
    

def to_md(headers, table):
    # TODO complete me
    outlet = f"| {' | '.join(headers)} |\n"
    outlet += f"|{'|'.join(['---'] * len(headers))}|\n"
    return outlet


def main(argv):
    lines = []
    with open(argv[0], 'r') as fp:
        for line in fp:
            lines.append(line.strip("\n"))
    headers = _get_fields(lines[0])
    operations = _get_operations(lines)
    table = _get_table(lines)
    return to_md(headers, extend(table, operations))


if __name__ == "__main__":
    print(main(argv[1:]))
