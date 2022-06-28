from flask import Flask
from flask import jsonify, request
from dbcon import *
import json
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


app = Flask(__name__)

#Instanciar o objeto MySQL
mysql = MySQL(cursorclass=DictCursor)
#Ligar o MYSQL ao Flask
mysql.init_app(app)
#configurar
config(app)

@app.route('/', methods=['GET'])
def inicio():
    return "FLASK API"

#Mostra Usuários
@app.route('/users', methods=['GET'])
def show_users():
    conn = mysql.connect()
    cursor = conn.cursor()
    respo = get_users(cursor,conn)
    return jsonify(respo)

#Mostra lojas
@app.route('/store', methods=['GET'])
def show_stores():
    user = request.args.get('user')
    print(user)
    conn = mysql.connect()
    cursor = conn.cursor()
    respo = get_stores(cursor,conn, user)
    return jsonify(respo)

#Mostra items
@app.route('/items', methods=['GET'])
def show_items():
    user = request.args.get('user')
    conn = mysql.connect()
    cursor = conn.cursor()
    respo = get_items(cursor,conn, user)
    return jsonify(respo)

#Método Post
@app.route('/insert', methods=['GET','POST'])
def insert_user():
    if request.method == 'POST':
        email = request.json['userEmail']
        conn = mysql.connect()
        cursor = conn.cursor()
        respo = insert_users(cursor,conn, email)
        return respo
    else:
        return "outro"

@app.route('/createStore', methods=['GET','POST'])
def insert_stores():
    if request.method == 'POST':
        user = request.json['userEmail']
        store_name= request.json['storename']
        description = request.json['about']
        location = request.json['location']

        conn = mysql.connect()
        cursor = conn.cursor()
        respo = insert_store(cursor,conn, user, store_name, description, location)
        return respo
    else:
        return "outro"

@app.route('/getstore', methods=['GET'])
def show_1store():
    user = request.args.get('user')
    conn = mysql.connect()
    cursor = conn.cursor()
    respo = get_1stores(cursor,conn, user)
    return jsonify(respo)

@app.route('/getidstore', methods=['GET'])
def getidstore():
    user = request.args.get('user')
    conn = mysql.connect()
    cursor = conn.cursor()
    respo = get_idstore(cursor,conn,user)
    return jsonify(respo)

@app.route('/additem', methods=['GET','POST'])
def insertitem():
    if request.method == 'POST':
        itemName = request.json['itemName']
        descriptionItem= request.json['descriptionItem']
        price = request.json['price']
        idstores = request.json['idstores']

        conn = mysql.connect()
        cursor = conn.cursor()
        respo = insert_item(cursor,conn, itemName, descriptionItem, price, idstores)
        return respo
    else:
        return "outro"

@app.route('/deleteitem', methods=['GET','DELETE'])
def deleteitem():
    iditem = request.args.get('iditem')
    print(iditem)
    conn = mysql.connect()
    cursor = conn.cursor()
    delete_item(cursor,conn, iditem)
    return "DELETADO"

if __name__ == "__main__":
    app.run(port=8080, debug=True)