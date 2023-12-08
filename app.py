from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '34.93.131.182'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mohitdixit12345!'
app.config['MYSQL_DB'] = 'demo'

mysql = MySQL(app)

@app.route('/')
def hello_geek():
    #Creating a connection cursor
    cursor = mysql.connection.cursor()
	 
    #Executing SQL Statements
    cursor.execute(''' INSERT INTO users (name,email) VALUES('sad','abc@gmail.com') ''')
	 
    #Saving the Actions performed on the DB
    mysql.connection.commit()
	 
    #Closing the cursor
    cursor.close()	
    return '<h6>Welcome from Flask</h6>'


if __name__ == "__main__":
    app.run(debug=True)
