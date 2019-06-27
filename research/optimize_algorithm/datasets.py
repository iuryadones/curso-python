from multiprocessing import Pool
from random import random
from random import randint
from timeit import default_timer as timer
from functools import partial
import csv
import os


def coef_rand(n):
    list_coef = [randint(10,99) for _ in range(n)]
    return list_coef

def x_rand():
    return randint(1,3)

def func(list_coef,x):
    result = 0
    for n, coef in enumerate(list_coef):
        result +=  coef * x ** n
    return result

def main(coef,x,n):
    started_time = timer()
    result = func(coef,x)
    end_time = timer()

    dic = {
        'timer': (end_time - started_time)
    }
    return dic

if __name__ == '__main__':
    n = 18
    X = 3
    list_coef = coef_rand(n)
    with open('coefs.txt','w') as arq:
        for _coef in list_coef:
            arq.write(f'{_coef}\n')

    p_main = partial(main,list_coef,X)

    RUN = 20
    for _ in range(RUN):
        p = randint(1,20)
        runs = randint(1,20)

        pool = Pool(p)
        dict_data = pool.map(p_main, (n for _ in range(runs)))
        pool.close()
        pool.join()

        csv_columns = list(dict_data[0].keys()) + ['num_pool','runs']

        csv_file = "datasets.csv"
        try:
            if csv_file in os.listdir():
                type_file = 'a'
            else:
                type_file = 'w'
            with open(csv_file, type_file) as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                if type_file == 'w':
                    writer.writeheader()
                for data in dict_data:
                    data.update({'num_pool':p, 'runs': runs})
                    writer.writerow(data)
        except IOError:
            print("I/O error")
