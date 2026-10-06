bands = {}

while True:
    band = input("Enter an artist's name or type 'done' to finish voting: ").strip()
    
    if band.lower() == 'done':
        break

    if not user_input:
        continue
    
    if user_input in bands:
        bands[band] += 1
    else:
        bands[band] = 1

band_keys = list(bands.keys())

print("\n--- Votes ---")
for band in band_keys:
    print(f"{band}: {bands[band]}")
