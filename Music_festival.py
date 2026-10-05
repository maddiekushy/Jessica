bands = {}
band = input(“Enter a Musician:")

while band != “done”:
  if band.lower() in bands:
	  bands[band.lower()] += 1
  else:
	  bands[band.lower()] = 1

for key in bands:
	print("votes:" + key + “:” + str(bands[key]))
