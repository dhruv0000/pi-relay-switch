# DIY Smart Home
This readme was made for my future reference. Dont expect it to be perfect.

## Requirements
- Pi (with wifi access)
- Relay Module
- Female-Female Wire

## What you need to know
Relay is basically a electromagnatic switch you can turn on/off using small electrical currents from your Pi. Learn More here: https://raspberrypi-guide.github.io/electronics/control-electronics-with-a-relay

Key Things to remember:

- Connect one wire of your circuit to `common`
- Connect the other wire to `NO(Normally Open)` if the circuit is broken by default or NC(Normally Connceted) if complete by default.
- If your circuit has ground, it will probably go at `NC(Normally Closed)` and the other wire at NO
.
    - `In`, `GND` and `VCC` connect to your Pi's pins.
    - `In` is the switch. Connect it to a GPIO. (Change the `fan_pin` var in `setup.py` accordingly)
    - `GND` is ground. Duh. Conncet it any ground pin.
    - `VCC` is the operating voltage. Connect to 5V or 3.3V pin depending on the Relay.

## How to run
1. Clone this repo in you Pi

2. Install Flask
```
pip install flask
```

3. Run the Server
```
python server.py
```

4. Control your switch at `localhost:6969` or `ip-address:6969` in any device in your local network. (Run `hostname -I` your Pi to check the ip-address)

## Ref Images
1. 5V Realy
![Relay](5V-relay.jpg)

2. Pi Pins
![Pi](/GPIO.png)
