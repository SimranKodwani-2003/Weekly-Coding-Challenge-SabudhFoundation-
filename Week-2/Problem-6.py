def roman(sym):
    
    rom_value={
        "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
        "XL": 40, "L": 50, "XC": 90, "C": 100,
        "CD": 400, "D": 500, "CM": 900, "M": 1000
    }

    n=0
    i=0
    while i<len(sym):
        if i + 1 < len(sym) and sym[i:i+2] in rom_value:
            n += rom_value[sym[i:i+2]]
            i += 2  # mmove ahead by 2 places
        else:
            n += rom_value[sym[i]]
            i += 1  # move ahead by 1 place

    return n
    
sym = "MCMXCIV"
print(roman(sym))