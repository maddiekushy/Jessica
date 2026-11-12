def fractal(n):
    if len(n) == 1:
        print(n[0])
    
    else:
        print(n[0])
        fractal(n[1:])
        print(n[0])

print(fractal(["***", "**", "*"]))