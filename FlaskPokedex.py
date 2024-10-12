#11 🔎 Pokédex****
# Crea una Pokédex simple que:
# - Mantenga una lista de Pokémon
# - Permita agregar nuevos Pokémon (nombre, tipo, nivel)
# - Permita buscar Pokémon por nombre
# - Muestre todos los Pokémon registrados
# - Implemente un sistema de evolución basado en el nivel del Pokémon
# - Permita comparar estadísticas entre dos Pokémon

from flask import Flask, render_template, redirect, url_for, flash, request
app=Flask(__name__)
app.secret_key='supersecretkey'


#Modelo Pokemon
class pokemon:
    def __init__(self,entry:int, name:str, types: list,level:int):
        self.entry = entry
        self.name = name
        self.types = types
        self.level = level
        
    
    def searchPokemon(list_pokemon,name_pokemon):        
        for pokemon in list_pokemon:
            if pokemon.name == name_pokemon:
                return pokemon
        return 
    
    def ShowPokemons(list_pokemon):
        for i in list_pokemon:
            print(f"Nombre {i.name}\nTipo {i.types}\nNivel {i.level}")
        return
    
    def AddPokemon(nuevo_pok,list_pokemon):        
        list_pokemon.append(nuevo_pok)
        print(f"{nuevo_pok.name} Agregado")
        return
    
    def EvolutionPokemons(list_pokemon):
        for p in list_pokemon:
            org = p.name
            if p.entry == 1 and p.level >= 16:
                p.entry = 2
                p.name = "Ivysaur"
                print(f"{org} Evoluciono a {p.name}")                
            if p.entry == 2 and p.level >= 34:
                p.entry = 3
                p.name = "Venusaur"    
                print(f"{org} Evoluciono a {p.name}")
            if p.entry == 4 and p.level >= 16:
                p.entry = 5
                p.name = "Charmeleon"
                print(f"{org} Evoluciono a {p.name}")
            if p.entry == 5 and p.level >= 36:
                p.entry = 6
                p.name = "Charizard"
                print(f"{org} Evoluciono a {p.name}")            
            if p.entry == 7 and p.level >= 16:
                p.entry = 8
                p.name = "Wartortle"
                print(f"{org} Evoluciono a {p.name}")
            if p.entry == 8 and p.level >= 36:
                p.entry = 9
                p.name = "Blastoise"
                print(f"{org} Evoluciono a {p.name}")
        return 
    
    
        
   
#Para evolucionar modifique los valores del nivel   
pokemones = [pokemon(1,"Bulbasaur",["Grass","Posion"],12),
            pokemon(4,"Charmander",["Fire"],22),
            pokemon(7,"Squirtle",["Water"],38)
            ]

@app.route('/')
def index():
    return render_template('inicio.html')

if __name__ == '__main__':
    app.run(debug=True)
