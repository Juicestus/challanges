#!/usr/bin/env python3

FILENAME = 'data.csv'

mean = lambda a : sum(a) / len(a)

array_mult = lambda a, b : [aa * bb for aa, bb in zip(a, b)]

def best_fit(xs, ys):
    m1 = (mean(xs) * mean(ys)) - mean(array_mult(xs, ys))
    m2 = (mean(xs) * mean(xs)) - mean(array_mult(xs, xs))
    m = m1 / m2

    b = mean(ys) - m * mean(xs)
    return round(m, 2), round(b, 2)

def read_file_for_points(filename):
    xs = []
    ys = []
    with open(filename, 'r') as f:
        for l in f: # \n
            l = l.replace(' ', '')
            e = l.split(',')
            xs.append(float(e[0]))
            ys.append(float(e[1]))
    return xs, ys

if __name__ == '__main__':
    xs, ys = read_file_for_points(FILENAME)
    m, b = best_fit(xs, ys)
    print(f'The line of best fit is 𝑦 ≈ {m}𝑥 + {b}')

