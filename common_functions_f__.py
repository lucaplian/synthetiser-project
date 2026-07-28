import numpy as np 

def generate_embedings_index():
    embeddings_index = {}


    f = open('input/numberbatch-en.txt')

    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs
            
    f.close()
    return embeddings_index