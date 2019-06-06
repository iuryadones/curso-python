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
        'n': n,
        'result': result,
        'timer': (end_time - started_time)
    }
    return dic

if __name__ == '__main__':
    n = 17
    coef = coef_rand(n)
    X = x_rand()
    RUN = 200000
    
    for _ in range(RUN):
        p = randint(1,100)
        runs = randint(1,100)
        
        p_main = partial(main,coef,X)

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
                    for i in range(len(x)):
                        data.update({f'coef_{i}': coef[i]})
                    data.update({'x': X,'num_pool':p, 'runs': runs})
                    writer.writerow(data)
        except IOError:
            print("I/O error")
