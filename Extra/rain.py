

print('have sigma or F?[F-1][sig-2]')
ans_sORf = int(input())

F_a = [ ]
F_min = [ ]
F_m = [ ]
F_max = [ ]
sigma_awave = [ ]
sigma_a = [ ]
sigma_m = [ ]
sigma_max = [ ]
sigma_min = [ ]


if ans_sORf == 1:
    print('how many rows you have?')
    n_row = int(input())
    for i in range(0, n_row):
        print('insert F max[kN]'+str(i+1))
        F_max.append(float(input()))
        print('insert F min[kN]'+str(i+1))
        F_min.append(float(input()))
        F_a.append((F_max[i]-F_min[i])*0.5)
        F_m.append((F_max[i]+F_min[i])*0.5)

    print('calculate sigma?[1-y][0-n]')
    ans_sigma = int(input())

    if ans_sigma == 1:
        print('insert k*F=sigma.k?')
        k = float(input())
        i = 1
        for Fa in F_a:
            sigma_a.append(Fa*k)
            i += 1
        i = 1
        for Fm in F_m:
            sigma_m.append(Fm*k)
            i += 1

    print('need normalize?[1-y][0-n]')
    ans_norm = int(input())

    if ans_norm == 1:
        print('insert sigmad-1[MPa]')
        sigmad_1 = float(input())

        print('insert Rm[MPa]')
        Rm = float(input())

        i = 0
        for sigmaa in sigma_a:
            sigma_awave.append(sigmaa/(1-sigma_m[i]/Rm))
            i += 1

    for j in range(0, n_row):
        print('Fa'+str(j+1)+'= '+str(F_a[j]))
        print('Fm'+str(j+1)+'= '+str(F_m[j]))
        print('sigma_a'+str(j+1)+'= '+str(sigma_a[j]))
        print('sigma_m'+str(j+1)+'= '+str(sigma_m[j]))
    
    print('sigma_aWave'+'= '+str(sigma_awave))
1
if ans_sORf == 2:

    print('how many rows you have?')
    n_row = int(input())
    for i in range(0, n_row):
        print('insert sigm max[kN]'+str(i))
        sigma_max.append(float(input()))
        print('insert sigma min[kN]'+str(i))
        sigma_min.append(float(input()))
        sigma_a.append((sigma_max[i]-sigma_min[i])*0.5)
        sigma_m.append((sigma_max[i]+sigma_min[i])*0.5)

    print('need normalize?[1-y][0-n]')
    ans_norm = int(input())

    if ans_norm == 1:
        print('insert sigmad-1[MPa]')
        sigmad_1 = float(input())

        print('insert Rm[MPa]')
        Rm = float(input())

        for q in range(0, n_row):
            sigma_awave.append(sigmaa/(1-sigma_m[q]/Rm))

    # for j in range(1, n_row+1):
    #     print('sigmaa'+str(j)+'= '+str(sigma_a[j]))
    #     print('sigmam'+str(j)+'= '+str(sigma_m[j]))
    #     print('sigma_aWave'+str(j)+'= '+str(sigma_awave[j]))
    print(sigma_a)
    print(sigma_m)
    print(sigma_awave)
