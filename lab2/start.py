# download some w2v things
import io
import numpy as np
from heapq import heappush, heappushpop

def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())

    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = np.array([float(val) for val in tokens[1:]])  #map(float, tokens[1:])
    return data

if __name__=='__main__':
    print('hi')
    data = load_vectors('./small.vec')
    print('Loaded vectors')

    cur_vec = data['left']
    nearest = []

    for word in data.keys():
        if word != 'left':
            vec = data[word]
            dist = np.linalg.norm(cur_vec - vec)
            if len(nearest) < 10:
                heappush(nearest, (-dist, word))
            else:
                heappushpop(nearest, (-dist, word))

    print(nearest)
