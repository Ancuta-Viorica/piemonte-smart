import math
from operator import mul

v1=[0.1, 0.2, 0.0021]
v2=[0.3, 0.0014, 2.54]

print("hello")


class prova():
    inp = int(input("numeri"))

    def d0(v1, v2):
        """
        d0 is Nominal approach:
        multiply/add in a loop
        """
        out = 0
        for k in range(len(v1)):
            out += v1[k] * v2[k]
        return out
        #out=d0(v1,v2)
        print("outt",out)

    # def d1(v1, v2):
    #     """
    #     d1 uses a map
    #     """
    #     return sum(map(mul, v1, v2))