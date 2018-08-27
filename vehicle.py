
class properties():
	"""docstring for properties"""
	def __init__(self):
		self.No_of_wheels = 4


class Vehicle(properties):
	"""docstring for Vehicle"""
	fuel_price = 70
	Total_cost = 0
	# Mileage = None
	# Travelled = None
	def __init__(self, name,mil,distance):
		properties.__init__(self)
		self.v_name = name
		self.Mileage = mil
		self.Travelled = distance


	def Calculation(self):
		# global Total_cost
		cost =  (self.Travelled/self.Mileage)*self.fuel_price
		Vehicle.Total_cost+=cost
		return cost

	def __str__(self):
		return 'Name = '+self.v_name +'\nMileage = '+ str(self.Mileage) +'\nTravelled = '+ str(self.Travelled) +'\n'+str(self.No_of_wheels)

def main():
	
	car = Vehicle("Car",20,100)
	jeep = Vehicle("Jeep",15,120)
	bus = Vehicle("Bus",10,150)
	veh = []
	veh.append(car)
	veh.append(jeep)
	veh.append(bus)
	for obj in veh:
		print(obj)
		print('Cost = ',obj.Calculation())
	print("Total cost = ",Vehicle.Total_cost)

	


if __name__ == '__main__':
	main()