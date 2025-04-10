edat = 17

#Condicionals: if, else, elif
if edat>=18:
    print("És major d'edat.")
else:
    print("És menor d'edat.")

if edat>=18:
    print("És major d'edat.")
elif edat==17.5:
    print("És un pobret.")
else:
    print("És menor d'edat.")


#Bucles: while, for
edatMotillo = 12

while edatMotillo < 16:
    print(f"No pot tenir moto, té {edatMotillo} anys.")
    if edatMotillo == 14:
        print(f"Epp, motillo(AB), té {edatMotillo} anys.") 
        break
    edatMotillo += 1

while edatMotillo < 18:
    print(f"No pot cotxe, té {edatMotillo} anys.")
    edatMotillo += 1

print(f"Ja toca cotxe, té {edatMotillo} anys.")

