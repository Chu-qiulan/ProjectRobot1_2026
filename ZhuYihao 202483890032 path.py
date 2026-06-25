
from microbit import display, Image
import tinybit

SPEED_STRAIGHT = 90
SPEED_TURN = 80

display.show(Image.HEART)

def read_track_sensors():
    left = tinybit.traking_sensor_L()
    right = tinybit.traking_sensor_R()
    return left, right

def decide_action(left, right):
    if not left and not right:
        return 'forward'
    elif left and not right:
        return 'left'
    elif not left and right:
        return 'right'
    else:
        return 'stop'

def execute_action(action):
    if action == 'forward':
        tinybit.car_run(SPEED_STRAIGHT)
    elif action == 'left':
        tinybit.car_spinleft(SPEED_TURN)
    elif action == 'right':
        tinybit.car_spinright(SPEED_TURN)
    else:
        tinybit.car_stop()

def main():
    while True:
        left_sensor, right_sensor = read_track_sensors()
        current_action = decide_action(left_sensor, right_sensor)
        execute_action(current_action)

if __name__ == "__main__":
    main()
