from os import listdir
from time import time


def knapsack(K, C, N, V, P):

    def _knapsack(k, c, n):
        if c < 0 or n == 0 and k > 0:
            return - float("infinity")
        if k == 0:
            return 0

        if (k, c, n) in mem:
            return mem[k, c, n][0]
        p = P[n-1]
        mem[k, c, n] = max(
                    (V[n - 1] * d + _knapsack(k - d,  c - p * d, n - 1), (k - d,  c - p * d, n - 1), d)
                    for d in (0, 1)
                    )
        return mem[k, c, n][0]
    mem = {}
    sol = []
    value = _knapsack(K, C, N)
    if value == - float("infinity"):
        return "NO SOLUTION"
    k_prev, c_prev, n_prev = K, C, N
    while n_prev > 0 and k_prev > 0:
        data = mem[k_prev, c_prev, n_prev]
        if data[2] == 1:
            sol.append(n_prev - 1)
        k_prev, c_prev, n_prev = data[1]
    sol.reverse()
    weight = C - c_prev
    return value, weight, sol


def reader():
    for file in listdir("test"):
        with open("test/"+file, "r") as f:
            if file[-1] == 'i':
                print(file)
                K, C, N = (int(letter) for letter in f.readline().split())
                V = [int(letter) for letter in f.readline().split()]
                P = [int(letter) for letter in f.readline().split()]
                yield True, K, C, N, V, P
            else:
                yield False, f.read()


if __name__ == "__main__":
    start_time = time() #Obtenemos el tiempo de inicio

    for file in reader():
        if file[0]:
            print("ANSWER: ")
            K, C, N, V, P = file[1:]
            ans = knapsack(K, C, N, V, P)
            if ans == "NO SOLUTION":
                print(ans)
            else:
                print(ans[0])
                print(ans[1])
                objects = ""
                for elem in ans[2]:
                    objects += str(elem) + " "
                print(objects)
        else:
            print("EXPECTED: ")
        print(file[1])
    elapsed_time = time() - start_time #Calculamos el tiempo de ejecucion
    print("\nElapsed time: %.10f seconds." % elapsed_time)
