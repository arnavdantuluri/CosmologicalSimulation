# from numba.experimental import jitclass
# from numba import int32
# from numba import njit
import time

start = time.time()


# specs = [
#     ('x', int32)
# ]

# x = 0

# @njit
def func(n):
    for i in range(n):
        x = 0
        x += 1

n = 1000000

func(n)
print(f"time: {(time.time() - start ) * 1000} ms")