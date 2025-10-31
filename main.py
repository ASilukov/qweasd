def a():
    magicbit.motor_run(magicbit.Motors.M1, randint(-255, 255))
    magicbit.motor_run(magicbit.Motors.M2, randint(-255, 255))
    magicbit.motor_run(magicbit.Motors.M3, randint(-255, 255))
    magicbit.motor_run(magicbit.Motors.M4, randint(-255, 255))
def doSomething():
    basic.show_icon(randint(0,21))
basic.show_icon(IconNames.HEART)
magicbit.motor_run(magicbit.Motors.M1, randint(-255, 255))
magicbit.motor_run(magicbit.Motors.M2, randint(-255, 255))
magicbit.motor_run(magicbit.Motors.M3, randint(-255, 255))
magicbit.motor_run(magicbit.Motors.M4, randint(-255, 255))
basic.show_icon(IconNames.GHOST)
icons = [IconNames.HEART,
    IconNames.HAPPY,
    IconNames.SAD,
    IconNames.ANGRY,
    IconNames.CONFUSED,
    IconNames.ASLEEP,
    IconNames.SURPRISED,
    IconNames.SILLY,
    IconNames.FABULOUS,
    IconNames.MEH,
    IconNames.YES,
    IconNames.NO,
    IconNames.TRIANGLE,
    IconNames.SQUARE,
    IconNames.DIAMOND,
    IconNames.CHESSBOARD,
    IconNames.DUCK,
    IconNames.HOUSE,
    IconNames.TORTOISE,
    IconNames.BUTTERFLY,
    IconNames.GHOST,
    IconNames.COW]

def on_forever():
    basic.show_icon(IconNames.HAPPY)
    doSomething()
    a()
    basic.pause(randint(1, 10000))
    basic.show_icon(IconNames.SAD)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
basic.forever(on_forever)
