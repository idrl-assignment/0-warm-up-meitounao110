# TODO: import ...
import numpy as np
import imageio


def generate_random_matrix(m, n):
    matrix = np.random.randint(0, 2, (m, n))
    #matrix = np.mat(matrix)
    return matrix


def save_matrix(matrix, file_name):
    imageio.imwrite(file_name, matrix)


if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    print(type(matrix))
    save_matrix(matrix, "example.jpg")
