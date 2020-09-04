# from multiprocessing import Pool
from cloudbutton.multiprocessing import Pool
import random


def is_inside(n):
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x*x + y*y < 1:
            count += 1
    return count


if __name__ == '__main__':
    np, n = 96, 15000000000
    part_count = [int(n/np)] * np
    pool = Pool(processes=np, initargs={'runtime_memory': 4096})
    count = pool.map(is_inside, part_count)
    pi = sum(count)/n*4
    print("Esitmated Pi: {}".format(pi))
