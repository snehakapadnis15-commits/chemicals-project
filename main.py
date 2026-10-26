import csv

def load_chemicals(path):
    chemicals = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            chemicals.append(row)
    return chemicals

def find_heaviest(chemicals):
    heaviest = chemicals[0]
    for chem in chemicals:
        if float(chem["molar_mass"]) > float(heaviest["molar_mass"]):
            heaviest = chem
    return heaviest

chemicals = load_chemicals("chemicals.csv")
heaviest = find_heaviest(chemicals)
print("heaviest compound:", heaviest["name"], heaviest["molar_mass"])
