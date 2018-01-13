# Python 3: Prime sieve

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


# noinspection SpellCheckingInspection
def sieve(x):
    """
    sieve as a list 0,1,2...are all (p)rime to start with
    Make all evens (c)ompound

    :param x:
    :return:
    """
    sieve1 = []
    odd = False
    for y in range(x + 1):
        if odd:
            sieve1.append('p')
        else:
            sieve1.append('c')

        if odd:
            odd = False
        else:
            odd = True

    sieve1[1] = 'c'
    sieve1[2] = 'p'
    return sieve1


def process(sieve2, prime2):
    """
    optimize not looking at previous prime multiple IE 3 x 7 : 21 already done
    test me - I can't cope with being sent a zero!
    :param prime2:
    :param sieve2:
    :return: 
    """
    logging.info('Finding multiples of %s', prime2)
    count = prime2 * 3  # start at 3x the prime
    step = prime2 * 2  # increment in 2x to avoid evens
    while count <= (len(sieve2)):
        sieve2[count] = 'c'
        logging.debug("%s is a multiple of prime %s", count, prime2)
        count = count + step
    return sieve2


def pretty_print_all(sieve3):
    """
    Print the sieve
    :param sieve3:
    :return:
    """
    for i in range(sieve3.__len__()):
        print(repr((i, sieve3[i])))

def pretty_print_primes(sieve4):
    """
    Print the sieve
    :param sieve4:
    :return:
    """
    for i in range(len(sieve4)):
        if sieve4[i] == 'p':
            print(i,end=',')


def next_prime(sieve4, prime):
    """
    Count up from prime and find the next index that is prime
    :param sieve4:
    :param prime:
    :return: next prime, or 0 is there are no more
    """

    for i in range(prime + 2, len(sieve4), 2):
        if sieve4[i] == 'p':
            logging.debug('Next prime: %s', i)
            return i
        return 0


s = sieve(9999)
p = 3
while p != 0:
    s = process(s, p)
    p = next_prime(s, p)
    #pretty_print_all(s)

# sieve = process(sieve, 3)
# sieve = process(sieve, 5)
# sieve = process(sieve, 7)
# sieve = process(sieve, 11)

pretty_print_primes(s)
