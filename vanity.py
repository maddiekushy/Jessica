def main():
    plate = input("Plate:")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(p):
    if not (2 <= len(p) <= 6):
        return False

    if not p.isalnum():
        return False
        
    if not (p[0].isalpha() and p[1].isalpha()):
        return False

    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0':
                return False
            
            for rest in p[i:]:
                if not rest.isdigit():
                    return False
            break

    return True

main()

