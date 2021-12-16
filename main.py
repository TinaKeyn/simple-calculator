def find_min(lst):
    mn = lst[0]
    for e in lst:
        if e < mn:
            mn = e

    return mn


def find_max(lst):
    mx = lst[0]
    for e in lst:
        if e > mx:
            mx = e

    return mx


def find_sum(lst):
    sm = 0
    for e in lst:
        sm += e

    return sm


def find_product(lst):
    prod = 1
    for e in lst:
        try:
            prod *= e
        except OverflowError:
            return

    return prod


def read():
    with open("input.txt", "r") as f:
        lst_inp = list(map(int, f.readline().split()))
    return lst_inp


def run(lst_inp, out=True):
    mn = find_min(lst_inp)
    mx = find_max(lst_inp)
    sm = find_sum(lst_inp)
    prod = find_product(lst_inp)
    if out:
        print("Minimum:", mn)
        print("Maximum:", mx)
        print("Sum:", sm)
        print("Product:", prod)


def main(out=True):
    lst_inp = read()
    run(lst_inp, out)


if __name__ == '__main__':
    main()
