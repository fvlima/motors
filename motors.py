import keyboard
import RPi.GPIO as GPIO

motor_1 = (16, 18, 22)
motor_2 = (19, 21, 23)


def init_motor(motor):
    for n in motor:
        GPIO.setup(n, GPIO.OUT)

        
def init_motors():
    GPIO.setmode(GPIO.BOARD)
    init_motor(motor_1)
    init_motor(motor_2)    

        
def stop_motor(motor):
    GPIO.output(motor[2], GPIO.LOW)

    
def stop_motors(cleanup=True):
    stop_motor(motor_1)
    stop_motor(motor_2)
    if cleanup:
        GPIO.cleanup()


def go_forward(motor):
    GPIO.output(motor[0], GPIO.HIGH)
    GPIO.output(motor[1], GPIO.LOW)
    GPIO.output(motor[2], GPIO.HIGH)


def go_back(motor):
    GPIO.output(motor[0], GPIO.LOW)
    GPIO.output(motor[1], GPIO.HIGH)
    GPIO.output(motor[2], GPIO.HIGH)


def go_right(motor):
    go_forward(motor)


def go_left(motor):
    go_back(motor)


def main():
    init_motors()
    try:
        while True:
            if keyboard.is_pressed('up'):
                print('UP')
                go_forward(motor_2)
            elif keyboard.is_pressed('down'):
                print('DOWN')
                go_back(motor_2)
            elif keyboard.is_pressed('left'):
                print('LEFT')
                go_left(motor_1)
            elif keyboard.is_pressed('right'):
                print('RIGHT')
                go_right(motor_1)
            else:
                stop_motors(cleanup=False)
    except KeyboardInterrupt:
        print('BYE')
        stop_motors()


if __name__ == '__main__':
    main()
