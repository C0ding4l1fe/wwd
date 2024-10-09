print("This is a velocity calculcator, please input the necessary data, and we'll calculate it for you.")
mass=float(input("What is the mass of the object? (In kg):"))
gravity=float(input("What is the force of gravity, in m/s^2? (9.8 for Earth, 24 for Jupiter):"))
time=float(input("What is the time in seconds:"))
density=float(input("What is the density of the fluid that the object's falling through?:"))
cross_sectional_area=float(input("What is the cross sectional area in m^2:"))
drag_constant=float(input("What is the drag constant? (0.5 for a sphere, 1.1 for a cylinder):"))
c_value=(0.5)*density*cross_sectional_area*drag_constant
print (f"The inner value of c is {(0.5)*density*cross_sectional_area*drag_constant}""!")
import math
print (f"The velocity is {(math.sqrt((mass*gravity)/c_value)*((1-math.exp(-((math.sqrt(mass*gravity*c_value)/mass)*time))))):.3f}!")