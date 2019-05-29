from multiprocessing import Pool
from random import random
from random import randint
from timeit import default_timer as timer
import csv
import os


def coef_rand(n):
    list_coef = [random() for _ in range(n)]
    return list_coef

def x_rand(n):
    list_x = [random() for _ in range(n)]
    return list_x

def func(list_coef,list_x):
    result = 0
    for n, (coef, x) in enumerate(zip(list_coef, list_x)):
        result +=  coef * x ** n
    return result

def main(n):
    coef = coef_rand(n)
    x = x_rand(n)
    started_time = timer()
    result = func(coef,x)
    end_time = timer()

    dic = {
        'n': n,
        'result': result,
        'timer': (end_time - started_time)
    }
    for i in range(len(x)):
        dic[f'coef_{i}'] = coef[i]
        dic[f'x_{i}'] = x[i]
    return dic

if __name__ == '__main__':
    for _ in range(1000):
        p = randint(1,20)
        runs = randint(1,20)
        n = 2

        pool = Pool(p)
        dict_data = pool.map(main, (n for _ in range(runs)))
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
