import csv
from collections import deque
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


# def Search_Recursion(id,Global_num,K):
# 	it=0
# 	queue=[]
# 	for i in Device_list_dict[id]:
# 		if(Device_list_dict[i].recChunk==False & it<K):
# 			Device_list_dict[i].recChunk=True
# 			Global_num+=1
# 			it+=1
# 			queue.append(i)
# 	for i in queue:			
# 		if(Global_num<0.9*len(Device_list_dict)):
# 			Search_Recursion(i,Global_num)

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
	while ((Global_num<int(0.9*len(Device_list_dict))) & (len(queue)>0)):
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
				New_device=Device(int(row[1]),0,0)
				Device_list_dict[int(row[1])]=New_device
				Device_list_dict[int(row[1])].node_set.append(int(row[2]))
			else:
				if int(row[2]) not in Device_list_dict[int(row[1])].node_set:
					Device_list_dict[int(row[1])].node_set.append(int(row[2]))

			if (int(row[2]) not in Device_list_dict):
				New_device=Device(int(row[2]),int(row[1]),int(row[0]))
				Device_list_dict[int(row[2])]=New_device
			# 	Device_list_dict[int(row[2])].node_set.add(int(row[1]))
			# else:
			# 	Device_list_dict[int(row[2])].node_set.add(int(row[1]))
i=76
# while (Global_num<int(0.9*len(Device_list_dict))):
# 	Broadcaster(26,i)
# 	print(str(i)+" "+str(Global_num)+" "+str(Time_Broadcast))
# 	i+=1
Broadcaster(26,2)
while (i<5000):
	try:
		if((Device_list_dict[i].node_set)!=[]):
			print(Device_list_dict[i].node_set)
			print(i)
	except:
		pass
	
	i+=1