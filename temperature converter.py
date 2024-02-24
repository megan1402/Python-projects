
#convert farenheight to celcius 
def f_to_c (farenheight):
    celsisus = (farenheight -  32) * 5/9
    return celsisus

#get input from user and prin out conversion
f_user = 350
c_user = f_to_c(f_user)
print(f"{f_user} farenheight is {c_user} in celsisus")

# convert celcisus to farenheight
def c_to_f (c_temp):
    f_temp = (c_temp * 9/5) + 32
    return f_temp

#get input from user and print out the conversion
user_c = 0
user_f = c_to_f(user_c)
print(f"{user_c} celsius is {user_f} in farenheight")
