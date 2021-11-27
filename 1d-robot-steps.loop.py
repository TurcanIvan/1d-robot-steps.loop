# ---------- R --------->
# 0 

batteryCharge = 70   #%
ratePerStep   = 10   # 10%/m

steps = 0

# COMPLEXITY
# DRY - Don't Repeat Yourself 
while batteryCharge > 0:
     ############ one step ############################
    steps         += 1           # increment
    batteryCharge -= ratePerStep # decrement
    print("steps", steps,"battery:",batteryCharge, "%")
    if batteryCharge <= 10:
        print("WAITING!!! need to charge")
     ############# one step ############################