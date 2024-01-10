def moyenne(note1, note2, note3):
    moyenne == float(note1) + float(note2) + float(note3) / 3
    if moyenne >= 15 and moyenne < 21:
        print("Très bon élève")
    elif moyenne >= 11 and moyenne < 15:
        print("Bon élève")
    elif moyenne >= 8 and moyenne < 11:
        print("lève moyen")
    elif moyenne >=0 and moyenne < 8:
        print("lève devant faire des efforts")
    
moyenne(input("Insérez une 1ère note entre 0 et 20 : "), input("Insérez une 2ème note entre 0 et 20 : "), input("Insérez une 3ème note entre 0 et 20 : "))