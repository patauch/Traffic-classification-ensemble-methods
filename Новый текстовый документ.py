def kaprekar_step(L):
    L = "".join(map(str, sorted(L)))
    return int(L[::-1]) - int(L)


def numerics(n):
    return list(map(int, str(n)))


def kaprekar_check(n):
    nums_dict = [3, 4, 6]
    nums_wrong = [100, 1000, 100000]
    if len(set(numerics(n))) == 1:
        return False
    elif not len(numerics(n)) in nums_dict:
        return False
    elif n in nums_wrong:
        return False
    else:
        return True


def kaprekar_loop(n, set_of_changes = []):
    kaprekar_list = [495, 6174, 549945, 631764]
    if kaprekar_check(n):
        if n in kaprekar_list:
            print(n)
            return n
        else:
            if n not in set_of_changes:
                print(n)
                set_of_changes.append(n)
                return kaprekar_loop(kaprekar_step(numerics(n))), set_of_changes
            else:
                print("Следующее число - {}, кажется процесс зациклился...".format(n))

    else:
        print("Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара".format(n))



