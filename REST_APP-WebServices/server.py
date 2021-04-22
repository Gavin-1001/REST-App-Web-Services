from flask import Flask,request,render_template
from flask import request
from datetime import datetime
import pika
import requests
import json
from data import setup
from schema import schema
from graphene.test import Client
import xmlrpc.client
import urllib.request
import hprose
from ping_hp import hpping
import socket


app = Flask(__name__)

@app.route('/')
def homepage():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/ \n')
    f.close()
    return render_template('index.html')

@app.route('/weather')
def press_for_msg():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/ \n')
    f.close()
    return render_template('messages.html')


@app.route('/weather', methods=['POST'])
def wait_for_msg():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '\ \n')
    f.close()

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='weather')


    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)


    channel.basic_consume(
        queue='weather', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    return 'Check Console for Messages'

@app.route('/justweather')
def weather():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/justweather \n')
    f.close()

    with urllib.request.urlopen('http://kylegoslin.pythonanywhere.com/') as f:
        content = f.read().decode('utf-8')
        var = json.loads(content)
        x = var['forecast']

    output ='{ date: \"' + y + '\"' + ', weather: \"' + x + '\"}'
    f.close()
    return output

@app.route('/updates')
def updates_function():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/updates \n')
    f.close()

    out = ' '

    f = open('updates.txt', 'r')
    x = f.readlines()

    '''
    This for loop will run over the lines in the file and print them to the console.

    '''

    output = '{'

    for item in x:
        output = output + '"update": "'+item + '",'
    f.close()
    output = output[:-1]
    output = output + '}'
    return output

@app.route('/ping')
def ping_function():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/ping pong \n')
    f.close()
    return 'pong  ' + str(y)

@app.route('/callClient')
def get_input():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/callClient \n')
    f.close()
    return render_template('input.html')

@app.route('/callClient', methods=['POST'])
def call_client():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/callClient POST \n')
    f.close()
    text = request.form['text']
    with xmlrpc.client.ServerProxy("http://localhost:8001/") as proxy:
        print('connected')
    return "and our survey says!: %s" % str(proxy.temp_resolve(int(text)))

@app.route('/insertStudent')
def insertStudent():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/insertStudent \n')
    f.close()

    fn = request.args.get('firstname','')
    ln = request.args.get('lastname', '')
    id = request.args.get('id')
    with open('users.log', 'a') as f:
        f.write(fn+ '  ' + ln + '  ' + id +'\n')
    f.close()
    return 'Inserting new student: ' + fn + ln

@app.route('/student')
def get_student_input():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/student \n')
    f.close()
    return render_template('student.html')

@app.route('/student', methods=['POST'])
def retrieve_student():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/student POST \n')
    f.close()
    name = request.form['name']
    id = request.form['id']
    dob = request.form['dob']

    setup()
    client = Client(schema)
    name_query = """
        query FetchNameQuery($name: String!) {
            studentByName(name: $name) {
                id
                name
                dob
            }
        }
    """

    dob_query = """
        query FetchDobQuery($dob: String!) {
            studentByDob(dob: $dob) {
                id
                name
                dob
            }
        }
    """

    id_query = """
        query FetchIdQuery($id: String!) {
            studentById(id: $id) {
                id
                name
                dob
            }
        }
    """
    name_params = {"name":name}
    dob_params = {"dob": dob}
    id_params = {"id": id}
    if name != '':
        result_name = client.execute(name_query, variables=name_params)
        return 'and our survey says!:' + (str(result_name))
    elif id != '':
        result_id = client.execute(id_query, variables=id_params)
        return 'and our survey says!:' + (str(result_id))
    elif dob != '':
        result_dob = client.execute(dob_query, variables=dob_params)
        return 'and our survey says!:' + (str(result_dob))

    return 'You didn\'t search for anything'

@app.route('/pingpong')
def ping():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/ping ip\n')
    f.close()
    client = hprose.HttpClient('http://127.0.0.1:8080/')
    return client.ping()

@app.route('/pingserver')
def ping_server_start():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/ping_server \n')
    f.close()
    return render_template('hprose.html')

@app.route('/pingserver', methods=['POST'])
def ping_server():
    f = open('calls.log', 'a')
    y = datetime.now()
    y = y.strftime("%d/%m/%Y %H:%M:%S")
    f.write(str(y) + '/ping_server POST\n')
    f.close()
    server = hprose.HttpServer(port = 8181)
    ip = socket.gethostbyname(socket.gethostname())
    def ping():
    	return ip
    server.addFunction(ping)
    server.start()
