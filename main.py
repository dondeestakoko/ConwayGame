import numpy as np

frame = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

def compute_number_neighbors(paded_frame, index_line, index_column):
    """
    Cette fonction prend en entrée la matrice avec bordure et
    renvoie le nombre de cellules voisines vivantes.
    """
    number_neighbors = 0
    for line in range(-1, 2): #passer sur l'element precedent actuelle et suivant des lignes
        for column in range(-1, 2): # et des colonnes
            if not (line == 0 and column == 0):
                #calculer la vrai position du voisin
                neighbor_row = index_line + line  
                neighbor_col = index_column + column
                #la somme des voisins 
                number_neighbors += paded_frame[neighbor_row, neighbor_col]

    return number_neighbors

print(compute_number_neighbors(frame, 2, 3))

def compute_next_frame(frame):
    """
    Cette fonction prend en entrée une frame et calcule la frame suivante
    à partir des règles du jeu de la vie
    """
    paded_frame = np.pad(frame, 1, mode="constant") # je vous offre le code pour le zéro padding c'est cadeau !
    """
    # Étape 1 : 2 boucles for imbriquées pour parcourir la matrice avec bordure (zero padding) element par element.
    Faites attention à l'index de début et d'arrêt ! (il s'agit de la matrice avec bordure)

    # L'étape 2 et 3 se font au cours de la même itération (attention à l'indentation !)
    """
    frame_modify = paded_frame.copy() # creation d'une copie à modifer (apparament si je fait une simple assignation quand je modify le array ils changes tous les deux)
    # recuperationration de la taille des lignes et des colonnes
    rows, cols = frame_modify.shape
    print(rows, cols)
    for line in range(1, rows-1):
        for column in range(1, cols-1):
            number_neighbors = compute_number_neighbors(paded_frame, line, column) #voir combien de voisin
            if (paded_frame[line, column] == 0) and (number_neighbors == 3): 
                frame_modify[line, column] = 1
            elif paded_frame[line, column] == 1 and (number_neighbors in [2, 3]):
                continue #ne rien faire 
            else : frame_modify[line, column] = 0
    """
    # Étape 3 : Pour chacun des éléments faire les tests (état de l'élément et son nombre de voisin) afin de voir
    si il y a des modifications à faire.
    Si c'est le cas effectuez les modifications directement dans la matrices frame (Attention à l'indice
    utilisé ! )"""
    
    return frame_modify

print(compute_next_frame(frame))

"""while True:
    # boucle infini qui affiche toutes les frames successives (ctrl + c pour arrêter le script)
    print(frame)
    frame = compute_next_frame(frame)"""
