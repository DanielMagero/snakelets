print("Input should be win, lose or draw")
mancity_result = input("Predict the Man City result: \n -")
ars_result = input("Predict the Ars result: \n -")

if mancity_result == "win":
    print("Man City will be Champions")
elif mancity_result == "draw":
    if ars_result == "win":
        print("Arsenal will be Champions")
    else: print("Man City will be Champions")
elif mancity_result == "lose":
    if ars_result == "win":
        print("Arsenal will be Champions")
    else: print ("Man City will be Champions")