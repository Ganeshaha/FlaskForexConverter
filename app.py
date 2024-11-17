from flask import Flask, request, render_template, session, jsonify, flash
import json, requests
##from flask_debugtoolbar import DebugToolbarExtension

app=Flask("__forex__")
app.debug = True
app.config['SECRET_KEY'] = 'my_key'

@app.route('/')
def main_page():

    return render_template("converter.html")

@app.route('/submit', methods = ['POST'])
def submit():


    #print(json.loads(request.data)['fromValue'])
    #print(json.loads(request.data)['toValue'])
    #print(json.loads(request.data)['amountValue'])

    from_value = json.loads(request.data)['fromValue']
    to_value = json.loads(request.data)['toValue']
    amount_value = json.loads(request.data)['amountValue']

    access_key = '780e37fe1e205ee915a6e4f0c6bf4830'
    response_string = f"http://api.exchangerate.host/convert?access_key={access_key}&from={from_value}&to={to_value}&amount={amount_value}&format=1"
    print(response_string)
    try:
        response = requests.get(response_string)
        response.raise_for_status()
        data = response.json()

        #for key in data:{ 
        #print(key,":", data[key]) }
      
            
      #  if data['success']  == 'False':
           # flash(f'{data["error"]["info"]}')     


    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
    except Exception as err:
        return jsonify({'error': f'Other error occurred: {http_err}'}), 500
    

    return data