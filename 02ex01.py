USAGE = """USAGE: {script} initial_sum percent fixed_period set_period
\tCalculate deposit yield. See script source for more details.
"""
#USAGE = USAGE.strip()


def deposit(initial_sum, percent, fixed_period, set_period):
    per = percent / 100
    one_year = (1 + per)
    growth_five = one_year ** 5
    growth_ten = one_year ** 10
    growth_set = one_year ** (set_period / fixed_period)


    return f"One month yield: {initial_sum * one_year / 12}\n" \
           f"One year yield: {initial_sum * one_year}\n" \
           f"Five year yield: {'%.2f' % (initial_sum * growth_five)}\n" \
           f"Ten year yield: {'%.2f' % (initial_sum * growth_ten)}\n" \
           f"Set period yield: {initial_sum * growth_set}"


def main(args):
    if len(args) != 4 + 1:
        exit(USAGE.format(script=args[0]))

    args = args[1:]
    initial_sum, percent, fixed_period, set_period = map(float, args)

    res = deposit(initial_sum, percent, fixed_period, set_period)
    print(res)


if __name__ == '__main__':
    import sys

    main(sys.argv)
