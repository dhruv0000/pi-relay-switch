from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO
import os

app = Flask(__name__)

fan_pin = 16
light_pin = 15

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/fan/<int:value>')
def fan(value=0):
  if(change_gpio_out(fan_pin,value)):
    return redirect(url_for('index'))
  return "<p>Error mate!</p>"

@app.route('/light/<int:value>')
def ligth(value=0):
  if(change_gpio_out(light_pin,value)):
    return redirect(url_for('index'))
  return "<p>Error mate!</p>"

@app.route('/light/switch')
def ligth_switch():
  if(change_gpio_out(light_pin,None)):
    return redirect(url_for('index'))
  return "<p>Error mate!</p>"

# Change the output of a specific `pin`.
def change_gpio_out(pin:int,value: int):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pin, GPIO.OUT)

  if value==None:
    if GPIO.input(pin)==GPIO.LOW:
      value=1
    else:
      value=0
  
  try:
    GPIO.output(pin, value)
    return True
  except:
    return False

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 6969))
    app.run(host='0.0.0.0', port=port)
