G_Solar = [
    [12.5, 14.0, 11.2],
    [15.1, 13.7, 14.5],
    [10.9,12.1, 13.0]
]

energia_total = 0.0

for i in range(len(G_Solar)):
    for j in range(len(G_Solar[i])):
        energia_total += G_Solar[i][j]

print(f"La energia total acumulada en la Grilla solar es de {energia_total:.2f} Kwh")
