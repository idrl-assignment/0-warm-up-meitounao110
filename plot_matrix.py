# TODO: import ...
import numpy as np
import scipy

def generate_random_matrix(m, n):
    return np.mat(np.random.randint(0,2,(m,n)))


def save_matrix(matrix, file_name):
    scipy.misc.imsave(file_name,matrix)


if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
