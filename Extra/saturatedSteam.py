# import pandas as pd
# import numpy as np

# df = pd.read_excel('table.xls', 'Sheet1')

T = [0.01, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 373.95
     ]
p = [0.0061165, 0.0087258, 0.012282, 0.017058, 0.023393, 0.031699, 0.04247, 0.05629, 0.073849, 0.09595, 0.12352, 0.15762, 0.19946, 0.25042, 0.31201, 0.38595, 0.47414, 0.57867, 0.70182, 0.84608, 1.0142, 1.4338, 1.9867, 2.7028, 3.6154, 4.7616, 6.1823, 7.9219, 10.028, 12.552, 15.549, 19.077, 23.196, 27.971, 33.469, 39.762, 46.923, 55.03, 64.166, 74.418, 85.879, 98.651, 112.84, 128.58, 146.01, 165.29, 186.66, 210.44, 220.64
     ]

h_l = [0, 21.02, 42.02, 62.98, 83.91, 104.83, 125.73, 146.63, 167.53, 188.43, 209.34, 230.26, 251.18, 272.12, 293.07, 314.03, 335.01, 356.01, 377.04, 398.09, 419.17, 461.42, 503.81, 546.38, 589.16, 632.18, 675.47, 719.08, 763.05, 807.43, 852.27, 897.63, 943.58, 990.19, 1037.6, 1085.8, 1135, 1185.3, 1236.9, 1290, 1345, 1402.2, 1462.2, 1525.9, 1594.5, 1670.9, 1761.7, 1890.7, 2084.3
       ]
h_h = [2500.9, 2510.1, 2519.2, 2528.3, 2537.4, 2546.5, 2555.5, 2564.5, 2573.5, 2582.4, 2591.3, 2600.1, 2608.8, 2617.5, 2626.1, 2634.6, 2643, 2651.3, 2659.5, 2667.6, 2675.6, 2691.1, 2705.9, 2720.1, 2733.4, 2745.9, 2757.4, 2767.9, 2777.2, 2785.3, 2792, 2797.3, 2800.9, 2802.9, 2803, 2800.9, 2796.6, 2789.7, 2779.9, 2766.7, 2749.6, 2727.9, 2700.6, 2666, 2621.8, 2563.6, 2481.5, 2334.5, 2084.3
       ]

u_l = [0, 21, 42, 63, 83.9, 104.8, 125.7, 146.6, 167.5, 188.4, 209.3, 230.2, 251.2, 272.1, 293, 314, 335, 356, 377, 398, 419.1, 461.3, 503.6, 546.1, 588.8, 631.7, 674.8, 718.2, 761.9, 806, 850.5, 895.4, 940.8, 986.8, 1033.4, 1080.8, 1129, 1178.1, 1228.3, 1279.9, 1332.9, 1387.9, 1445.3, 1505.8, 1570.6, 1642.1, 1726.3, 1844.1, 2015.7
       ]
u_h = [2374.9, 2381.8, 2388.6, 2395.5, 2402.3, 2409.1, 2415.9, 2422.7, 2429.4, 2436.1, 2442.7, 2449.3, 2455.9, 2462.4, 2468.9, 2475.2, 2481.6, 2487.8, 2494, 2500, 2506, 2517.7, 2528.9, 2539.5, 2549.6, 2559.1, 2567.8, 2575.7, 2582.8, 2589, 2594.2, 2598.3, 2601.2, 2602.9, 2603.1, 2601.8, 2598.7, 2593.7, 2586.4, 2576.5, 2563.6, 2547.1, 2526, 2499.2, 2464.4, 2418.1, 2351.8, 2230.3, 2015.7
       ]

v_l = [0.001, 0.001, 0.001, 0.001001, 0.001002, 0.001003, 0.001004, 0.001006, 0.001008, 0.00101, 0.001012, 0.001015, 0.001017, 0.00102, 0.001023, 0.001026, 0.001029, 0.001032, 0.001036, 0.00104, 0.001044, 0.001052, 0.00106, 0.00107, 0.00108, 0.001091, 0.001102, 0.001114, 0.001127, 0.001142, 0.001157, 0.001173, 0.00119, 0.001209, 0.00123, 0.001252, 0.001276, 0.001303, 0.001333, 0.001366, 0.001404, 0.001448, 0.001499, 0.001561, 0.001638, 0.00174, 0.001895, 0.002215, 0.003106

       ]
v_h = [205.99, 147.01, 106.3, 77.88, 57.76, 43.34, 32.88, 25.21, 19.52, 15.25, 12.03, 9.564, 7.667, 6.194, 5.04, 4.129, 3.405, 2.826, 2.359, 1.981, 1.672, 1.209, 0.8912, 0.668, 0.5085, 0.3925, 0.3068, 0.2426, 0.1938, 0.1564, 0.1272, 0.1043, 0.08609, 0.0715, 0.05971, 0.05008, 0.04217, 0.03562, 0.03015, 0.02556, 0.02166, 0.01834, 0.01547, 0.01298, 0.01078, 0.008802, 0.006949, 0.004954, 0.003106
       ]


s_l = [0, 0.0763, 0.1511, 0.2245, 0.2965, 0.3672, 0.4368, 0.5051, 0.5724, 0.6386, 0.7038, 0.768, 0.8313, 0.8937, 0.9551, 1.0158, 1.0756, 1.1346, 1.1929, 1.2504, 1.3072, 1.4188, 1.5279, 1.6346, 1.7392, 1.8418, 1.9426, 2.0417, 2.1392, 2.2355, 2.3305, 2.4245, 2.5177, 2.6101, 2.702, 2.7935, 2.8849, 2.9765, 3.0685, 3.1612, 3.2552, 3.351, 3.4494, 3.5518, 3.6601, 3.7784, 3.9167, 4.1112, 4.407

       ]
s_h = [9.1555, 9.0248, 8.8998, 8.7803, 8.666, 8.5566, 8.452, 8.3517, 8.2555, 8.1633, 8.0748, 7.9898, 7.9081, 7.8296, 7.754, 7.6812, 7.6111, 7.5434, 7.4781, 7.4151, 7.3541, 7.2381, 7.1291, 7.0264, 6.9293, 6.8371, 6.7491, 6.665, 6.584, 6.5059, 6.4302, 6.3563, 6.284, 6.2128, 6.1423, 6.0721, 6.0016, 5.9304, 5.8579, 5.7834, 5.7059, 5.6244, 5.5372, 5.4422, 5.3356, 5.211, 5.0536, 4.8012, 4.407
       ]


i = 0

print('do yo have pressure or temperature?[p-1][T-2]')
ans_pOrt = int(input())


def interpolator(x1, y1, x2, x3, y3):
    y2 = ((x2-x1)*(y3-y1))/(x3-x1)+y1
    # print('x1= '+str(x1))
    # print('x2= '+str(x2))
    # print('y1= '+str(y1))
    # print('x3= '+str(x3))
    value_Interpolated = y2
    return value_Interpolated


if ans_pOrt == 1:
    print('insert pressure[bar]')
    p_x = float(input())

    for pressure in p:
        if p[i] == p_x:
            print('found')
            print('P= '+str(p[i]))
            print('T= '+str(T[i]))
            print('v_l= '+str(v_l[i]))
            print('v_h= '+str(v_h[i]))
            print('h_l= '+str(h_l[i]))
            print('h_h= '+str(h_h[i]))
            print('s_l= '+str(s_l[i]))
            print('s_h= '+str(s_h[i]))
            break

        if p[i+1] > p_x and p[i] < p_x:
            print('interpolating....\n...')
            Tint = interpolator(p[i], T[i], p_x, p[i+1], T[i+1])

            v_lINT = interpolator(p[i], v_l[i], p_x, p[i+1], v_l[i+1])
            v_hINT = interpolator(p[i], v_h[i], p_x, p[i+1], v_h[i+1])

            h_lINT = interpolator(p[i], h_l[i], p_x, p[i+1], h_l[i+1])
            h_hINT = interpolator(p[i], h_h[i], p_x, p[i+1], h_h[i+1])

            s_lINT = interpolator(p[i], s_l[i], p_x, p[i+1], s_l[i+1])
            s_hINT = interpolator(p[i], s_h[i], p_x, p[i+1], s_h[i+1])

            print('found')
            print('P= '+str(p_x))
            print('T= '+str(Tint))
            print('v_l= '+str(v_lINT))
            print('v_h= '+str(v_hINT))
            print('h_l= '+str(h_lINT))
            print('h_h= '+str(h_hINT))
            print('s_l= '+str(s_lINT))
            print('s_h= '+str(s_hINT))
            break
        i += 1

elif ans_pOrt == 2:
    print('insert temperature[degC]')
    T_x = float(input())

    for temperature in T:
        if T[i] == T_x:
            print('found')
            print('T= '+str(T[i]))
            print('p= '+str(p[i]))
            print('v_l= '+str(v_l[i]))
            print('v_h= '+str(v_h[i]))
            print('h_l= '+str(h_l[i]))
            print('h_h= '+str(h_h[i]))
            print('s_l= '+str(s_l[i]))
            print('s_h= '+str(s_h[i]))
            break

        if T[i+1] > T_x and T[i] < T_x:
            print('interpolating....\n...')
            pint = interpolator(T[i], p[i], T_x, T[i+1], p[i+1])

            v_lINT = interpolator(T[i], v_l[i], T_x, T[i+1], v_l[i+1])
            v_hINT = interpolator(T[i], v_h[i], T_x, T[i+1], v_h[i+1])

            h_lINT = interpolator(T[i], h_l[i], T_x, T[i+1], h_l[i+1])
            h_hINT = interpolator(T[i], h_h[i], T_x, T[i+1], h_h[i+1])

            s_lINT = interpolator(T[i], s_l[i], T_x, T[i+1], s_l[i+1])
            s_hINT = interpolator(T[i], s_h[i], T_x, T[i+1], s_h[i+1])

            print('found')
            print('p= '+str(pint))
            print('T= '+str(T_x))
            print('v_l= '+str(v_lINT))
            print('v_h= '+str(v_hINT))
            print('h_l= '+str(h_lINT))
            print('h_h= '+str(h_hINT))
            print('s_l= '+str(s_lINT))
            print('s_h= '+str(s_hINT))
            break
        i += 1
