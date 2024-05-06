# Se importan las librerías necesarias
import time
import board
import digitalio
import pwmio
import random

# Funcion que genera el indicador del tipo de portero que va a jugar en el turno
def generar_aleatorios():
    num_AN = random.randint(1, 3)
    grupos_AN1 = random.randint(1, 3)
    grupos_AN2 = random.randint(1, 2)
    grupos_AN3 = random.randint(1, 2)
    return num_AN, grupos_AN1, grupos_AN2, grupos_AN3

num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()

# Funcion que asigna los leds que se van a prender segun lo que se genere en generar_aleatorios()
def AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3):
    if num_AN == 1:
        if grupos_AN1 == 1:
            led_pins = [board.GP4, board.GP5]
            pins_botones = [16, 17]
        elif grupos_AN1 == 2:
            led_pins = [board.GP6, board.GP7]
            pins_botones = [18, 19]
        elif grupos_AN1 == 3:
            led_pins = [board.GP8, board.GP9]
            pins_botones = [20, 21]
    elif num_AN == 2:
        if grupos_AN2 == 1:
            led_pins = [board.GP4, board.GP5, board.GP6]
            pins_botones = [16, 17, 18]
        elif grupos_AN2 == 2:
            led_pins = [board.GP7, board.GP8, board.GP9]
            pins_botones = [19, 20, 21]
    elif num_AN == 3:
        if grupos_AN3 == 1:
            led_pins = [board.GP4, board.GP6, board.GP8]
            pins_botones = [16, 18, 20]
        elif grupos_AN3 == 2:
            led_pins = [board.GP7, board.GP5, board.GP9]
            pins_botones = [17, 19, 21]

    leds = [digitalio.DigitalInOut(pin) for pin in led_pins]
    for led in leds:
        led.direction = digitalio.Direction.OUTPUT
    return pins_botones, leds

#Aqui se definen los botones y el pin al que esta asociado cada uno
button_pin4 = board.GP16
button_pin5 = board.GP17
button_pin6 = board.GP18
button_pin7 = board.GP19
button_pin8 = board.GP20
button_pin9 = board.GP21

button4 = digitalio.DigitalInOut(button_pin4)
button5 = digitalio.DigitalInOut(button_pin5)
button6 = digitalio.DigitalInOut(button_pin6)
button7 = digitalio.DigitalInOut(button_pin7)
button8 = digitalio.DigitalInOut(button_pin8)
button9 = digitalio.DigitalInOut(button_pin9)

button4.direction = digitalio.Direction.INPUT
button5.direction = digitalio.Direction.INPUT
button6.direction = digitalio.Direction.INPUT
button7.direction = digitalio.Direction.INPUT
button8.direction = digitalio.Direction.INPUT
button9.direction = digitalio.Direction.INPUT

# Definicion del mini parlante
buzzer_pin = board.GP15
buzzer = pwmio.PWMOut(buzzer_pin, variable_frequency=True)

print(num_AN, "-", grupos_AN1, "-", grupos_AN2, "-", grupos_AN3)

# Funcion que genera el sonido de victoria
def gol():
    frequencies = [1000, 1500, 2000, 2500] # Funciona con onda de seno
    for frequency in frequencies:
        buzzer.frequency = frequency
        buzzer.duty_cycle = 2**15
        time.sleep(0.2)
        buzzer.duty_cycle = 0
        time.sleep(0.1)

# Funcion que genera sonido de perdedor
def no_gol():
    frequencies = [200, 200, 200, 200]
    for frequency in frequencies:
        buzzer.frequency = frequency
        buzzer.duty_cycle = 2**15
        time.sleep(0.2)
        buzzer.duty_cycle = 0
        time.sleep(0.1)
pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)

while True:   # En este while se va a definir cuando se reproduce gol() y cuando no_gol() dependiendo de si esta en la lista de leds que se definia en AN()

    if button4.value:
        for led in leds:
            led.value = True
        if 16 in pins_botones:
            no_gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
        else:
            gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
    elif button5.value:
        for led in leds:
            led.value = True
        if 17 in pins_botones:
            no_gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
        else:
            gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
    elif button6.value:
        for led in leds:
            led.value = True
        if 18 in pins_botones:
            no_gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
        else:
            gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
    elif button7.value:
        for led in leds:
            led.value = True
        if 19 in pins_botones:
            no_gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
        else:
            gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
    elif button8.value:
        for led in leds:
            led.value = True
        if 20 in pins_botones:
            no_gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
        else:
            gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
    elif button9.value:
        for led in leds:
            led.value = True
        if 21 in pins_botones:
            no_gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
        else:
            gol()
            time.sleep(3)
            for led in leds:
                led.value = False
                led.deinit()
            num_AN, grupos_AN1, grupos_AN2, grupos_AN3 = generar_aleatorios()
            pins_botones, leds = AN(num_AN, grupos_AN1, grupos_AN2, grupos_AN3)
    
