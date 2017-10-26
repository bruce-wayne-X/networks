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
		self.indexnum=0
	def __init__(self,id,discoverer_id,discover_time):
		self.id=id
		self.discover_time=discover_time
		self.discoverer_id=discoverer_id
		self.node_set=[]
		self.recChunk=False
		self.indexnum=0
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
	
# BFS as required in the question
Global_num_new=0
S_num=0
L_num=0
Else_num=0
Time_Broadcast_new=0
def Broadcaster_new(Starter_id,S,L,p):
	
	for i in Device_list_dict_new:
		Device_list_dict_new[i].recChunk=False
	
	global Global_num_new
	global S_num
	global L_num
	global Else_num
	global Time_Broadcast_new
	Global_num_new=0
	Time_Broadcast_new=0
	S_num=0
	L_num=0
	Else_num=0

	queue_new=deque([])
	queue_new.append(Starter_id)
	Device_list_dict_new[Starter_id].recChunk=True
	Global_num_new+=1
	while ((len(queue_new)>0)):
		first_new=queue_new.popleft()
		if((Device_list_dict_new[first_new].indexnum + 1) >= ((1-(L/100)) * len(Device_list_dict_new))):
			L_num+=1
		elif((Device_list_dict_new[first_new].indexnum + 1) <= (((S/100)) * len(Device_list_dict_new))):
			S_num+=1
		else:
			Else_num+=1

		for i in Device_list_dict_new[first_new].node_set:
			if((Device_list_dict_new[i].recChunk==False) & (queue_new.count(i)==0)):
				# print(Device_list_dict_new[i].indexnum)
				if((Device_list_dict_new[i].indexnum + 1) >= ((1-(L/100)) * len(Device_list_dict_new))):
					Device_list_dict_new[i].recChunk=True
					# print(i)
					Global_num_new+=1
					queue_new.append(i)
					if(Device_list_dict_new[i].discover_time>=Time_Broadcast_new):
						Time_Broadcast_new=Device_list_dict_new[i].discover_time
				elif((Device_list_dict_new[i].indexnum + 1) <= (((S/100)) * len(Device_list_dict_new))):
					awe=random.random()
					if(awe>(1-p)):
						# print(str(awe)+"ihbfj")
						Device_list_dict_new[i].recChunk=True
						# print(i)
						Global_num_new+=1
						queue_new.append(i)
						if(Device_list_dict_new[i].discover_time>=Time_Broadcast_new):
							Time_Broadcast_new=Device_list_dict_new[i].discover_time

				else :
					awe=random.random()
					if(awe>(p)):
						# print(str(awe)+"jfj")
						# print(i)
						Device_list_dict_new[i].recChunk=True
						Global_num_new+=1
						queue_new.append(i)
						if(Device_list_dict_new[i].discover_time>=Time_Broadcast_new):
							Time_Broadcast_new=Device_list_dict_new[i].discover_time

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


Random_Device_list=[8636, 7588, 8205, 7242, 9333, 1059, 229, 550, 4681, 1995, 434, 10353, 1508, 166, 685, 784, 1110, 4956, 1377, 6349, 4778, 8419, 7405, 2455, 570, 860, 6547, 5833, 11048, 578, 53, 1807, 9342, 6588, 4049, 6560, 1101, 9999, 1473, 901, 6817, 11009, 6732, 9337, 129, 4355, 1, 2237, 34, 11571, 1875, 4829, 5810, 1591, 4788, 1070, 7794, 7693, 19, 780, 1215, 6048, 483, 71, 4081, 1977, 5336, 1884, 4845, 991, 9277, 5308, 690, 10331, 6312, 6537, 187, 544, 6664, 5146, 11556, 1134, 2167, 11070, 1019, 116, 6527, 2600, 7222, 4630, 1596, 10013, 7595, 58, 663, 11867, 3453, 10984, 1064, 10271, 1069, 4738, 4191, 11065, 9822]


Device_list_list=list(Device_list_dict.items())
Device_list_list=sorted(Device_list_list,key=lambda b: len(b[1].node_set),reverse=True)

k=0
for i in range(0,len(Device_list_list)-1):
	Device_list_list[i][1].indexnum=i
	# print(str(i)+" "+str(Device_list_list[i][0])+" "+str(len(Device_list_list[i][1].node_set)))
Device_list_dict_new=dict(Device_list_list)
Global_num_list=[]
Time_Broadcast_list=[]
S_list=[]
Else_list=[]
L_list=[]
P_list=[0,0.01,0.02,0.05,0.1,0.15,0.2,0.25,0.35,0.5,0.65,0.7,0.8,0.85,0.9,0.92,0.95,0.98,0.99,1]
S_L_list=[0,0.5,0.75,1,2,5,10,15,20,25,35,50,60,70,80,90,92,95,99,1]
for j in range(0,len(S_L_list)-1):
	for k in range(0,len(S_L_list)-1):
		if((S_L_list[j]+S_L_list[k])<=100):
			Global_num_list=[]
			Time_Broadcast_list=[]
			S_list=[]
			Else_list=[]
			L_list=[]

			for i in range(0,len(P_list)):
				Broadcaster_new(26,S_L_list[j],S_L_list[k],P_list[i])
				Global_num_list.append(Global_num_new)
				Time_Broadcast_list.append(Time_Broadcast_new)
				S_list.append(S_num)
				Else_list.append(Else_num)
				L_list.append(L_num)
			print(str(S_L_list[j])+" "+str(S_L_list[k]))
			print("P_list")
			print(P_list)
			print("Global_num_list")
			print(Global_num_list)
			print("Time_Broadcast_list")
			print(Time_Broadcast_list)
			print("S_list")
			print(S_list)
			print("Else_list")
			print(Else_list)
			print("L_list")
			print(L_list)