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
Time_Broadcast_new=0
def Broadcaster_new(Starter_id,S,L,p):
	for i in Device_list_dict_new:
		Device_list_dict_new[i].recChunk=False
	global Global_num_new
	global Time_Broadcast_new
	Global_num_new=0
	Time_Broadcast_new=0
	queue_new=deque([])
	queue_new.append(Starter_id)
	Device_list_dict_new[Starter_id].recChunk=True
	Global_num_new+=1
		# print(len(queue))
		# print(int(0.9*len(Device_list_dict)))
		# print(Global_num<int(0.9*len(Device_list_dict)) )
		# print(len(queue)>0)
		# print(Global_num<int(0.9*len(Device_list_dict)) & len(queue)>0)
	while ((len(queue_new)>0)):
		# print("haha")
		first_new=queue_new.popleft()
		# print(first_)
		# print("haha")
		it=0
		# print(Device_list_dict[first_].node_set)
		for i in Device_list_dict_new[first_new].node_set:
			if((Device_list_dict_new[i].recChunk==False) & (queue_new.count(i)==0)):
				print(Device_list_dict_new[i].indexnum)
				if((Device_list_dict_new[i].indexnum + 1) >= ((1-(L/100)) * len(Device_list_dict_new))):
					Device_list_dict_new[i].recChunk=True
					print(i)
					Global_num_new+=1
					queue_new.append(i)
					if(Device_list_dict_new[i].discover_time>=Time_Broadcast_new):
						Time_Broadcast_new=Device_list_dict_new[i].discover_time
				elif((Device_list_dict_new[i].indexnum + 1) <= (((S/100)) * len(Device_list_dict_new))):
					awe=random.random()
					if(awe>(1-p)):
						print(str(awe)+"ihbfj")
						Device_list_dict_new[i].recChunk=True
						print(i)
						Global_num_new+=1
						queue_new.append(i)
						if(Device_list_dict_new[i].discover_time>=Time_Broadcast_new):
							Time_Broadcast_new=Device_list_dict_new[i].discover_time

				else :
					awe=random.random()
					if(awe>(p)):
						print(str(awe)+"jfj")
						print(i)
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

# The part a and b of the question
# i=1
# while (Global_num<int(0.9*len(Device_list_dict))):
# 	Broadcaster(26,i)
# 	print(str(i)+" "+str(Global_num)+" "+str(Time_Broadcast))
# 	i+=1


Device_list_list=list(Device_list_dict.items())
Device_list_list=sorted(Device_list_list,key=lambda b: len(b[1].node_set),reverse=True)
Device_list_x=[]
Device_list_y=[]
k=0
for i in range(0,len(Device_list_list)-1):
	Device_list_list[i][1].indexnum=i
Device_list_dict_new=dict(Device_list_list)
Broadcaster_new(26,100,0,1)
print("badum_"+str(Global_num_new))