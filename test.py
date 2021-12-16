from time import time

from main import *


def test_min():
    assert find_min([4, 3, 2, 1]) == 1
    assert find_min([1, 3, 2, 4]) == 1
    assert find_min([4, 3, 1, 2]) == 1


def test_max():
    assert find_max([4, 3, 2, 1]) == 4
    assert find_max([1, 3, 2, 4]) == 4
    assert find_max([3, 4, 1, 2]) == 4


def test_sum():
    assert find_sum([3, 1, 2, 4]) == 10
    assert find_sum([0, 0, 0, 0]) == 0
    assert find_sum([1, 0, 0, 2]) == 3


def test_product():
    assert find_product([4, 3, 2, 1]) == 24
    assert find_product([1, 3, 2, 0]) == 0
    assert find_product([1, 1, 1, 1]) == 1


def write_input(s):
    with open("input.txt", "w") as f:
        f.write(s)


def test_speed():
    write_input("123 " * 10000)
    t1 = time()
    main(out=False)
    print("Time needed", time() - t1)


def test_read():
    write_input("1 2 3 4")
    assert read() == [1, 2, 3, 4]


def test():
    test_min()
    print("Passed find_min")
    test_max()
    print("Passed find_max")
    test_sum()
    print("Passed find_sum")
    test_product()
    print("Passed find_product")
    test_speed()
    test_read()
    print("Passed speed")


if __name__ == '__main__':
    test()
