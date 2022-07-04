weight = input("Weight:")
scale = input("(K)g or (L)bs:")
weight_float=float(weight)
lbs=2.24
kg=0.45
if scale=='k':
    float_lbs = weight_float * lbs
    print("Weight in lbs: "+str(float_lbs))
else:
    float_kg = weight_float * kg
    print("Weight in kg: " + str(float_kg))
