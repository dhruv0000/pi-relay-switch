from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/fan/1')
def fan_on():
  try:
    print("Fan On")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, False)
    return redirect(url_for('index'))
  except:
    return "<p>Error Bro</p>"

@app.route('/fan/0')
def fan_off():
  try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, True)
    return redirect(url_for('index'))
  except:
    return "<p>Error Bro</p>"
 

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 6969))
    app.run(host='0.0.0.0', port=port)
