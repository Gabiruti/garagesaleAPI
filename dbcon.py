def config(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
    app.config['MYSQL_DATABASE_DB'] = 'garagesale'
    app.config['MYSQL_CURSOR_CLASS'] = 'DictCursor'




def get_users(cursor,conn):
    cursor.execute(f'SELECT * FROM garagesale.users;')
    resp= cursor.fetchall()
    cursor.close()
    conn.close()
    return resp

def get_stores(cursor,conn,user):
    cursor.execute(f'SELECT * FROM garagesale.stores WHERE email_user NOT LIKE ("{user}");')
    resp= cursor.fetchall()
    print(resp)
    cursor.close()
    conn.close()
    return resp

def get_items(cursor,conn, user):
    cursor.execute(f'SELECT * FROM garagesale.items WHERE store_id = (SELECT idstores FROM garagesale.stores WHERE email_user = ("{user}"));')
    resp= cursor.fetchall()
    cursor.close()
    conn.close()
    return resp

def insert_users(cursor,conn,email):
    cursor.execute(f'INSERT INTO garagesale.users (email) VALUES ("{email}")')
    conn.commit()
    cursor.close()
    conn.close()
    return "boa"

def insert_store(cursor,conn,user,store_name, description, location):
    cursor.execute(f'INSERT INTO garagesale.stores (store_name, about, location, email_user) VALUES ("{store_name}","{description}","{location}","{user}")')
    conn.commit()
    cursor.close()
    conn.close()
    return "boa"

def insert_item(cursor,conn, itemName, descriptionItem, price, idstores):
    cursor.execute(f'INSERT INTO garagesale.items (name, description_item, price, store_id) VALUES ("{itemName}","{descriptionItem}","{price}","{idstores}")')
    conn.commit()
    cursor.close()
    conn.close()
    return "boa"

def delete_item(cursor,conn, iditem):
    cursor.execute(f'DELETE FROM garagesale.items WHERE idItems = ("{iditem}")')
    conn.commit()
    cursor.close()
    conn.close()
    return "DELETADO"


def get_1stores(cursor,conn,user):
    cursor.execute(f'SELECT * FROM garagesale.stores WHERE email_user = "{user}";')
    resp= cursor.fetchall()
    print(resp)
    cursor.close()
    conn.close()
    return resp

def get_idstore(cursor,conn,user):
    cursor.execute(f'SELECT idstores FROM garagesale.stores WHERE email_user = "{user}";')
    resp= cursor.fetchall()
    print(resp)
    cursor.close()
    conn.close()
    return resp

