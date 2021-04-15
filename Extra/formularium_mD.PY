
stop = 0

while(stop != 1):
    print(
        'how can I help? \n [1]FKM \n [2]Fracture \n [3]Bolts \n [4]Gears \n [5]LCF\n [6]Bearings\n [7]Fun Facts')

    formulaSheets = ['You fucked', 'FKM', 'Fracture', 'Bolts',
                     'Gears', 'LCF', 'Bearings', 'Fun Facts']

    formulaSheet_chosen = int(input())

    print(formulaSheets[formulaSheet_chosen])

    if (formulaSheet_chosen == 1):
        print(
            '\n\n\n\n **FKM&Fatigue**\n Fail-Safe:keep changing like human bones\n Safe-Life:Car Tier\n Wft=Wfb*2\n Wfb=pi*d^3/32\n FKM: sigmad=sigmad-1-sigmad-1/(alfa*Rm)*sigmam\n Msigma=aM*e-3Rm,c+bM\n aM=0.355 bM=-0.1 Rm in MPa\n sigmab--> totally alternate\n sigmatc-->totally mean\n tau-->totally mean\n Ix=pi*d^4/64\n Ip=Ix*2\n ntot_failure = 1/sum(alfai/Ni) just count the failure cycles\n Heibach extension e6-e8\n Larson Miller\n P=(T+460)/(C+logtrapture)\n M.H\n P=(teta-teta0)/(logt-logt0)\n Bousinnessque \n du=(1-ni^2)/E*F/rb\n sigma increase benchmarks get closer and final rought area gets bigger XD\n')
        print('\n\n\ngot you served thank you next!')

    if (formulaSheet_chosen == 2):
        print(
            '\n\n\n\n **Rapid Fracture** \n SF= Kic/Ki\n Ki=Ysqrt(a)*sigma\n sigma=P/(W*B)\n B: depth\n W: Base\n **Yield Safety**\n SFy=Rpo2/sigma\n sigma =P/((w-2a)*B)\n **Dimensioning**\n B=Max(Byielding,Brapid_fracture)')
        print('\n\n\ngot you served thank you next!')

    if (formulaSheet_chosen == 3):
        print(
            '\n\n\n\n **BOLTSz** \n min(muK_max,muG_min)\n Fm,max=.9Rp02As/sqrt(1+k^2)\n k=2/ds*(.16*x+.58*d2*muG)\n Amin=(3%4)Fa/Rp02\n M16-->dn=16mm\n n=deltapk/deltap=La/Lk\n Ma=Fm*(0.16p+0.58*muG+Dkm/2*muK)\n Wt=pi*d^3/16\n k=tau/sigma\n SF=sigma_lim/sigma_a\n sigma_lim=sigma_a**0.9\n Proof load: Fp = As*Sp\n Yield Strenght: F= As*Rp02\n delta_sk=lsk/Es*An: sull cuore del nut\n ls=dn*(0.5-->exagonal or 0.4-->socket cap\n deltaGM=deltaG+deltaM\n deltaG=lG/Es*Ad3\n deltaM=lm/Ex*An\n lm=dn*(0.33dn-->tapped thread or 0.4--> botted joint\n lG=0.5*dn\n Fsa=Fa*deltap/(deltas+deltap)\n Fpa=Fa*deltas/(deltas+deltap)\n deltaFs=deltai/(deltas+deltap)\n alfaA=Fm,max/Fm,min')
        print('\n\n\ngot you served thank you next!')

    if (formulaSheet_chosen == 4):
        print(
            '\n\n\n\n **GEARSz**\n i=w1/w2=r2/r1=rb2/rb1=z2/z1=M2out/M1in\n m=2r/z\n p=pi()*m\n epsilonalfa=AE/pb\n z>=2/sinalfa\n AC<T1C (condition for minimum teeths:)\n z>=2/sin(alfat)*cos(beta)\n vn=w1*0T1(orT2)\n vt=T1E*w1(p(curvature)*w) \n Almen: sigmaH*vg*Ah*mu \n DIN --> epsilon_alfa>1, knotch,x,m\n ISO epsilon_alfa>1\n Lewis-->epsilonalfa=1, only Ft no notch\n w2^2*p2a*p2e=w1p1a*p1e (p is the curvature T1 to point)\n zetaA=-zetaE\n invalfaw= inv alfa+2*(x1+x2)/(z1+z2)*tanalfa\n invalfa=tanalfa-alfa(alfa in radiants because tan spouts radiants)\n tanalfat = tan alfan/cosbeta\n tanbetab = tan beta*cosalfat\n epsilon alfa = AE/(pb or pt*cosalfat)\n epsilonbeta = b*tanbetab/(pt*coslafatat)\nepsilon = epsilonalfa+epsilonbeta\n b>3%4*pt\n pn=pt*cosbeta\n mn=mt*cosbeta\n radd=r+mn\n **Bendinging Fatigue Verification**\n wft=w*Ke*Kv*Kfalfa*Kfbeta\n sigmaF=wft/mn*Yf*Yepsilon*Ybeta\n Sf= sigmafd/digmaf>)1.8\n w=Ft/b\n **Surface Fatigue Wear Verification**\n sigmah=sqrt(wft*(u+1/(u*d1))*Zh*Zh*Zepsilon)\n Sh=sigmahd/sigmah>=(z1>20-->1.25 orz1<=20-->1.4)\n  ')
        print('\n\n\ngot you served thank you next!')

    if (formulaSheet_chosen == 5):
        print(
            '\n\n\n\n **LCF** \n Basquin-Coffin \n epsilon_a=sigma_f/E*(2Nf)^b+epsilon_f(2Nf)^c\n Moffin: \n epsilon_a=sigma_f/E*(1-sigma_m/sigma_f)*(2Nf)^b+epsilon_f*(1-sigma_m/sigma_f)^c/b*(2Nf)^c\n delta_epsilon = delta_epsilon_e +delta epsilon_p\n SF=epsilon_lim/epsilon_p')
        print('\n\n\ngot you served thank you next!')

    if (formulaSheet_chosen == 6):
        print(
            '\n\n\n\n **BEARINGS** \n F=K(deltai+deltao)^n\n n=1.1-->ball bearing\n n=1.5-->cylinder bearing\n p=3-->ball bearing\n p=10/3-->cylinder bearing\n pmax=1.61ReH-->ball bearing\n pmax=1.67Reh-->cylinder bearing\n z/b=0.48-->ball bearing\n z/b=0.78-->cylinder bearingdeltatot=F^1/n*(1/Kin^1/n+1/Kout^1/n)\n min(gmin%gmax)\n k=ni/ni1\n ni: real viscosity\n ni1: required viscosity\n F0=0.5R/cosalfa+0.5A/sin(alfa)\n C0/P0>=S0\n deltaphi=deltar*cosphi*cosalfa+deltaa*sinalfa\n deltaphi=deltarcosphi-g/2\n convex:circle from inside+\n concave: raceway -\n **Palmgreen Provavility**\n deltaphi= zita*a*di/2*z0*deltaphi\n S=Si*So\n S=e^-(J0+Ji)*R^r+L^e\n \n\n **Load Cases**\n I-a-->deltaa=0 phimax=pi/2 like olimpic flag vertical \n I-b-->deltaa=deltar/tgalfa phimax=pi small circle and big circle touch at the top like a toung \n II--> deltaa>deltar/tanalafa phimax=pi small circle in big circle\n Pu:fatigue limit \n eta: contamination factor\n L=a1 askf*(C/P)^p\n L_hour=Le6/(60*n)\n **no axial ONLY RADIAL** \n g=0-->Fcontact=4.08*Fr/Z\n g=0.6deltar--> Fcontact=5*Fr/z ')
        print('\n\n\ngot you served thank you next!')

    if (formulaSheet_chosen == 7):
        print(
            '\n\n\n\n **Fun Facts**\n What is the difference between mechanical engineers and civil engineers?Mechanical engineers build weapons. Civil engineers build targets.\n ')
        print(
            'Who designed the human body?\nThree engineering students were gathered together discussing the possible designers of the human body.\nOne said, "It was a mechanical engineer. Just look at all the joints!"\nAnother said, "No, it was an electrical engineer. The nervous system has many thousands of electrical connections."\nThe last one said, "No, actually it had to have been a civil engineer. Who else would run a toxic waste pipeline through the recreational area?"')
        print('\n\n\ngot you served thank you next!')
    print('\n can I serve you something else Sir?[0-yes][1-no]')
    stop = int(input())
    if(stop == 0):
        print('\n great to see you again master\n\n')
    else:
        print('thanks for coming by Ill be always there if you need me you know where to find me\n\n GoodLuck ;)')
