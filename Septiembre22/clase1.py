
#crear cuenta en github
#relacionar clave ssh, antes del push

juego={
    "personajes":[
                    {"nombre":[{"nombre1":"Darsamat","apellido":"hernen"}],"tipo":"mago","level":23,"password":"320320"},
                    {"nombre":[{"nombre1":"JuanElGuerrero","apellido":"jimenez"}],"tipo":"guerrero","level":22,"password":"13213123"},
                    {"nombre":[{"nombre1":"juan","apellido":"perez"}],"tipo":"elfo","level":24,"password":"32323213"},
                 ],
    }

def game():
    for i in juego:
        for n in juego[i]:
            a=(n["nombre"][0]["nombre1"])
            b=(n["password"])
            total=a+" "+b
            print(total)

game()

