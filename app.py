from flask import Flask,request,render_template,jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process',methods= ['POST'])
def process():
  weight_in_kg  = float(request.form['weight_in_kg'])
  height_in_foot_and_inches = float(request.form['height_in_foot_and_inches'])
  height_in_meters=0.304* float(height_in_foot_and_inches)
  output = str(weight_in_kg / (height_in_meters*height_in_meters))
  bmi =float(output)
  if bmi <=18.5:
    return jsonify({'output':'You are Under weight as your bmi is: ' + output})
  elif (bmi >=18.5) and (bmi <=24.9):
    return jsonify({'output':'Perfect!You have normal weight and your bmi is : '+ output})
  elif bmi >=25 and bmi <=29.9:
   return jsonify({'output':'You are Overweight as your bmi is: ' + output})
  elif bmi>=30:
   return jsonify({'output':'You are highly obese as your bmi is: ' + output})
  else :
   return jsonify({'output':'and your bmi is : '+ output})
  return jsonify({'error' : 'Missing data!'})