# 1. Вычислить число пи c заданной точностью *d*
# *Пример:*
# - при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

# 3,1415926535 8979323846


def calculation_pi(d: float):
    pi, sign, m = 3, 1, 2
    while abs(pi - (pi + sign * 4 / (m**3 + 3 * m**2 + 2 * m))) > 10**(-d):
        pi = pi + sign*4 / (m**3 + 3 * m**2 + 2 * m)
        sign = -1 * sign
        m = m + 2
    return round((pi + (pi + sign*4 / (m**3 + 3 * m**2 + 2*m))) / 2, d)


input_value = input('Введите d для точности вычислений например 0.0001\n')
d = len(str(input_value).split('.')[1])
pi = calculation_pi(d)
print(f'С точностью d={input_value}, число {pi=}; ')
