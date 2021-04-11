from AVLtree import AVL
import random


def srtd(li):
    return all(li[i] <= li[i+1] for i in range(len(li)-1))


def test_iter():
    a1 = AVL.Node(1)
    a3 = AVL.Node(3)
    a2 = AVL.Node(2, a1, a3)
    a5 = AVL.Node(5)
    a7 = AVL.Node(7)
    a6 = AVL.Node(6, a5, a7)
    a4 = AVL.Node(4, a2, a6)

    l_nodes = [a1, a2, a3, a4, a5, a6, a7]

    for n in l_nodes:
        a = AVL(node=n)
        t_list = list(map(lambda x: x.v, a))
        assert srtd(t_list)


def test_add():
    a = AVL()
    for i in range(1, 99):
        a.add(i)
        t_list = list(map(lambda x: x.v, a))
        assert srtd(t_list)

    t_len = len(list(map(lambda x: x.v, a)))

    for i in range(1, 99):
        a.add(i)
        t_list = list(map(lambda x: x.v, a))
        assert len(t_list) == t_len

    for i in range(-1, -99, -1):
        a.add(i)
        t_list = list(map(lambda x: x.v, a))
        assert srtd(t_list)


def test_add2():
    lst = [random.randint(1, 10) for _ in range(100)]
    s_lst = list(set(lst))

    b = AVL()

    for i in lst:
        b.add(i)

    t_lst = list(map(lambda x: x.v, b))

    assert len(t_lst) == len(s_lst)

    assert s_lst == t_lst


def test_contains():
    lst = [random.randint(1, 1000) for _ in range(100)]

    a = AVL()

    for i in lst:
        a.add(i)

    lst = set(lst)

    for i in lst:
        assert a[i] is not None

    for _ in range(100):
        i = random.randint(1, 1000)
        f1 = (a[i] is not None)
        f2 = i in lst
        f3 = i in a
        assert f1 == f2 == f3


def test_len():
    lsts = [[random.randint(1, 1000) for _ in range(100)]
            for _ in range(10)]

    for lst in lsts:
        a = AVL()

        for i in lst:
            a.add(i)

        lst = set(lst)

        assert len(lst) == len(a)
