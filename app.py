from flask import Flask, render_template
import mysql.connector
from credenziali import host, user, password, database

app = FLask(__name__)

def connetti_al_database():
  connessione = mysql.connector(
    host = host,
    user = user,
    password = password,
    database = database
  )

  return connessione

@app.route("/")
def home():
  connessione = connetti_al_database()

  cursore = connessione.cursor()

  cursore.execute('SELECT * FROM boh')

  lista_prodotti = cursore.fecthall()

  connessione.close()

  return render_template("index.html", prodotti=lista_prodotti)

if __name__ == "__main__":
    app.run(debug=True)  