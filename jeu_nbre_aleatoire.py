#nbre_aleat = random.randint(0 , 100)
nbre_aleat = 8
nbre_entre=0


while nbre_entre != nbre_aleat:
    nbre_entre = input("Essayer de deviner le nombre aleatoire")
    nbre_entre = int(nbre_entre)

    if nbre_entre < nbre_aleat:
        notation = "Votre nombre est plus petit"
    elif nbre_entre > nbre_aleat:
        notation = "Votre nombre est plus grand"
    else:
        notation = "Bravoooooooh!!!!!! vous avez trouvé le nombre juste"

    print(notation)



