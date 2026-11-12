def open_doll(s):
    if s <= 1:
        return {"size": s, "inner doll": None}
    
    return  {"size": s, "inner doll": open_doll(s - 1)}

print(open_doll(4))