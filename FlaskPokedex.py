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
class Pokemon:
    def __init__(self,entry:int, name:str, types: list,level:int):
        self.entry = entry
        self.name = name
        self.types = types
        self.level = level
        

    
 #Modelo Pokemons
class Pokemons:
    def __init__(self):
        self.pokemons = {}   
    
    def Add_pokemon(self, entry, name, types,level):
        if entry in self.pokemons:
            flash("El pokemon ya Existe")
        else:
            self.pokemons[entry] = Pokemon(entry, name, types,level)
            flash(f"Pokemon agregado con el nombre {name}")
        
   

pokemones = Pokemons()
@app.route('/')
def index():
    return render_template('inicio.html')


@app.route('/Add_pokemon', methods= ['GET', 'POST'])
def Add_pokemon():
    if request.method == 'POST':
        entry= request.form['entry']
        pokemon= request.form['name_pokemon']
        tipo= request.form['name_pokemon']
        level= int(request.form['level'])
        
        if pokemon in pokemones.pokemons:
            flash(f"El pokemon Ya Existe")
        else:
            pokemones.Add_pokemon(entry,pokemon,tipo,level)
        return redirect(url_for('index'))
    return render_template('Add_pokemon.html')

if __name__=="__main__":
    app.run(debug=True)

