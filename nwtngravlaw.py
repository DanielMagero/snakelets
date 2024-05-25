print("Calculating the force in Newton's Law of Gravitation")
m1 = float(input("Enter the mass of M1 in kg: "))
m2 = float(input("Enter the mass of M2 in kg: "))
r_f = float(input("Enter the distance between the objects in meters: "))

F_g = ((6.7 * 10**-11) * m1 * m2)/(r_f * r_f)

print (f"The force of gravitational attraction between the two bodies = {F_g} Newtons.")