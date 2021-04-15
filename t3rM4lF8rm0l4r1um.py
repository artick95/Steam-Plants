stop = 1

while (stop != 0):
    print(
        'how can I help?\n [1]Chemically Reactive Systems\n [2]Turbines (+Hydraulic)\n [3]Compressors\n [4]Steam Plant\n [5]Turbogas\n [6]Volumetric Compressors\n [7]Pumps \n [8]Noozles\n [9]FluidDynSym')

    formulaSheets = ['You fucked', 'Chemically Reactive Systems', 'Turbines (+Hydraulic)', 'Compressors',
                     'Steam Plant', 'Turbogas', 'Volumetric Compressors', 'Pumps', 'Q&A']

    formulaSheet_chosen = int(input())

    print(formulaSheets[formulaSheet_chosen])

    if (formulaSheet_chosen == 2):
        print(
            ' **Turbines&Hydraulic**\n **Francis**\n 0-1: Lwdis=c1^2/(1/phi^2-1)\n 1-2(relavive): Lwrun=w2^2/2*(1/PHI^2-1)\n 2-b: Lwdis)c^3/2\n 2-3: Ldraftt=c3^2/2*(1/phi^2+1)\n 01:vane\n 12:blade\n 23:drafttube\n')

    if (formulaSheet_chosen == 3):
        print(' **Compressors**\n beta'' < 90° su\n beta'' = 90° norm\n beta'' > 90° giù\n ')

    if (formulaSheet_chosen == 7):
        print(
            ' **Pump**\n etav=Qr/Qth\n etamh=Cth/Cr\n Pu=Q*deltap\n Pspesa=C*w\n **Motor**\n etav=Qth/Qr\n etamh=Cr/Cth\n Pu=C*w\n Pspesa=Q*deltap\n mdot=A*p1tot/sqqrt(RT1tot)*sqrt(2*gamma/(gamma-1)*((p/p1tot)^2/gamma-(p/p1tot)^(gamma+1/gamma)))  ')
    if (formulaSheet_chosen == 8):
        print(
            ' **Noozles**\n Renkine Hugoniot\n dA/A=(Ma^2-1)*dc/c\n **Simply Convergent**\n lambda=sqrt(gamma*(2/gamma+1)^(gamma+1)/(gamma-1))\n')

    if (formulaSheet_chosen == 9):
        print(' **FluidDynamicSym**\n **4PUmps**\n Hu/Hu0=(n/n0)^2=(Q/Q0)^2\n tauw=lambda/8*pho*c^2')

    if (formulaSheet_chosen == 3):
        print(' **Compressors**\n ')

    print('need something else?[1-yes][0-no]')
    stop = int(input())
    if (stop == 0):
        print('see you later ;)')
    else:
        print('thanks Master GoodLuck ;)')
