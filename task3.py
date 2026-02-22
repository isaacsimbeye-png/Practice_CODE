from_unit = input("FROM (KM,M,CM,MILLI): ").upper()
to_unit = input("TO (KM,M,CM,MILLI): ").upper()
distance = float(input("Enter Distance: "))

if from_unit == 'M' and to_unit == 'KM' :
	result = distance/1000
	print(f"Distance = {result} KM")

elif from_unit == 'CM' and to_unit == 'KM' :
	result = distance / 100000
	print(f"Distance = {result} KM")

elif from_unit == 'MILLI' and to_unit == 'KM' :
	result = distance / 1000000
	print(f"Distance = {result} KM") 
elif from_unit == 'M' and to_unit == 'CM' :
    result = distance * 100
    print(f"Distance = {round(result,2)} CM")
elif from_unit == 'MILLI' and to_unit == 'CM' :
    result = distance / 10
    print(f"Distance = {round(result,2)} CM")
elif from_unit == 'KM' and to_unit == 'CM' :
    result = distance * 100000
    print(f"Distance = {round(result,2)} CM")

elif from_unit == 'KM' and to_unit == 'M' :
	result = distance * 1000
	print(f"Distance = {round(result,2)} M")
elif from_unit == 'CM' and to_unit == 'M' :
	result = distance / 100
	print(f"Distance = {round(result,2)} M")
elif from_unit == 'MILLI' and to_unit == 'M' :
	result = distance / 1000
	print(f"Distance = {round(result,2)} M")
elif from_unit == 'KM' and to_unit == 'MILLI' :
	result = distance * 1000000
	print(f"Distance = {result} MILLI ")
elif from_unit == 'M' and to_unit == 'MILLI' :
	result = distance * 1000
	print(f"Distance = {result} MILLI ")
elif from_unit == 'CM' and to_unit == 'MILLI' :
	result = distance * 10
	print(f"Distance = {result} MILLI ")
else:
	print("invalid unit inputs")

