import sqlite3
import json
class CRUD(object):
#################### CREACION DE BASE DE DATOS SQLITE ####################
    def __init__(self):
        self.conexion = sqlite3.connect("cities.db")
        self.cursor = self.conexion.cursor()

#################### CREACION DE TABLA CITY ####################
    def CreateDB(self):
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS CITY (
                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                NAME VARCHAR(35),
                COUNTRYCODE VARCHAR(3),
                DISTRICT VARCHAR(20),
                POPULATION INTEGER
            );'''
        )

#################### LLENADO DE TABLA CITY ####################
    def PopulateTable(self):
        self.cursor.executescript("""
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Kabul','AFG','Kabol',1780000);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Qandahar','AFG','Qandahar',237500);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Herat','AFG','Herat',186800);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Mazar-e-Sharif','AFG','Balkh',127800);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Amsterdam','NLD','Noord-Holland',731200);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Rotterdam','NLD','Zuid-Holland',593321);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Haag','NLD','Zuid-Holland',440900);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Utrecht','NLD','Utrecht',234323);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Eindhoven','NLD','Noord-Brabant',201843);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Tilburg','NLD','Noord-Brabant',193238);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Groningen','NLD','Groningen',172701);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Breda','NLD','Noord-Brabant',160398);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Apeldoorn','NLD','Gelderland',153491);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Nijmegen','NLD','Gelderland',152463);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Enschede','NLD','Overijssel',149544);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Haarlem','NLD','Noord-Holland',148772);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Almere','NLD','Flevoland',142465);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Arnhem','NLD','Gelderland',138020);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Zaanstad','NLD','Noord-Holland',135621);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('´s-Hertogenbosch','NLD','Noord-Brabant',129170);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Amersfoort','NLD','Utrecht',126270);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Maastricht','NLD','Limburg',122087);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Dordrecht','NLD','Zuid-Holland',119811);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Leiden','NLD','Zuid-Holland',117196);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Haarlemmermeer','NLD','Noord-Holland',110722);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Zoetermeer','NLD','Zuid-Holland',110214);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Emmen','NLD','Drenthe',105853);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Zwolle','NLD','Overijssel',105819);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Ede','NLD','Gelderland',101574);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Delft','NLD','Zuid-Holland',95268);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Heerlen','NLD','Limburg',95052);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Alkmaar','NLD','Noord-Holland',92713);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Willemstad','ANT','Curaçao',2345);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Tirana','ALB','Tirana',270000);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Alger','DZA','Alger',2168000);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Oran','DZA','Oran',609823);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Constantine','DZA','Constantine',443727);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Annaba','DZA','Annaba',222518);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Batna','DZA','Batna',183377);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Sétif','DZA','Sétif',179055);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Sidi Bel Abbès','DZA','Sidi Bel Abbès',153106);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Skikda','DZA','Skikda',128747);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Biskra','DZA','Biskra',128281);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Blida (el-Boulaida)','DZA','Blida',127284);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Béjaïa','DZA','Béjaïa',117162);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Mostaganem','DZA','Mostaganem',115212);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Tébessa','DZA','Tébessa',112007);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Tlemcen (Tilimsen)','DZA','Tlemcen',110242);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Béchar','DZA','Béchar',107311);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Tiaret','DZA','Tiaret',100118);
            INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES ('Ech-Chleff (el-Asnam)','DZA','Chlef',96794);
        """)

#################### CREACION DE ELEMENTO ####################
    def Create(self, name, countryCode, district, population):
        try:
            select = f"SELECT NAME FROM City WHERE NAME = '{name}'"
            if self.cursor.execute(select).fetchone():
                return f"THE CITY {name} IS ALREADY REGISTRED"

            self.cursor.executescript(f"""
                INSERT INTO city (NAME, COUNTRYCODE, DISTRICT, POPULATION)
                VALUES('{name}','{countryCode}','{district}',{population});
            """)
            self.conexion.commit()
            return "SUCCESS, THE CITY HAS BEEN REGISTRED"
        except:
            return "ERROR ON CREATE CITY"

#################### LECTURA DE ELEMENTOS ####################
    def ReadAll(self):
        self.cursor.execute("""
            SELECT * FROM city
        """)
        rows = self.cursor.fetchall()
        dictrow = []
        for r in rows:
            dictrow.append({
                "ID":r[0],
                "NAME": r[1],
                "COUNTRYCODE": r[2],
                "DISTRICT": r[3],
                "POPULATION": r[4]
            })
        return dictrow
#################### ACTUALIZAR ELEMENTO ####################
    def Update(self, id, name, countryCode, district, population):
        try:
            self.cursor.executescript(f"""
                UPDATE city SET 
                    NAME = '{name}',
                    COUNTRYCODE = '{countryCode}',
                    DISTRICT = '{district}',
                    POPULATION = {population}
                WHERE ID = {id}
            """
            )
            self.conexion.commit()
            return "SUCCESS, THE CITY HAS BEEN UPDATED"
        except:
            return "Error on update"

#################### BORRAR ELEMENTO ####################
    def Delete(self, id):
        try:
            self.cursor.executescript(f"""
                DELETE FROM city
                WHERE ID = {id}
            """)
            self.conexion.commit()
            return "SUCCESS, THE CITY HAS BEEN DELETED"
        except sqlite3.OperationalError:
            return "ERROR :C"

#################### AGRUPAR POBLACION POR PAIS ####################
    def GroupByCountry(self):
        self.cursor.execute(f"""
        SELECT COUNTRYCODE, SUM(POPULATION) FROM city
        GROUP BY COUNTRYCODE
        """)
        rows = self.cursor.fetchall()
        dictrows = []
        for r in rows:
            dictrows.append(
                {
                    'name':r[0],
                    'y': r[1]
                }
            )
        return dictrows

#################### LAS CIUDADES MAS POBLADAS ####################
    def MostPolutedCities(self):
        self.cursor.execute("""
            SELECT * FROM CITY
            ORDER BY POPULATION DESC
            LIMIT 5;
        """)
        rows = self.cursor.fetchall()
        dictrow = []
        for r in rows:
            dictrow.append({
                "ID":r[0],
                "NAME": r[1],
                "COUNTRYCODE": r[2],
                "DISTRICT": r[3],
                "POPULATION": r[4]
            })
        return dictrow

#################### DATOS DE UNA CIUDAD POR ID ####################
    def SearchCityById(self, id):
        try:
            self.cursor.execute(f"""
                SELECT * FROM city
                WHERE ID = {id}
            """)
            row = self.cursor.fetchall()
            dictrow = {
                "ID":row[0][0], 
                "NAME":row[0][1],
                "COUNTRYCODE":row[0][2],
                "DISTRICT": row[0][3],
                "POPULATION" : row[0][4]
                }
            return dictrow
        except:
            return "ERROR ON SEARCH CITY BY ID"