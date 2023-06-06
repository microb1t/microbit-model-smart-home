def on_received_number(receivedNumber):
    global angle
    angle = receivedNumber
    pins.servo_write_pin(AnalogPin.P0, angle)
    led.stop_animation()
radio.on_received_number(on_received_number)

angle = 0
radio.set_group(1)
angle = 90
pins.servo_write_pin(AnalogPin.P0, angle)

def on_forever():
    basic.show_number(angle)
basic.forever(on_forever)
