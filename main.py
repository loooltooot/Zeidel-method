import copy


def seidel(x, a, b):
    n = len(x)

    for number_of_eqution in range(n):
        d = b[number_of_eqution]

        for number_of_var in range(n):
            if number_of_eqution != number_of_var:
                d -= a[number_of_eqution][number_of_var] * x[number_of_var]

        x[number_of_eqution] = d / a[number_of_eqution][number_of_eqution]

    return x


amount_of_variebles = int(input("Enter amount of vars: "))
x = [0 for x in range(amount_of_variebles)]
a = [[0 for x in range(amount_of_variebles)]
     for x in range(amount_of_variebles)]
b = []
e = float(input("Enter infelicity: "))

for i in range(0, amount_of_variebles):
    b.append(float(input("Enter result of {} eqution: ".format(i + 1))))
    for j in range(0, amount_of_variebles):
        a[i][j] = float(input(
            "Enter {} coefficient of {} eqution: ".format(j + 1, i + 1)))

for i in range(20):
    isBiggerThanInfelicity = False
    pre_x = copy.deepcopy(x)
    x = seidel(x, a, b)

    for j in range(amount_of_variebles):
        if abs(x[j] - pre_x[j]) > e:
            isBiggerThanInfelicity = True
    print("\nResult of {} iteration: {}".format(i + 1, x))
    if isBiggerThanInfelicity is not True:
        break
