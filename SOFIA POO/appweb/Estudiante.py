from db import db 

class Estudiante(db.Model):


    #Nombre de tabla

    _tablename_="Estudiantes"


    # Conjunto de atributos que van a ser los campos de la tabla


    #Llave primaria 
    id = db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    email=db.Column(db.String(70))
    codigo=db.Column(db.String(15))

    #Metodo contructor para mapear datos a los campos definidos 

    def _init_(self, nombre, email, codigo):

        self.nombre=nombre
        self.email=email
        self.codigo=codigo

    


from db import db 

class Estudiante(db.Model):


    #Nombre de tabla

    _tablename_="Estudiantes"


    # Conjunto de atributos que van a ser los campos de la tabla

    #Llave primaria 
    id=db.Colum(db.Interger, primary_key=True)
    nombre=db.Colum(db.String(50))
    email=db.Colum(db.String(70))
    codigo=db.Colum(db.String(15))

    #Metodo contructor para mapear datos a los campos definidos 

    def _init_(self, nombre, email, codigo):

        self.nombre=nombre
        self.email=email
        self.codigo=codigo