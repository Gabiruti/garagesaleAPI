# GaragesaleAPI
Uma API desenvolvida em python, utilizando a biblioteca Flask e o banco de dados MySQL.

# Requisitos para executar
- [Pycharm](https://www.jetbrains.com/pt-br/pycharm/) - Não é exatamente um "Requisito", mas eu recomendo pois facilita instalar bibliotecas e instanciar um ambiente de desenvolvimento.
- [Python](https://www.python.org/)
- [MySQL](https://www.mysql.com/)

# Bibliotecas
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - Versão utilizada 2.1.2.
- [Flask-MySQL](https://flask-mysql.readthedocs.io/en/stable/) - Versão utilizada 1.5.2.
- [PyMySQL](https://pymysql.readthedocs.io/en/latest/) - Versão utilizada 1.0.2.

# Como Executar
Para iniciar a API basta executar o arquivo `main.py`.

# Porta de execução
Voce pode mudar a porta de execução da API mundando o 'port':

```
if __name__ == "__main__":
    app.run(port=8080, debug=True)
```
Isso pode ajudar caso a sua aplicação esteja rodando em outra porta e não esteja conseguindo acessar a API. Caso você não queira que a API rode na mesma porta que sua aplicação, basta dar um `port foward` na porta em que a API estiver em execução:

```
adb reverse tcp:8080 tcp:8080
```


