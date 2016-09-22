# 1. Eratosthenes Sieve:

"""
Inputs:
    (int) n = 0
Output:
    (string) "23571"

Inputs:
    (int) n = 3
Output:
    (string) "71113"
"""

if __name__ == "__main__":


    a_indx = int(raw_input("Enter Index"))

    list_of_primes = [2]
    str_CFS = ''.join([str(x) for x in list_of_primes])
    iter_count = 2
    while len(str_CFS) < a_indx + 5:
        if 0 not in [iter_count%x for x in list_of_primes] :
            list_of_primes.append(iter_count)
            str_CFS = str_CFS + str(iter_count)
        iter_count = iter_count + 1

    print(str_CFS)

    print(str_CFS[a_indx:a_indx + 5])
