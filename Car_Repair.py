from flask import Flask, request, jsonify, render_template
import mysql.connector
from datetime import datetime

app = Flask(__name__)

#Configuración de la base de datos
db = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)
cursor = db.cursor()

# Ruta principal: formulario de registro
@app.route('/')
def home():
    return render_template('register.html')

# Ruta para registrar un cliente
@app.route('/register', methods=['POST'])
def register_customer():
    if request.method == 'POST':
        try:
            # Recoger los datos enviados desde el formulario
            data = request.form

            name = data['name']
            phone = data['phone']
            email = data['email']
            gender = data['gender']
            problem = data['problem']
            car_brand = data['car_brand']
            car_model = data['car_model']
            car_year = data['car_year']
            wants_prayer = 'prayer_request' in data  # Si el checkbox está marcado

            # Insertar los datos en la base de datos
            query = """INSERT INTO customers 
                       (name, phone, email, gender, problem, car_brand, car_model, car_year, wants_prayer, created_date) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, CURDATE())"""
            cursor.execute(query, (name, phone, email, gender, problem, car_brand, car_model, car_year, wants_prayer))
            db.commit()

            # Devolver respuesta JSON indicando éxito
            return jsonify({"message": "Registro exitoso"})

        except Exception as e:
            return jsonify({"message": "Error al registrar el cliente", "error": str(e)})

# Ruta para listar los clientes
@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        # Obtener todos los registros de la base de datos
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()

        # Renderizar la plantilla HTML y pasar los datos
        return render_template('customers.html', customers=customers)

    except Exception as e:
        return jsonify({"message": "Error al obtener la lista de clientes", "error": str(e)})

# Ruta para ver los detalles de un cliente específico
@app.route('/view_previous/<int:customer_id>', methods=['GET'])
def view_previous(customer_id):
    try:
        # Obtener los detalles del cliente por ID
        query = """
            SELECT * FROM customers 
            WHERE id = %s
        """
        cursor.execute(query, (customer_id,))
        customer = cursor.fetchone()

        if customer:
            # Mostrar los detalles del cliente
            return render_template('customer_details.html', customer=customer)
        else:
            return "No se encontró un registro para este cliente", 404
    except Exception as e:
        return jsonify({"message": "Error al obtener los registros", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)


