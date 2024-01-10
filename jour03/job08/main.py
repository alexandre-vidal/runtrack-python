def fruitslegumes(type, saison):
    if type == "fruits" and saison == "hiver" :
        print("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "ete":
        print("poire, fraise, cassis")
    elif type == "legumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legumes" and saison == "ete":
        print("artichaut, aubergine, navet")
    
fruitslegumes("fruits", "hiver")
fruitslegumes("fruits", "ete")
fruitslegumes("legumes", "hiver")
fruitslegumes("legumes", "ete")