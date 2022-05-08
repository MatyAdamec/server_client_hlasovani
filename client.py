radio.set_group(100)
radio.set_transmit_power(10)
radio.set_transmit_serial_number(True)

vote =1
transmitting = True

def on_button_pressed_a():
    global vote
    if transmitting:
        vote +=1
        if vote >=25:
             vote = 1
        basic.show_string(String.from_char_code(64+vote))

def on_button_pressed_b():
    global vote
    if transmitting:
        vote -=1
        if vote < 0:
            vote = 25
        basic.show_string(String.from_char_code(65+vote))

def on_button_pressed_ab():
    global vote
    radio.send_value("vote", vote)

def on_received_value(name, value):
    if name == "enabled":
        if value == 0:
            if transmitting == True:
                transmitting = False
                basic.show_icon(IconNames.NO)
            else:
                transmitting = True
                basic.show_icon(IconNames.YES)
    if name == "back":
        if value == control.device_serial_number():
            music.play_tone(Note.C, music.beat())

radio.on_received_value(on_received_value)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.A, on_button_pressed_a)
