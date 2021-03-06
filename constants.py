
COUPLING_TYPE_STATS=[
    #type   #mean, std, min, max
    '1JHC',  94.97236504744275,   18.276733175215483,   66.6008,   204.8800,
    '2JHC',  -0.27153255445260427,    4.5227716549161245,  -36.2186,    42.8192,
    '3JHC',   3.6882680755559987, 3.070535818158166,  -18.5821,    76.0437,
    '1JHN',  47.46033350576121, 10.904271524567221,   24.3222,    80.4187,
    '2JHN',   3.118677977878313, 3.6690875751571723,   -2.6209,    17.7436,
    '3JHN',   0.9907631467972438, 1.3162109271658124,   -3.1724,    10.9712,
    '2JHH', -10.287318535034318, 3.9776350423190183,  -35.1761,    11.8542,
    '3JHH',  4.772346592250247, 3.7055315330498892,   -3.0205,    17.4841,
]
NUM_COUPLING_TYPE = len(COUPLING_TYPE_STATS)//5

COUPLING_TYPE_MEAN = [ COUPLING_TYPE_STATS[i*5+1] for i in range(NUM_COUPLING_TYPE)]
COUPLING_TYPE_STD  = [ COUPLING_TYPE_STATS[i*5+2] for i in range(NUM_COUPLING_TYPE)]
COUPLING_TYPE      = [ COUPLING_TYPE_STATS[i*5  ] for i in range(NUM_COUPLING_TYPE)]
