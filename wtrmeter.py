ini_v = float(input("Enter the inital water meter reading in kiloliters: "))
fn_v = float(input("Enter the final water meter reading in kiloliters: "))

cnsp = fn_v - ini_v
w_cost = cnsp * 1.50

print(f"The water consumption is {cnsp} kilolitres. \n The cost is Shs. {w_cost}.")