# Test Data

seeds = [79, 14, 55, 13]

seed_to_soil_map = [[50, 98, 2], [52, 50, 48]]

soil_to_fertilizer_map = [[0, 15, 37], [37, 52, 2], [39, 0, 15]]

fertilizer_to_water_map = [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]]

water_to_light_map = [[88, 18, 7], [18, 25, 70]]

light_to_temperature_map = [[45, 77, 23], [81, 45, 19], [68, 64, 13]]

temperature_to_humidity_map = [[0, 69, 1], [1, 0, 69]]

humidity_to_location_map = [[60, 56, 37], [56, 93, 4]]


# Run Data
"""
seeds = [
    1367444651,
    99920667,
    3319921504,
    153335682,
    67832336,
    139859832,
    2322838536,
    666063790,
    1591621692,
    111959634,
    442852010,
    119609663,
    733590868,
    56288233,
    2035874278,
    85269124,
    4145746192,
    55841637,
    864476811,
    347179760,
]

seed_to_soil_map = [
    [873256303, 3438158294, 3400501],
    [3338810960, 408700040, 99469568],
    [876656804, 586381004, 55967396],
    [2937187724, 3352513245, 85645049],
    [3633224442, 4294716315, 250981],
    [4063203128, 3993405594, 231764168],
    [628606346, 884567853, 85164246],
    [1848085960, 2225191252, 328179324],
    [1686068310, 2992301693, 162017650],
    [1456962076, 179593806, 229106234],
    [0, 1520731987, 239660433],
    [2759350898, 1833519805, 177836826],
    [494634602, 642348400, 67929420],
    [3022832773, 758696310, 125871543],
    [3563677889, 4225169762, 69546553],
    [2637775123, 710277820, 48418490],
    [3148704316, 969732099, 112580498],
    [3261284814, 2623022420, 77526146],
    [489910414, 174869618, 4724188],
    [1187482559, 2700548566, 269479517],
    [713770592, 2139594657, 85596595],
    [850982693, 2970028083, 22273610],
    [932624200, 2013609609, 125985048],
    [799367187, 1082312597, 51615506],
    [3633475423, 3563677889, 429727705],
    [562564022, 3283192654, 66042324],
    [2181319395, 2553370576, 69651844],
    [2250971239, 1133928103, 386803884],
    [3438280528, 3349234978, 3278267],
    [2686193613, 513223719, 73157285],
    [239660433, 1760392420, 73127385],
    [487657436, 2011356631, 2252978],
    [312787818, 0, 174869618],
    [1058609248, 3154319343, 128873311],
    [2176265284, 508169608, 5054111],
]

soil_to_fertilizer_map = [
    [297032819, 3559164217, 26523093],
    [323555912, 2482284077, 316032053],
    [74171080, 3214516077, 10202585],
    [3176226661, 2368836568, 113447509],
    [2918425623, 1610395638, 257801038],
    [3933490965, 2171144546, 103908097],
    [1218064889, 55976272, 92496985],
    [2591090931, 0, 23819721],
    [1798514394, 148473257, 159960710],
    [2288143061, 1868196676, 302947870],
    [639587965, 3736262447, 6060799],
    [3609511269, 699586127, 40962058],
    [1575586870, 3249692350, 47378699],
    [1310561874, 2798316130, 265024996],
    [3650473327, 2308711439, 60125129],
    [1958475104, 483393073, 178493006],
    [259332771, 661886079, 37700048],
    [907741932, 980768687, 228854035],
    [1185908338, 23819721, 32156551],
    [3437918904, 3874038292, 163360770],
    [645648764, 3297071049, 262093168],
    [2648569448, 1432515231, 29635673],
    [1647939257, 3585687310, 150575137],
    [3710598456, 1209622722, 222892509],
    [2678205121, 740548185, 240220502],
    [84373665, 308433967, 174959106],
    [2614910652, 2275052643, 33658796],
    [1622965569, 3224718662, 24973688],
    [3289674170, 1462150904, 148244734],
    [3601279674, 3791635617, 8231595],
    [0, 3799867212, 74171080],
    [2136968110, 3063341126, 151174951],
    [1136595967, 3742323246, 49312371],
]

fertilizer_to_water_map = [
    [0, 478733437, 191375707],
    [2494518625, 3362803490, 180386054],
    [1605510969, 1985802816, 27464898],
    [3545871802, 2267467733, 385725819],
    [1580307385, 1113809296, 8335179],
    [2267467733, 4179194655, 34953467],
    [1588642564, 52640953, 16868405],
    [768087626, 69509358, 314799711],
    [2835042306, 4002148814, 177045841],
    [320920516, 1122144475, 447167110],
    [1082887337, 670109144, 443700152],
    [3218018460, 3543189544, 156036618],
    [1921732119, 1569311585, 321765324],
    [1632975867, 384309069, 40704472],
    [1526587489, 425013541, 53719896],
    [3140697718, 2802291105, 77320742],
    [1726321292, 1891076909, 94725907],
    [3070918618, 2732512005, 69779100],
    [1673680339, 0, 52640953],
    [3374055078, 3830332090, 171816724],
    [2755723853, 2653193552, 79318453],
    [3012088147, 3242981522, 58830471],
    [2363412697, 3699226162, 131105928],
    [1821047199, 2013267714, 100684920],
    [2302421200, 3301811993, 60991497],
    [191375707, 2113952634, 129544809],
    [3931597621, 2879611847, 363369675],
    [2674904679, 4214148122, 80819174],
]

water_to_light_map = [
    [3219102205, 2181622520, 201394006],
    [920319894, 2563844887, 124975374],
    [739491533, 2383016526, 180828361],
    [653894144, 112244681, 85597389],
    [3420496211, 0, 112244681],
    [3657404452, 197842070, 151065180],
    [2385949305, 1028427888, 284402820],
    [3532740892, 1312830708, 124663560],
    [379827855, 754361599, 274066289],
    [0, 374533744, 379827855],
    [1070921762, 1437494268, 744128252],
    [1815050014, 3237570341, 372982025],
    [2670352125, 2688820261, 548750080],
    [1045295268, 348907250, 25626494],
    [2188032039, 3610552366, 197917266],
]

light_to_temperature_map = [
    [2153765789, 597465407, 100160624],
    [2781845200, 2181361650, 40610317],
    [667326513, 1345068833, 191904517],
    [2473693610, 3180449558, 308151590],
    [3613083869, 2293229230, 341401182],
    [1062907936, 2938916666, 34067323],
    [1451871003, 2221971967, 71257263],
    [3954485051, 4137063579, 102141117],
    [4192502901, 3838513492, 49627103],
    [1389629967, 2876675630, 62241036],
    [1593277643, 2972983989, 143397067],
    [859231030, 2634630412, 203676906],
    [4056626168, 790528713, 68145539],
    [1523128266, 2838307318, 38368312],
    [503645468, 3488601148, 84794865],
    [1333867367, 4239204696, 55762600],
    [2902105909, 1961894500, 219467150],
    [3268371481, 858674252, 266627384],
    [2253926413, 1125301636, 219767197],
    [4124771707, 3888140595, 67731194],
    [1159014133, 3663660258, 174853234],
    [3121573059, 1536973350, 56534177],
    [4242130004, 1593507527, 52837292],
    [3534998865, 697626031, 78085004],
    [1096975259, 503645468, 62038874],
    [588440333, 3116381056, 64068502],
    [2052224391, 3955871789, 101541398],
    [3178107236, 3573396013, 90264245],
    [1736674710, 1646344819, 315549681],
    [1561496578, 565684342, 31781065],
    [2822455517, 4057413187, 79650392],
    [652508835, 775711035, 14817678],
]

temperature_to_humidity_map = [
    [539306376, 906765326, 12587914],
    [0, 164719538, 374586838],
    [3299714596, 2417002864, 137882274],
    [3574681727, 1862289721, 10695948],
    [1377359247, 1111480860, 147188226],
    [2546515862, 3738486436, 38563842],
    [2519543212, 3564238204, 26972650],
    [1619134727, 3777050278, 31686173],
    [551894290, 728868054, 177897272],
    [3834998050, 3919246788, 238635651],
    [729791562, 919353240, 625999],
    [1524547473, 3627710187, 94587254],
    [2399595894, 3277935618, 48769514],
    [1340859914, 3591210854, 36499333],
    [2585079704, 2011159197, 185411491],
    [3723551203, 3452791357, 111446847],
    [2895131743, 2873352765, 404582853],
    [374586838, 0, 164719538],
    [1776907125, 1258669086, 373340162],
    [2881001532, 2859222554, 14130211],
    [2217932998, 2606381854, 181662896],
    [2166436282, 2554885138, 51496716],
    [2448365408, 2788044750, 71177804],
    [1650820900, 3326705132, 126086225],
    [1110579441, 1632009248, 230280473],
    [3437596870, 4157882439, 137084857],
    [730417561, 539306376, 189561678],
    [4294065877, 1110579441, 901419],
    [2150247287, 3722297441, 16188995],
    [2770491195, 3808736451, 110510337],
    [3585377675, 1872985669, 138173528],
    [4073633701, 2196570688, 220432176],
]

humidity_to_location_map = [
    [3656475570, 3037182697, 7397903],
    [682722270, 547529272, 780546181],
    [266636474, 1328075453, 316323944],
    [1591860664, 3642496089, 50700992],
    [1642561656, 266636474, 280892798],
    [1923454454, 1644399397, 1264527167],
    [3979139381, 3408096655, 6045369],
    [3663873473, 4002979627, 291987669],
    [3955861142, 3208017899, 23278239],
    [582960418, 3414142024, 99761852],
    [3187981621, 3231296138, 176800517],
    [3364782138, 3044580600, 163437299],
    [1463268451, 3513903876, 128592213],
    [3528219437, 2908926564, 128256133],
    [4175159701, 3693197081, 119807595],
    [3985184750, 3813004676, 189974951],
]
"""
