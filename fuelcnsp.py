print("Fuel consumption")
ini_s = float(input("Enter the initial odometer reading in km: "))
fn_s = float(input("Enter the final odometer readin in km: "))
fuel_used = float(input("Enter the amount of fuel used in litres: "))

ds = fn_s - ini_s
fl_cnsp = ds/fuel_used

print(f"The fuel consumption of the car is {fl_cnsp} km/litre. ")