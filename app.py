#################### IMPORTACION LIBRERIA JSON ####################
import json

#################### IMPORTACION LIBRERIA FLASK ####################
from flask import Flask,render_template,request

#################### IMPORTACION DE CLASE CRUD ####################
from CRUD import CRUD

#################### INICIALIZACION APLICACION DE FLASK####################
app = Flask(__name__)



#################### RUTA PARA MOSTRAR TEMPLATE INDEX ####################
@app.route('/')
def index():
    return render_template('index.html')

#################### FUNCION RESPONSE DATOS A GRAFICA ####################
@app.route('/ajaxChart', methods=['POST'])
def ajaxChart():
    db = CRUD()
    Population = db.GroupByCountry()
    return json.dumps(Population)

#################### FUNCION RESPONSE DATOS CIUDADES MAS POBLADAS ####################
@app.route('/ajaxMostPopulated', methods=['POST'])
def ajaxMostPopulated():
    db = CRUD()
    Top = db.MostPolutedCities()
    return json.dumps(Top)

#################### FUNCION RESPONSE TODOS LOS DATOS DE LA TABLA CIUDAD ####################
@app.route('/ajaxAllCities', methods=['POST'])
def ajaxAllCities():
    db = CRUD()
    Cities = db.ReadAll()
    return json.dumps(Cities)

#################### RUTA PARA MOSTRAR TEMPLATE MODIFYCITIES ####################
@app.route('/Modify-cities')
def ModifyCities():
    return render_template("ModifyCities.html")

#################### FUNCION RESPONSE PARA BORRAR UNA CIUDAD ####################
@app.route('/deleteCity', methods=['POST'])
def DeleteCity():
    db = CRUD()
    ID = request.form.get("id")
    DelCity = db.Delete(ID)
    return DelCity

#################### FUNCION RESPONSE PARA BUSCAR CIUDAD POR ID ####################
@app.route('/seachCityById', methods=['POST'])
def SearchCity():
    db = CRUD()
    ID = request.form.get("id")
    SearchId = db.SearchCityById(ID)
    return json.dumps(SearchId)

#################### FUNCION RESPONSE PARA ACTUALIZAR DATOS DE UNA CIUDAD ####################
@app.route('/UpdateCity', methods=['POST'])
def UpdateCity():
    db = CRUD()
    ID = request.form.get("ID")
    NAME = request.form.get("NAME")
    COUNTRCODE = request.form.get("COUNTRYCODE")
    DISTRICT = request.form.get("DISTRICT")
    POPULATION = request.form.get("POPULATION")
    update = db.Update(ID,NAME,COUNTRCODE,DISTRICT,POPULATION)
    return update

#################### FUNCION RESPONSE PARA CREAR CIUDAD ####################
@app.route('/CreateCity', methods=['POST'])
def CreateCity():
    db = CRUD()
    NAME = request.form.get("NAME")
    COUNTRCODE = request.form.get("COUNTRYCODE")
    DISTRICT = request.form.get("DISTRICT")
    POPULATION = request.form.get("POPULATION")
    create = db.Create(NAME,COUNTRCODE,DISTRICT,POPULATION)
    return create

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
    
