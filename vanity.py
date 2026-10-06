def main():
    plate = input("Plate:")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if not (2 <= len(plate) <= 6):
        return False

    if not plate.isalnum():
        return False
        
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    for i, char in enumerate(plate):
        if char.isdigit():
            if char == '0':
                return False
            
            for rest in plate[i:]:
                if not rest.isdigit():
                    return False
            break

    return True
main()
