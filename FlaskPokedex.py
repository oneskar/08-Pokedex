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
        
    def Search(self):        
        return (f"{self.name}, es tipo {self.types} y esta a nivel {self.level}.")
    
    def Show(self):        
        return self
        #return (f"Numero: {self.entry}\nPokemon: {self.name}\nTipo: {self.types}\nNivel: {self.level}\n******\n")
        #return  self.entry,self.name,self.types,self.level
        

    
 #Modelo Pokemons
class Pokemons:
    def __init__(self):
        self.pokemons = {}   
    
    def Add(self, entry, name, types,level):
        if entry in self.pokemons:
            flash("El pokemon ya Existe")
        else:
            self.pokemons[entry] = Pokemon(entry, name, types,level)
            flash(f"{name} ha sido agregado al Pokedex")
        
   

pokemones = Pokemons()
@app.route('/')
def index():
    return render_template('inicio.html')


@app.route('/Add', methods= ['GET', 'POST'])
def Add():
    if request.method == 'POST':
        numero= request.form['entry']
        pokemon= request.form['name']
        tipo= request.form['types']
        nivel= int(request.form['level'])
        
        if pokemon in pokemones.pokemons:
            flash(f"El pokemon Ya Existe")
        else:
            pokemones.Add(numero,pokemon,tipo,nivel)
        return redirect(url_for('index'))
    return render_template('Add.html')


@app.route('/Search', methods=['GET', 'POST'])
def Search():
    if request.method == 'POST':
        Numero = request.form['entry']
        if Numero in pokemones.pokemons:
            name = pokemones.pokemons[Numero].Search()            
            flash(f"El #{Numero} corresponde al pokemon>> {name}")
        else:
            flash("El pokemon no ha sido Ingresado")
        return redirect(url_for('index'))
    return render_template('Search.html')


@app.route('/Show', methods=['GET', 'POST'])
def Show():
    for pkm in pokemones.pokemons:            
        descripcion = pokemones.pokemons[pkm].Show()           
        #flash(f"{descripcion}")          
        
        flash(f"Numero: {descripcion.entry}\n")
        flash(f"Pokemon: {descripcion.name}\n")
        flash(f"Tipo: {descripcion.types}\n")
        flash(f"Nivel: {descripcion.level}\n")
        flash("********\n")
    return redirect(url_for('index'))



if __name__=="__main__":
    app.run ('0.0.0.0', 5000, debug=True)
    #app.run (debug=True)

