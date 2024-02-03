
age = input("WHAAAT ARE YOYR AGEEEE?!")
if age is str:
    print("Please, write your age use numbers")
else:
    age = int(age)
if age < 18 and age>1:
    print("FUCK YOU")
elif age >= 18:
    print("HELLO MY FRIEND!")
else:
    print("AAAa? Speak clearer BOY!!!")









#age_guest = {
#    "yes" : "Okey, wath are you order?",
#    "no" : "WATH?!"
#}

#age = input("Hello kid, you sure what your age +18? ")
#age_otvet = age_guest.get(age)
#if age_otvet is None:
#    print("Sorry, your answer incorrect")
#else:
#    print(age_otvet)