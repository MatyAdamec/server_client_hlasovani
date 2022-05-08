radio.set_group(100)
radio.set_transmit_power(10)
radio.set_transmit_serial_number(True)

answers_name = [control.device_serial_number()]
answers = [0]
receiving = True

def recieving_():
    global receiving
    if receiving == True:
        receiving = False
        radio.send_value("enabled", 0)
    else:
        receiving = True
input.on_button_pressed(Button.A, recieving_)

def on_received_value(name, value):
    global receiving, answers_name, answers
    if receiving == True:
        if name == "vote":
            serialcode = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
            if serialcode in answers_name:
                answers[answers_name.index(serialcode)] = value
            else:    
                answers.append(value)
                answers_name.append(serialcode)
        radio.send_value("back", radio.receivedSerial())

radio.on_received_value(on_received_value)

def show_results():
    global answers
    for i in range(1, 27):
        console.log_value(String.from_char_code(64+i),(answers.count(i)))
input.on_button_pressed(Button.B, show_results)

def reset():
    answers = [0]
    answers_name = [control.device_serial_number()]
input.on_logo_event(TouchButtonEvent.PRESSED, reset)
