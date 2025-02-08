def roman(num):
    
    rom_value=[
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]

    rom=""
    for value, symbol in rom_value:
        while num>=value:
            rom+=symbol
            num=num-value
    return rom
    
num = 3749
print(roman(num))