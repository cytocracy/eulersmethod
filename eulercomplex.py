print("Enter dy/dx")
dydx = input()
f = lambda x, y: eval(dydx)

print("Enter given x")
x1 = eval(input())

print("Enter given y")
y1 = eval(input())

print("Enter dx")
dx = eval(input())

print("Enter x to find y")
x2 = eval(input())

print("\n----------------------\n")
while(x1 < x2):
    print("pt: (", x1, ",", y1, ")")
    y1 = y1 + f(x1, y1)*dx
    x1 = x1 + dx

print("Final pt: (", x2, ",", y1, ")")