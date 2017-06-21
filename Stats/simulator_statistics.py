import numpy as np
import csv
import os
import glob
import re
import pickle

#rectangle of intersection dimension in simulator x = -42 y = -28 width 14 height 14

collisionPoints = []
car1speed = []
car2speed = []
total_speeds = []
scene = []
scenarios = []
car1_arr = []
x1_arr = []
y1_arr = []
lights1_arr = []
speed1_arr = []
car2_arr =[]
x2_arr = []
y2_arr = []
lights2_arr = []
speed2_arr = []
speedTemp = []
speed_calc = []
speed_calc_temp = []
distances = []
actual_speed1 = []
actual_speed2 = []
actual_speed_total =[]
dir1_arr = []
dir2_arr = []

stationaryScene = []
stationaryScenario = []
stationaryScenario1_CSV = []
stationaryScenario2_CSV = []
movingScenario = []
movingScenario_CSV = []
position_CSV = []
sample_position_CSV = []

sample = 1
datapoints = 0;
z1 = np.linspace(0, 49, 49)
start = 0
end = 49
start2 = 0
timesteps = 10
finalDist1 = 0
finalDist2 = 0
length_speed = len(x1_arr) - 1

max_x = 0
min_x = 0
max_y = 0
min_y = 0
max_l = 0
min_l = 0
max_s = 0
min_s = 0
max_d = 0
min_d = 0

max_x2 = 0
min_x2 = 0
max_y2 = 0
min_y2 = 0
max_l = 0
min_l = 0
max_s2 = 0
min_s2 = 0
max_d2 = 0
min_d2 = 0

big_arr = []

norm_arr = []
norm_CSV = []
max_val = 0
min_val = 0

groundtruth = []

#find the distance between two coordinates
def distance(x1, x2, y1, y2):
	return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#find the midpoint between two coordinates
def midpoint(x1, y1, x2, y2):
    return ((x1 + x2)/2, (y1 + y2)/2)

#normalizing data between 0 and 1
def normalizer(val, mi, ma):
	a = val - mi
	b = ma - mi
	norm = a/b
	return norm

def denormalizer(val, mi, ma):
	a = ma - mi
	b = val * a
	denorm = b + mi
	return denorm


#reads simulator data from csv file and puts into arrays
print('Loading csv files...')
for filename in glob.glob('*.csv'):

	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			id1 = row[0]
			x1 = row[1]
			y1 = row[2]
			l1 = row[3]
			s1 = row[4]
			d1 = row[5]
			id2 = row[6]
			x2 = row[7]
			y2 = row[8]
			l2 = row[9]
			s2 = row[10]
			d2 = row[11]

			id1_arr = re.findall(r'\d+', id1)
			c_1 = id1_arr[0]
			c1 = int(c_1)
			car1_arr.append(c1)
			x1_arr.append(float(x1))
			y1_arr.append(float(y1))
			lights1_arr.append(int(l1))
			speed1_arr.append(float(s1))
			dir1_arr.append(float(d1))
			id2_arr = re.findall(r'\d+', id2) 
			c_2 = id2_arr[0]
			c2 = int(c_2)
			car2_arr.append(c2)
			x2_arr.append(float(x2))
			y2_arr.append(float(y2))
			lights2_arr.append(int(l2))
			speed2_arr.append(float(s2))
			dir2_arr.append(float(d2))
			#Change c1 value with car 1 ID and c2 value with car 2 ID
			if(c1 == 333  and c2 == 1233):
				groundtruthscene = []
				groundtruthscene.append(c1)
				groundtruthscene.append(float(x1))
				groundtruthscene.append(float(y1))
				groundtruthscene.append(float(l1))
				groundtruthscene.append(float(s1))
				groundtruthscene.append(float(d1))
				groundtruthscene.append(c2)
				groundtruthscene.append(float(x2))
				groundtruthscene.append(float(y2))
				groundtruthscene.append(float(l2))
				groundtruthscene.append(float(s2))
				groundtruthscene.append(float(d2))
				groundtruth.append(groundtruthscene)
				groundtruthscene = []


			stationaryScene.append(c1)
			stationaryScene.append(float(x1))
			stationaryScene.append(float(y1))
			stationaryScene.append(float(l1))
			stationaryScene.append(float(s1))
			stationaryScene.append(float(d1))
			stationaryScene.append(c2)
			stationaryScene.append(float(x2))
			stationaryScene.append(float(y2))
			stationaryScene.append(float(l2))
			stationaryScene.append(float(s2))
			stationaryScene.append(float(d2))
			stationaryScenario.append(stationaryScene)
			stationaryScene = []
			
			c1speed = float(s1)
			c2speed = float(s2)

			temp_position_1 = []
			temp_position_2 = []

			temp_position_1.append(float(x1))
			temp_position_1.append(float(y2))
			temp_position_2.append(float(x2))
			temp_position_2.append(float(y2))

			position_CSV.append(temp_position_1)
			position_CSV.append(temp_position_2)


			#Both cars moving with speed range 0.2 3.5
			if(datapoints != 0 and datapoints%50 == 0 and ((c1speed and c2speed > 0.2) and (c1speed and c2speed < 3.5))):
				starting = datapoints-50
				for i in range(50):
					scene = stationaryScenario[starting+i]
					movingScenario_CSV.append(scene)
					scene = []
			#Car1 stationary
			if(datapoints != 0 and datapoints%50 == 0 and c1speed == 0):
				starting = datapoints-50
				for i in range(50):
					scene = stationaryScenario[starting+i]
					stationaryScenario1_CSV.append(scene)

					scene = []
			#Car2 stationary
			if(datapoints != 0 and datapoints%50 == 0 and c2speed == 0):
				starting = datapoints-50
				for i in range(50):
					scene = stationaryScenario[starting+i]
					stationaryScenario2_CSV.append(scene)
					scene = []
				

			datapoints += 1
#print(groundtruth)
#pickle.dump(groundtruth, open("ground_truth.pkl", "wb"))

print('Finished loading csv files')
big_arr.append(car1_arr)
big_arr.append(x1_arr)
big_arr.append(y1_arr)
big_arr.append(lights1_arr)
big_arr.append(speed1_arr)
big_arr.append(dir1_arr)
big_arr.append(car2_arr)
big_arr.append(x2_arr)
big_arr.append(y2_arr)
big_arr.append(lights2_arr)
big_arr.append(speed2_arr)
big_arr.append(dir2_arr)
#normalizing data
#print('normalizing data')
#print('length of big arr ' + str(len(big_arr[0])))

for i in range(len(big_arr)):
	max_val = np.amax(big_arr[i])
	#print('Position ' + str(i) + ' Max ' + str(max_val))
	min_val = np.amin(big_arr[i])
	#print('Position ' + str(i) + ' Min ' + str(min_val))
	temp_arr = []

	for j in range(len(big_arr[i])):
		val = big_arr[i][j]
		if(i == 0):
			temp_arr.append(val)
		if(i == 6):
			temp_arr.append(val)
		if(i != 0 and i != 6):
			normed = normalizer(val, min_val, max_val)
			temp_arr.append(normed)

	norm_arr.append(temp_arr)

#print(len(norm_arr[0]))
for i in range(len(norm_arr[0])):
	temp_arr = []
	for j in range(len(norm_arr)):
		temp_arr.append(norm_arr[j][i])

	norm_CSV.append(temp_arr)

#print('Done normalized')
#np.savetxt("CSVdata\Data_normed_final.csv", norm_CSV, delimiter=",")
#print('Saved normalizing')

length_full = int(len(x1_arr)/50) #Length of total timesteps
length_sample = length_full/sample #Length of sampled timesteps
length_pos_sample = int(datapoints/sample)
i_pos = 0;
for i in range(length_pos_sample):
	temp_position_1 = []
	temp_position_2 = []

	temp_position_1.append(x1_arr[i*sample])
	temp_position_1.append(y1_arr[i*sample])
	temp_position_2.append(x2_arr[i*sample])
	temp_position_2.append(y2_arr[i*sample])

	sample_position_CSV.append(temp_position_1)
	sample_position_CSV.append(temp_position_2)

#print('Sample position ' + str(len(sample_position_CSV)))
#Loop to plot sampled data and do some calculations 
for i in range(int(length_sample)):
	temp_speed = []

	actual_speed1.append(speed1_arr[end])
	actual_speed2.append(speed2_arr[end])

	temp_speed.append(speed1_arr[end])
	temp_speed.append(speed2_arr[end])
	actual_speed_total.append(temp_speed)

	#Making array of distance between center point of vehicles at collision
	distances.append(distance(x1_arr[end], x2_arr[end], y1_arr[end], y2_arr[end]))

	#Making array of collisionPoints which are the midpoint of the distance of center Car 1 vs Car 2
	collisionPoints.append(midpoint(x1_arr[end],y1_arr[end],x2_arr[end],y2_arr[end]))

	#Making x-coordinate and y-xoordinate arrays for later plotting
	xcol = [x1_arr[end], x2_arr[end]]
	ycol = [y1_arr[end], y2_arr[end]]

	#Increase indeces to use to sample from dataset
	start = start + (50*sample)
	end = end + (50*sample)

print('Saving to csv...')

#np.savetxt("CSVdata\Sample_collision_points.csv", collisionPoints, delimiter=",")
#np.savetxt("CSVdata\Sample_speed_at_collsion.csv", actual_speed_total, delimiter=",")
#np.savetxt("CSVdata\simulator_data_moving_cars.csv", movingScenario_CSV, delimiter=",")
#np.savetxt("CSVdata\simulator_data_stationary_car1.csv", stationaryScenario1_CSV, delimiter=",")
#np.savetxt("CSVdata\simulator_data_stationary_car2.csv", stationaryScenario2_CSV, delimiter=",")
#np.savetxt("CSVdata\Sample_distances.csv", distances, delimiter=",")
#np.savetxt("CSVdata\Total_data.csv", stationaryScenario, delimiter=",")
np.savetxt("CSVdata\ground_truth.csv", groundtruth, delimiter=",")
#np.savetxt("CSVdata\Total_position.csv", position_CSV, delimiter=",")
#np.savetxt("CSVdata\Sample_position.csv", sample_position_CSV, delimiter=",")

print('Collisions: ' + str(length_full))
print('Timesteps: ' + str(datapoints))
