function a () {
    magicbit.MotorRun(magicbit.Motors.M1, randint(-1 * speed, speed))
    magicbit.MotorRun(magicbit.Motors.M2, randint(-1 * speed, speed))
    magicbit.MotorRun(magicbit.Motors.M3, randint(-1 * speed, speed))
    magicbit.MotorRun(magicbit.Motors.M4, randint(-1 * speed, speed))
}
function doSomething () {
    basic.showIcon(randint(0, 21))
}
let speed = 0
speed = 64
let icons = [
IconNames.Heart,
IconNames.Happy,
IconNames.Sad,
IconNames.Angry,
IconNames.Confused,
IconNames.Asleep,
IconNames.Surprised,
IconNames.Silly,
IconNames.Fabulous,
IconNames.Meh,
IconNames.Yes,
IconNames.No,
IconNames.Triangle,
IconNames.Square,
IconNames.Diamond,
IconNames.Chessboard,
IconNames.Duck,
IconNames.House,
IconNames.Tortoise,
IconNames.Butterfly,
IconNames.Ghost,
IconNames.Cow
]
basic.showIcon(IconNames.Heart)
magicbit.MotorRun(magicbit.Motors.M1, randint(-1 * speed, speed))
magicbit.MotorRun(magicbit.Motors.M2, randint(-1 * speed, speed))
magicbit.MotorRun(magicbit.Motors.M3, randint(-1 * speed, speed))
magicbit.MotorRun(magicbit.Motors.M4, randint(-1 * speed, speed))
basic.showIcon(IconNames.Ghost)
basic.forever(function () {
    basic.showIcon(IconNames.Happy)
    doSomething()
    a()
    basic.pause(randint(1, 10000))
    basic.showIcon(IconNames.Sad)
})
