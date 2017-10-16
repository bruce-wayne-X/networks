import csv
from collections import deque
from collections import OrderedDict
import matplotlib.pyplot as plt
import math
import random
import numpy
class Device:
	def __init__(self,id,discoverer_id):
		self.id=id
		self.discover_time=0
		self.discoverer_id=discoverer_id
		self.node_set=[]
		self.recChunk=False
	def __init__(self,id,discoverer_id,discover_time):
		self.id=id
		self.discover_time=discover_time
		self.discoverer_id=discoverer_id
		self.node_set=[]
		self.recChunk=False
	def __eq__(self,other):
		return self.id==other.id

# BFS as required in the question
Global_num=0
Time_Broadcast=0
def Broadcaster(Starter_id,K):
	for i in Device_list_dict:
		Device_list_dict[i].recChunk=False
	global Global_num
	global Time_Broadcast
	Global_num=0
	Time_Broadcast=0
	queue=deque([])
	queue.append(Starter_id)
	Device_list_dict[Starter_id].recChunk=True
	Global_num+=1
		# print(len(queue))
		# print(int(0.9*len(Device_list_dict)))
		# print(Global_num<int(0.9*len(Device_list_dict)) )
		# print(len(queue)>0)
		# print(Global_num<int(0.9*len(Device_list_dict)) & len(queue)>0)
	while ((len(queue)>0)):
		# print("haha")
		first_=queue.popleft()
		# print(first_)
		# print("haha")
		it=0
		# print(Device_list_dict[first_].node_set)
		for i in Device_list_dict[first_].node_set:
			if((Device_list_dict[i].recChunk==False) & (it<K) & (queue.count(i)==0)):
				Device_list_dict[i].recChunk=True
				Global_num+=1
				it+=1
				queue.append(i)
				if(Device_list_dict[i].discover_time>=Time_Broadcast):
					Time_Broadcast=Device_list_dict[i].discover_time
				# print("haha"+str(i))				
	# print(Global_num)
	

Device_list_dict=dict()
with open('proximityedgestimestamps.csv') as csvfile:
	readCSV = csv.reader(csvfile,delimiter=";")
	for row in readCSV:
		if(row[0]!="number of nodes with degree more than 3 = 1723"):

			if (int(row[1]) not in Device_list_dict):
				New_device=Device(int(row[1]),int (row[2]),int(row[0]))
				Device_list_dict[int(row[1])]=New_device
				Device_list_dict[int(row[1])].node_set.append(int(row[2]))
			else:
				if int(row[2]) not in Device_list_dict[int(row[1])].node_set:
					Device_list_dict[int(row[1])].node_set.append(int(row[2]))

			if (int(row[2]) not in Device_list_dict):
				New_device=Device(int(row[2]),int(row[1]),int(row[0]))
				Device_list_dict[int(row[2])]=New_device
				Device_list_dict[int(row[2])].node_set.append(int(row[1]))
			else:
				if int(row[1]) not in Device_list_dict[int(row[2])].node_set:
					Device_list_dict[int(row[1])].node_set.append(int(row[1]))

# The part a and b of the question
# i=1
# while (Global_num<int(0.9*len(Device_list_dict))):
# 	Broadcaster(26,i)
# 	print(str(i)+" "+str(Global_num)+" "+str(Time_Broadcast))
# 	i+=1

Device_list1=list(Device_list_dict.values())
Random_Device_list=[8636, 7588, 8205, 7242, 9333, 1059, 229, 550, 4681, 1995, 434, 10353, 1508, 166, 685, 784, 1110, 4956, 1377, 6349, 4778, 8419, 7405, 2455, 570, 860, 6547, 5833, 11048, 578, 53, 1807, 9342, 6588, 4049, 6560, 1101, 9999, 1473, 901, 6817, 11009, 6732, 9337, 129, 4355, 1, 2237, 34, 11571, 1875, 4829, 5810, 1591, 4788, 1070, 7794, 7693, 19, 780, 1215, 6048, 483, 71, 4081, 1977, 5336, 1884, 4845, 991, 9277, 5308, 690, 10331, 6312, 6537, 187, 544, 6664, 5146, 11556, 1134, 2167, 11070, 1019, 116, 6527, 2600, 7222, 4630, 1596, 10013, 7595, 58, 663, 11867, 3453, 10984, 1064, 10271, 1069, 4738, 4191, 11065, 9822]


X_axis=[]
Y_axis=[]
Y_axis1=[]
Z_axis=[]
Z_axis1=[]

j=32
while (j<42):
	Node_num_array=[]
	Time_Broad_array=[]
	for i in range(0,99):
		Broadcaster(Random_Device_list[i],j)
		Node_num_array.append(Global_num)
		Time_Broad_array.append(Time_Broadcast)
	print(str(j)+" "+str(numpy.mean(Time_Broad_array))+" "+str(numpy.std(Time_Broad_array)))
	X_axis.append(j)
	Y_axis.append(numpy.mean(Time_Broad_array))
	Y_axis1.append(numpy.std(Time_Broad_array))
	Z_axis.append(numpy.mean(Node_num_array))
	Z_axis1.append(numpy.std(Node_num_array))
	j+=1
print("Y axis mean time")
print(Y_axis)
print("Y axis Std Dev time")
print(Y_axis1)
print("Z axis mean node")
print(Z_axis)
print("Z axis Std Dev node")
print(Z_axis1)
plt.errorbar(X_axis, Y_axis, Y_axis1,  marker='^')
plt.show()
# 	# Broadcaster(26,2)
# i=77
# while (i<5000):
# 	try:
# 		if((Device_list_dict[i].node_set)!=[]):
# 			print(Device_list_dict[i].node_set)
# 			print(i)
# 	except:
# 		pass
	
# 	i+=1

# Device_list_list=list(Device_list_dict.values())
# Device_list_list=sorted(Device_list_list,key=lambda Device: len(Device.node_set),reverse=True)
# Device_list_x=[]
# Device_list_y=[]
# k=0
# for i in range(0,len(Device_list_list)-1):
# 	k+=len(Device_list_list[i].node_set)
# 	Device_list_x.append(math.log(i+1))
# 	Device_list_y.append(k)
# plt.plot(Device_list_x,Device_list_y)
# # plt.xscale('log')
# # plt.yscale('log')
# # plt.annotate()
# plt.show()