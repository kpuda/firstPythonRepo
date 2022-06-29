def say_hi():
    print("Hello user!")

say_hi()

def cube(num):
    return num * num * num

print(cube(3))

#If statements
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are tall male.")
else:
    print("You neither male or tall")

#dictionary
month_Conversion = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March"
}
print(month_Conversion)
print(month_Conversion["Feb"])
print(month_Conversion.get("Mar"))
print(month_Conversion.get("Dec","Not valid"))


