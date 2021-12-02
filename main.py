import pandas as pd 

def d1p1(): #day 1 part 1
	file = pd.read_csv("./data/d1p1.csv")
	num_list = list(file['dataPoints'].tolist())
	current = 0
	big = 0
	for i in range(len(num_list)):
		if i != 0:
			if num_list[i] > current:
				big += 1
		current = num_list[i]
	return big

def d1p2(): #day 1 part 2
	file = pd.read_csv("./data/d1p1.csv")
	num_list = list(file['dataPoints'].tolist())
	current = 0
	big = 0
	for i in range(len(num_list)):
		if i != 0:
			try:
				if (num_list[i] + num_list[i+1] + num_list[i+2]) > current:
					big += 1
			except:
				break
		current = num_list[i] + num_list[i+1] + num_list[i+2]
	return big

def d2p1(): #day 2 part 1
	file = pd.read_csv("./data/d2p1.csv")
	num_list = list(file['dataPoints'].tolist())
	x = 0
	y = 0 
	for i in num_list:
		print(i)
		if i[:8] == "forward ":
			x += int(i[8:])
		elif i[:3] == "up ":
			y -= int(i[3:])
		elif i[:5] == "down ":
			y += int(i[5:])
	return x*y

def d2p2(): #day 2 part 2
	file = pd.read_csv("./data/d2p1.csv")
	num_list = list(file['dataPoints'].tolist())
	y = 0
	x = 0 
	aim = 0
	for i in num_list:
		print(i)
		if i[:8] == "forward ":
			x += int(i[8:])
			y = y + aim * int(i[8:])
		elif i[:3] == "up ":
			aim -= int(i[3:])
		elif i[:5] == "down ":
			aim += int(i[5:])
	return y*x

if __name__ == "__main__":
	print(d2p2())