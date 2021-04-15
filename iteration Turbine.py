import math

print('insert p0[bar]')
p0 = float(input())

print('insert pk[bar]')
pk = float(input())

print('insert (pk/p0)critical[-]')
ratio_critical = float(input())

print('insert mass flow rate[kg/s]')
m = float(input())

print('insert v0[m^3/kg]')
v0 = float(input())

L_greek = 1/(math.sqrt(1 - ((pk / p0 - ratio_critical) / (1 - ratio_critical))**2)) * m * math.sqrt(p0 * v0) / p0

print(str(L_greek) + 'kg/s*sqrt(bar*m^3/kg)')
print(str(L_greek*1e-3*3600) + 't/h*sqrt(bar*m^3/kg)')
