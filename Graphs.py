from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pickle
import glob
import csv
import os



def distance(x1, x2, y1, y2):
	return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def midpoint(x1, y1, x2, y2):
    return [(x1 + x2)/2, (y1 + y2)/2]


fig8 = plt.figure(8)
ax8 = fig8.add_subplot(111, projection='3d')
fig9 = plt.figure(9)
ax9 = fig9.add_subplot(111, aspect='equal')

sample = 1
car1_x_test = []
car1_y_test = []
car2_x_test = []
car2_y_test = []

car1_x_predict= []
car1_y_predict = []
car2_x_predict = []
car2_y_predict = []

dist_array = []
angle_array = []
light_array = []

gen_x_array = []
gen_y_array = []
gen_light_array =[]
gen_dist_array = []
gen_angle_array = []

gen_x_array2 = []
gen_y_array2 = []
gen_light_array2 =[]
gen_dist_array2 = []
gen_angle_array2 = []

denorm_gen_xylsd = []
denorm_gen_lsd = []

counter = 5

start_array = ['light','dist','angle', 'light2', 'dist2', 'angle']
start_x = 0
start_y = 0

normed_arr = []
denorm_arr = []

ground_truth_csv = []
ground_truth_x1 = []
ground_truth_y1 = []
ground_truth_x2 = []
ground_truth_y2 = []
ground_truth_l = []
ground_truth_s = []
ground_truth_d = []
ground_truth_2l = []
ground_truth_2s = []
ground_truth_2d = []

gen_speed1 = []
gen_speed2 = []
gen_dir1 = []
gen_dir2 = []

gen_x_ten = []
gen_y_ten = []
gen_x_ten2 = []
gen_y_ten2 = []


def denormalizer(val, mi, ma):
	denorm = val*(ma-mi)+mi
	return denorm


#nextXY = nextPoint(start_x, start_y, start_dist, start_angle)
#nextXY2 = nextPoint(start_x2, start_y2, start_dist2, start_angle2)

#Opens and loads a pickle file

for filename in glob.glob('simulator_data_d1.csv'):

	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		#print(filename)
		for row in reader:
			temp = []
			x1 = denormalizer(float(row[1]), -56.5545701913, -15.904584042)
			y1 = denormalizer(float(row[2]), -38.8697274136, 5.78484721801)
			l1 = denormalizer(float(row[3]), 1, 3)
			s1 = denormalizer(float(row[4]), 0.0, 12.8737431131)
			d1 = denormalizer(float(row[5]), -3.13358524866, 3.14159265359)
			x2 = denormalizer(float(row[7]), -95.3585481006, 24.968774703)
			y2 = denormalizer(float(row[8]), -78.4804293362, 28.7612966226)
			l2 = denormalizer(float(row[9]), 1, 3)
			s2 = denormalizer(float(row[10]), 0.0, 19.2470832483)
			d2 = denormalizer(float(row[11]), -3.13377098469, 3.14159265359)

			temp.append(float(x1))
			temp.append(float(y1))
			temp.append(float(l1))
			temp.append(float(s1))
			temp.append(float(d1))
			temp.append(float(x2))
			temp.append(float(y2))
			temp.append(float(l2))
			temp.append(float(s2))
			temp.append(float(d2))
			normed_arr.append(temp)
			temp = []

for filename in glob.glob('ground_truth.csv'):

	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		#print(filename)
		for row in reader:
			temp = []
			c1 = row[0]
			x1 = row[1]
			y1 = row[2]
			l1 = row[3]
			s1 = row[4]
			d1 = row[5]
			c2 = row[6]
			x2 = row[7]
			y2 = row[8]
			l2 = row[9]
			s2 = row[10]
			d2 = row[11]
			temp.append(float(c1))
			temp.append(float(x1))
			ground_truth_x1.append(float(x1))
			temp.append(float(y1))
			ground_truth_y1.append(float(y1))
			temp.append(float(l1))
			ground_truth_l.append(float(l1))
			temp.append(float(s1))
			ground_truth_s.append(float(s1))
			temp.append(float(d1))
			ground_truth_d.append(float(d1))
			temp.append(float(c2))
			temp.append(float(x2))
			ground_truth_x2.append(float(x2))
			temp.append(float(y2))
			ground_truth_y2.append(float(y2))
			temp.append(float(l2))
			ground_truth_2l.append(float(l2))
			temp.append(float(s2))
			ground_truth_2s.append(float(s2))
			temp.append(float(d2))
			ground_truth_2d.append(float(d2))
			ground_truth_csv.append(temp)
			temp = []


with open ('seed_gt.pkl', 'rb') as f:
	test = pickle.load(f)

	#test = test[0:1000]

with open ('5layer_Dir_1.6mse.pkl', 'rb') as f:
	predict = pickle.load(f)

with open ('generated_para_lsd_0.2mse.pkl', 'rb') as f:
	gen = pickle.load(f)

#np.savetxt("CSVdata\Data_denormed_of_final.csv", normed_arr, delimiter=",")
#with open ('lsp.pkl', 'rb') as f:
	#lsp = pickle.load(f)

	#lsp.insert(0,start_array1)
gen_50 = gen.tolist()
test_normed_csv = np.asarray(test)
#np.savetxt("CSVdata\Data_denormed_test.csv", test_normed_csv, delimiter=",")

# Add generated data to gen_li. Replace first data in the first index with the data from the last index of seed
gen_li = [[0.00000000e+00, 0.00000000e+00, 4.99361992e-01, 1.00000000e+00, 1.55850276e-02, 2.49065191e-01], [0.017823606729507446, -0.003981366753578186, 0.5068355798721313, 0.9739816188812256, 0.020607419312000275, 0.25599998235702515], [0.03674830496311188, -0.003629133105278015, 0.5133415460586548, 0.949859082698822, 0.021719858050346375, 0.26121625304222107], [0.057051897048950195, -0.003602251410484314, 0.5195087194442749, 0.9259974360466003, 0.02401401847600937, 0.2663509249687195], [0.07769735902547836, -0.004236236214637756, 0.5251985788345337, 0.9036086201667786, 0.025865502655506134, 0.27064356207847595], [0.09828156977891922, -0.0037170201539993286, 0.5305746793746948, 0.8823276162147522, 0.02724292129278183, 0.27430492639541626], [0.1190292239189148, -0.003485754132270813, 0.5355374813079834, 0.8620851635932922, 0.02853802964091301, 0.2774023115634918], [0.13979317247867584, -0.003116026520729065, 0.5402252674102783, 0.8428088426589966, 0.029629796743392944, 0.27992507815361023], [0.16052629053592682, -0.002487778663635254, 0.5446302890777588, 0.8243846893310547, 0.03047901764512062, 0.2819489538669586], [0.18123285472393036, -0.001882597804069519, 0.5487795472145081, 0.806755006313324, 0.031209036707878113, 0.28350162506103516], [0.20182988047599792, -0.0011708736419677734, 0.5527091026306152, 0.7898701429367065, 0.031769175082445145, 0.28460967540740967], [0.22226834297180176, -0.0003882497549057007, 0.5564296245574951, 0.7736819982528687, 0.032186903059482574, 0.2853093445301056], [0.2424909472465515, 0.00041209161281585693, 0.5599607229232788, 0.7581621408462524, 0.03248715028166771, 0.2856239974498749], [0.2624249756336212, 0.00125199556350708, 0.5633189678192139, 0.743285596370697, 0.03266812860965729, 0.2855783998966217], [0.2820059061050415, 0.002104818820953369, 0.5665152072906494, 0.7290321588516235, 0.03274789825081825, 0.2851966321468353], [0.30116450786590576, 0.002957060933113098, 0.5695620775222778, 0.7153881788253784, 0.032737769186496735, 0.2844993472099304], [0.31983163952827454, 0.0038048624992370605, 0.5724695920944214, 0.7023423910140991, 0.032646629959344864, 0.28350749611854553], [0.33794301748275757, 0.0046348124742507935, 0.5752465724945068, 0.6898850202560425, 0.03248674049973488, 0.28224074840545654], [0.35543757677078247, 0.005439937114715576, 0.5779013633728027, 0.6780073642730713, 0.032267630100250244, 0.2807175815105438], [0.37226006388664246, 0.0062143802642822266, 0.5804415941238403, 0.6667003631591797, 0.03199893236160278, 0.2789560854434967], [0.3883621394634247, 0.006951585412025452, 0.582874059677124, 0.655954122543335, 0.031690292060375214, 0.2769739627838135], [0.4037034511566162, 0.0076477378606796265, 0.585205078125, 0.6457576155662537, 0.031350113451480865, 0.2747877538204193], [0.418252170085907, 0.00829954445362091, 0.5874406099319458, 0.6360979676246643, 0.03098660707473755, 0.2724139392375946], [0.431985467672348, 0.008904710412025452, 0.5895862579345703, 0.626960039138794, 0.03060726821422577, 0.2698686420917511], [0.444889098405838, 0.009462133049964905, 0.5916472673416138, 0.6183271408081055, 0.030218757688999176, 0.2671673893928528], [0.4569583535194397, 0.009971454739570618, 0.5936288237571716, 0.6101798415184021, 0.029827255755662918, 0.26432567834854126], [0.4681967794895172, 0.010433375835418701, 0.5955356955528259, 0.6024975776672363, 0.02943800762295723, 0.26135799288749695], [0.47861555218696594, 0.0108489990234375, 0.5973724126815796, 0.5952578783035278, 0.029055733233690262, 0.25827881693840027], [0.488232284784317, 0.011220291256904602, 0.5991430878639221, 0.5884369611740112, 0.028684597462415695, 0.2551024258136749], [0.49707135558128357, 0.011549517512321472, 0.6008520126342773, 0.5820105075836182, 0.028328049927949905, 0.2518421411514282], [0.5051611661911011, 0.01183958351612091, 0.602502703666687, 0.5759532451629639, 0.027989041060209274, 0.24851128458976746], [0.5125349760055542, 0.01209348440170288, 0.6040987968444824, 0.5702398419380188, 0.027669765055179596, 0.24512261152267456], [0.5192285776138306, 0.012314528226852417, 0.6056433916091919, 0.5648458003997803, 0.02737225592136383, 0.24168816208839417], [0.5252792835235596, 0.012506097555160522, 0.6071394681930542, 0.5597460269927979, 0.027098018676042557, 0.2382199466228485], [0.5307266712188721, 0.012671738862991333, 0.608589231967926, 0.5549172163009644, 0.026848305016756058, 0.2347288727760315], [0.5356103777885437, 0.01281479001045227, 0.6099951267242432, 0.5503363609313965, 0.02662377431988716, 0.23122575879096985], [0.5399696826934814, 0.012938812375068665, 0.6113591194152832, 0.5459820032119751, 0.026425011456012726, 0.22772063314914703], [0.5438429713249207, 0.013046905398368835, 0.6126828193664551, 0.5418342351913452, 0.026252299547195435, 0.22422292828559875], [0.5472683906555176, 0.013142406940460205, 0.6139676570892334, 0.5378737449645996, 0.026105768978595734, 0.22074194252490997], [0.5502822399139404, 0.013228148221969604, 0.6152147650718689, 0.5340834856033325, 0.025985412299633026, 0.21728584170341492], [0.5529192686080933, 0.013307034969329834, 0.6164247989654541, 0.530447244644165, 0.02589089423418045, 0.21386244893074036], [0.5552121996879578, 0.013381734490394592, 0.6175984144210815, 0.5269503593444824, 0.025822021067142487, 0.21047933399677277], [0.5571922063827515, 0.01345449686050415, 0.6187360286712646, 0.5235800743103027, 0.025778330862522125, 0.20714309811592102], [0.5588881969451904, 0.013527542352676392, 0.6198378801345825, 0.5203243494033813, 0.025759201496839523, 0.20385995507240295], [0.5603272914886475, 0.01360301673412323, 0.6209039688110352, 0.5171728134155273, 0.025764193385839462, 0.20063547790050507], [0.5615345239639282, 0.013682499527931213, 0.6219340562820435, 0.514116108417511, 0.025792542845010757, 0.19747518002986908], [0.5625336170196533, 0.013767629861831665, 0.6229279041290283, 0.5111461877822876, 0.025843586772680283, 0.1943833976984024], [0.5633459091186523, 0.013859853148460388, 0.6238850951194763, 0.5082560777664185, 0.025916706770658493, 0.191364586353302], [0.563991367816925, 0.013960413634777069, 0.6248053312301636, 0.505439281463623, 0.026011046022176743, 0.1884225308895111]]

gen_li_xy = []
#print("length gen_li" + str(len(gen_li)))
#Add seed data here
seed = [[  3.33000000e+02,   6.72180951e-01,   4.39366579e-01,
          0.00000000e+00,   0.00000000e+00,   4.99361992e-01,
          1.23300000e+03,   5.16163290e-01,   6.26829803e-01,
          1.00000000e+00,   8.66106898e-03,   2.49065191e-01],
       [  3.33000000e+02,   6.72180951e-01,   4.39366579e-01,
          0.00000000e+00,   0.00000000e+00,   4.99361992e-01,
          1.23300000e+03,   5.16163290e-01,   6.26663923e-01,
          1.00000000e+00,   1.21259056e-02,   2.49065191e-01],
       [  3.33000000e+02,   6.72180951e-01,   4.39366579e-01,
          0.00000000e+00,   0.00000000e+00,   4.99361992e-01,
          1.23300000e+03,   5.16163290e-01,   6.26457036e-01,
          1.00000000e+00,   1.55850276e-02,   2.49065191e-01]]

for i in range(len(gen_li_xy)):
	temp = []
	for j in range(len(gen_li_xy[i])):
		if (j == 0):
			val = denormalizer(float(gen_li_xy[i][j]), -56.5545701913, -15.904584042)
			#print("car 1 x " + str(val) + ' ' + str(gen_li[i][j]))
			temp.append(val)
		if (j == 1):
			val = denormalizer(float(gen_li_xy[i][j]), -38.8697274136, 5.78484721801)
			temp.append(val)
			#print("car 1 y " + str(val) + ' ' + str(gen_li[i][j]))
		if (j == 2):
			val = denormalizer(float(gen_li_xy[i][j]), 1, 3)
			temp.append(val)
		if (j == 3):
			val = denormalizer(float(gen_li_xy[i][j]), 0.0, 12.8737431131)
			temp.append(val)
		if (j == 4):
			val = denormalizer(float(gen_li_xy[i][j]), -3.13358524866, 3.14159265359)
			temp.append(val)
		if (j == 5):
			val = denormalizer(float(gen_li_xy[i][j]), -95.3585481006, 24.968774703)
			temp.append(val)
		if (j == 6):
			val = denormalizer(float(gen_li_xy[i][j]), -78.4804293362, 28.7612966226)
			temp.append(val)
		if (j == 7):
			val = denormalizer(float(gen_li_xy[i][j]), 1, 3)
			temp.append(val)
		if (j == 8):
			val = denormalizer(float(gen_li_xy[i][j]), 0.0, 19.2470832483)
			temp.append(val)
		if (j == 9):
			val = denormalizer(float(gen_li_xy[i][j]), -3.13377098469, 3.14159265359)
			temp.append(val)
	denorm_gen_xylsd.append(temp)


for i in range(len(gen_li)):
	temp = []
	for j in range(len(gen_li[i])):
		if (j == 0):
			val = denormalizer(float(gen_li[i][j]), 1, 3)
			temp.append(val)
		if (j == 1):
			val = denormalizer(float(gen_li[i][j]), 0.0, 12.8737431131)
			temp.append(val)
		if (j == 2):
			val = denormalizer(float(gen_li[i][j]), -3.13358524866, 3.14159265359)
			temp.append(val)
		if (j == 3):
			val = denormalizer(float(gen_li[i][j]), 1, 3)
			temp.append(val)
		if (j == 4):
			val = denormalizer(float(gen_li[i][j]), 0.0, 19.2470832483)
			temp.append(val)
		if (j == 5):
			val = denormalizer(float(gen_li[i][j]), -3.13377098469, 3.14159265359)
			temp.append(val)

	denorm_gen_lsd.append(temp)

time_constant = 0.028609
#time_constant = 1
def nextPoint_car1(x, y, a, i):
	if (len(a) == 0):
		print('done calc car 1 xy')
	else:
		x2 = x+((a[i][1]*time_constant)*np.cos(a[i][2]))
		y2 = y+((a[i][1]*time_constant)*np.sin(a[i][2]))
		gen_x_array.append(x2)
		gen_x_ten.append(x2)
		gen_y_array.append(y2)
		gen_y_ten.append(y2)
		gen_x_ten.append
		gen_light_array.append(a[i][0])
		gen_dist_array.append(a[i][1]*time_constant)
		gen_angle_array.append(a[i][2])
		gen_speed1.append(a[i][1])
		i += 1
		nextPoint_car1(x2,y2, a[i:], 0)

def nextPoint_car2(x, y, a, i):
	if (len(a) == 0):
		print('done calc car 2 xy')
	else:
		x2 = x+((a[i][4]*time_constant)*np.cos(a[i][5]))
		y2 = y+((a[i][4]*time_constant)*np.sin(a[i][5]))
		gen_x_array2.append(x2)
		gen_x_ten2.append(x2)
		gen_y_array2.append(y2)
		gen_y_ten2.append(y2)
		gen_light_array2.append(a[i][3])
		gen_dist_array2.append(a[i][4]*time_constant)
		gen_angle_array2.append(a[i][5])
		gen_speed2.append(a[i][4])
		i += 1
		nextPoint_car2(x2,y2, a[i:], 0)

#6.53383851e-01   5.43324590e-01 
#5.58101833e-01   5.52258968e-01 
x_norm1 = denormalizer(seed[0][1], -56.5545701913, -15.904584042)
#print(seed[0][1])
#print(seed[0][2])
y_norm1 = denormalizer(seed[0][2], -38.8697274136, 5.78484721801)
x2_norm1 = denormalizer(seed[0][7], -95.3585481006, 24.968774703)
y2_norm1 = denormalizer(seed[0][8] , -78.4804293362, 28.7612966226)

x_norm2 = denormalizer(seed[1][1] , -56.5545701913, -15.904584042)
y_norm2 = denormalizer(seed[1][2], -38.8697274136, 5.78484721801)
x2_norm2 = denormalizer(seed[1][7], -95.3585481006, 24.968774703)
y2_norm2 = denormalizer(seed[1][8], -78.4804293362, 28.7612966226)

x_norm3 = denormalizer(seed[2][1], -56.5545701913, -15.904584042)
y_norm3 = denormalizer(seed[2][2], -38.8697274136, 5.78484721801)
x2_norm3 = denormalizer(seed[2][7], -95.3585481006, 24.968774703)
y2_norm3 = denormalizer(seed[2][8], -78.4804293362, 28.7612966226)

#print('seed: ')
#print('Car 1 pos 1: ' + str(x_norm1) + ' ' + str(y_norm1))
#print('Car 1 pos 2: ' + str(x_norm2) + ' ' + str(y_norm2))
#print('Car 1 pos 3: ' + str(x_norm3) + ' ' + str(y_norm3))

#print('Car 2 pos 1: ' + str(x2_norm1) + ' ' + str(y2_norm1))
#print('Car 2 pos 2: ' + str(x2_norm2) + ' ' + str(y2_norm2))
#print('Car 2 pos 3: ' + str(x2_norm3) + ' ' + str(y2_norm3))

gen_x_array.append(x_norm1)
gen_y_array.append(y_norm1)

gen_x_array2.append(x2_norm1)
gen_y_array2.append(y2_norm1)

gen_x_array.append(x_norm2)
gen_y_array.append(y_norm2)

gen_x_array2.append(x2_norm2)
gen_y_array2.append(y2_norm2)


#car1 : -29.994525695887116 -14.607798972343684
#car2 : -28.203648699971538 -19.255224393768863

#Car1 : -28.128791098845713 -17.513186992141364
	#	-33.25				-26.23277145829449


#Car2 : -28.203648699971538 -19.255224393768863
		#-31.008792218894047 -23.578177608507804

# Car 1 final : -33.328242112821684		-26.565997718478961
# Car 1 real  : -33.25 					-26.23277145829449
# Car 2 final : -25.028389364590794 	-22.75
# Car 2 real  : -25.028389364590794 	-23.578177608507804

# Car 1 first real : -33.25				-26.23277145829449
# Car 1 first gen  : -33.257220487765089 -26.244767584963974

# Car 2 first real : -25.048650499504262	-22.75
# Car 2 first gen  : -25.028389364590794 	-22.75


nextPoint_car1(x_norm3, y_norm3, denorm_gen_lsd, 0)
nextPoint_car2(x2_norm3, y2_norm3, denorm_gen_lsd, 0)
#print('X pos ' + str(gen_x_array))
#print('Y pos' + str(gen_y_array))

#print('Making test graph')

#Vertices of intersection: BL = -42, -28 BR = -28, -28 TR -28, -14 TL = -42, -14

intersection_x = [-42, -28, -28, -42]
intersection_y = [-28, -28, -14, -14]

#ax9.plot(gen_x_array, gen_y_array, c='k')

ax9.add_patch(
    patches.Rectangle(
        (-42, -28),
        14,
        14,
        fill=False,
        linestyle ='dashed',
        edgecolor="red"      # remove background
    )
)

car1gen = ax9.scatter(gen_x_array, gen_y_array, c='g', alpha = 0.2)
car2gen = ax9.scatter(gen_x_array2, gen_y_array2, c='r', alpha = 0.2)
car1gt = ax9.scatter(ground_truth_x1, ground_truth_y1, c='b', alpha = 0.2)
car2gt = ax9.scatter(ground_truth_x2, ground_truth_y2, c='y', alpha = 0.2)

mp = midpoint(ground_truth_x1[-1], ground_truth_y1[-1], ground_truth_x2[-1], ground_truth_y2[-1])
print('midpoint' + str(mp))
collision = ax9.scatter(mp[0], mp[1], c='k', marker=(5,2))

ax9.annotate('', xy=(gen_x_array2[0], gen_y_array2[0]), xycoords='data',
                  xytext=(gen_x_array2[-1], gen_y_array2[-1]), textcoords='data',
                  arrowprops=dict(arrowstyle="<->",
                                  connectionstyle="bar,fraction=-0.3",
                                  ec="r",
                                  shrinkA=1, shrinkB=1))

ax9.annotate('', xy=(gen_x_array[0], gen_y_array[0]), xycoords='data',
                  xytext=(gen_x_array[-1], gen_y_array[-1]), textcoords='data',
                  arrowprops=dict(arrowstyle="<->",
                                  connectionstyle="bar,fraction=0.3",
                                  ec="g",
                                  shrinkA=1, shrinkB=1))

ax9.annotate('', xy=(ground_truth_x1[0], ground_truth_y1[0]), xycoords='data',
                  xytext=(ground_truth_x1[-1], ground_truth_y1[-1]), textcoords='data',
                  arrowprops=dict(arrowstyle="<->",
                                  connectionstyle="bar,fraction=-0.3",
                                  ec="b",
                                  shrinkA=1, shrinkB=1))

ax9.annotate('', xy=(ground_truth_x2[0], ground_truth_y2[0]), xycoords='data',
                  xytext=(ground_truth_x2[-1], ground_truth_y2[-1]), textcoords='data',
                  arrowprops=dict(arrowstyle="<->",
                                  connectionstyle="bar,fraction=0.3",
                                  ec="y",
                                  shrinkA=1, shrinkB=1))

box = ax9.get_position()
ax9.set_position([box.x0, box.y0, box.width * 0.8, box.height])

ax9.legend((car1gen, car2gen, car1gt, car2gt, collision), ('Car 1 generated', 'Car 2 generated', 'Car 1 ground truth', 'Car 2 gound truth', 'Collision Ground Truth'), 
	scatterpoints = 1, loc='center left', bbox_to_anchor=(1, 0.5), ncol=1, fontsize=10)

#ax9.annotate('Start gen Car 1', xy=(gen_x_array[0], gen_y_array[0]), xytext=(gen_x_array[0]+2, gen_y_array[0]+2),
        #   arrowprops=dict(arrowstyle="->"),
        #    )

#ax9.annotate('End gen Car 1', xy=(gen_x_array[-1], gen_y_array[-1]), xytext=(gen_x_array[-1]+2, gen_y_array[-1]+2),
          # arrowprops=dict(arrowstyle="->"),
          #  )

ax9.annotate('Intersection', xy=(-38, -27), xytext=(-38, -27))

ax9.set_xlabel('X-coordinate')
ax9.set_ylabel('Y-coordinate')
ax9.title.set_text('Generated Scenario vs. Real Scenario')


for i in range(len(gen_x_array)):
	car1gen_flat = ax8.scatter(gen_x_array[i], gen_y_array[i], zs = i, zdir = 'z', c='g', alpha = 0.2)
	car2gen_flat = ax8.scatter(gen_x_array2[i], gen_y_array2[i], zs = i, zdir = 'z', c='r', alpha = 0.2)

for i in range(len(ground_truth_x1)):
	car1gd = ax8.scatter(ground_truth_x1[i], ground_truth_y1[i], zs = i, zdir = 'z', c='b', alpha = 0.2)
	car2gd = ax8.scatter(ground_truth_x2[i], ground_truth_y2[i], zs = i, zdir = 'z', c='y', alpha = 0.2)

for i in range(len(gen_x_ten)):
	car1gdten = ax8.scatter(gen_x_ten[i], gen_y_ten[i], zs = i, zdir = 'z', c='k', alpha = 0.2)
	car2gdten = ax8.scatter(gen_x_ten2[i], gen_y_ten2[i], zs = i, zdir = 'z', c='m', alpha = 0.2)

ax8.set_xlabel('X-coordinate')
ax8.set_ylabel('Y-coordinate')
ax8.title.set_text('Generated data')
ax8.legend((car1gen_flat, car2gen_flat, car1gd, car2gd, car1gdten, car2gdten), ('Car 1 gen', 'Car 2 gen', 'Car 1 ground truth', 'Car 2 gound truth', 
	'Car 1 Coord', 'Car 2 Coord'), scatterpoints = 1, loc='upper right', ncol=6, fontsize=10)

#print('finished plotting')
def printstats():
	print("gen x 1 " + str(gen_x_array))
	print("gen y 1 " + str(gen_y_array))
	print("gen s 1 " + str(gen_speed1))
	print("gen l 1 " + str(gen_dir1))
	print("gen x 2 " + str(gen_x_array2))
	print("gen y 2 " + str(gen_y_array2))
	print("gen s 2 " + str(gen_speed2))
	print("gen l 2 " + str(gen_dir2))
	print("ground x 1 " + str(ground_truth_x1))
	print("ground y 1 " + str(ground_truth_y1))
	print("ground s 1 " + str(ground_truth_l))
	print("ground d 1 " + str(ground_truth_d))
	print("ground x 2 " + str(ground_truth_x2))
	print("ground y 2 " + str(ground_truth_y2))
	print("ground s 2 " + str(ground_truth_2l))
	print("ground d 2 " + str(ground_truth_2d))

plt.gca().invert_yaxis()
plt.show()
