import consts

print(__name__)
print(f"addr(N)={hex(id(consts.N))}")
print(f"addr(L)={hex(id(consts.L))}")

consts.N = 20
consts.L.append(2)

print(f"addr(N)={hex(id(consts.N))}")
print(f"addr(L)={hex(id(consts.L))}")

print()
