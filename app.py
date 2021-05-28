
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            pre=int(request.form['pre'])
            glu = float(request.form['glu'])
            bp = float(request.form['bp'])
            st = float(request.form['st'])
            ins = float(request.form['ins'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = int(request.form['age'])
            filename = 'model.sav'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            scaler = pickle.load(open('scaler.sav', 'rb')) # loading scaler file from storage
            # predictions using the loaded model file
            prediction=loaded_model.predict(scaler.transform([[pre,glu,bp,st,ins,bmi,dpf,age]]))
            print('prediction is', prediction)
            # showing the prediction results in a UI
            if prediction[0]==1:
                return render_template('results.html',prediction='diabetic')
            else:
                return render_template('results.html', prediction='not diabetic')
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app