from functools import reduce

def detect_benford(filecontent):
    register = []

    def insert_into_register(leading_digit, i):
        while len(register) <= i:
            register.append([0 for x in range(10)])

        register[i][leading_digit] = register[i][leading_digit] + 1

    columns_count = 0
    correct_insertion = True
    first_line = True
    for line in filecontent.split("\n"):
        if first_line:
            first_line = False
            continue

        split_line = line.replace("\n", "").split("\t")
        for i, arg in enumerate(split_line):
            arg = arg.replace(" ", "")
            converted = None
            try:
                converted = float(arg)
            except:
                pass

            if isinstance(converted, (float, int)):
                if converted >= 0:
                    leading_digit = int(arg[0])
                else:
                    leading_digit = int(arg[1])
                insert_into_register(leading_digit, i)
        if columns_count:
            correct_insertion = columns_count == len(split_line)
        else:
            columns_count = len(split_line)
            correct_insertion = True

    records_count = [sum(column) for column in register]
    benford_detected = [col_sum > 10 and col[1] / col_sum > 0.25 and col[1] / col_sum < 0.35 for (col, col_sum) in
                        zip(register, records_count)]

    return ({"benford_detect": benford_detected,
             "columns_distribution": register,
             "records_count": records_count,
             "correct_insertion": correct_insertion})
