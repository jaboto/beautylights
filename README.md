# beautylights
MicroPython LED library for PYBLITE v1.0

Speed and duration is available for every method. Some methods allow to set specific parameters like fading (by default always 1), static (by default false and which leaves the lights on until the whole cycle is completed), right to left (by default always left to rigth)...
## Random single
Light a random LED and turn it off before turning on any other.

Options available:
* Random delay: delay will vary between 0 and the passed delay

Example:

![Random single pattern](/imgs/random_single.gif)

## Random single
Light a random number of LEDs and turn them off before turning on any other.

Options available:
* Random delay: delay will vary between 0 and the passed delay

Example:

![Random multiple pattern](/imgs/random_multiple.gif)

## Explode
Light the LEDs from inside to the outside.

Example:

![Explode pattern](/imgs/explode.gif)

## Implode
Light the LEDs from the outside to the inside.

Example:

![Implode pattern](/imgs/implode.gif)

## Jump
Light the LEDs jumping to the furthest that hasn't been lighted yet.

Options available:
* Static
* Right to left

Examples:
* Normal

![Jump pattern](/imgs/jump.gif)

* Static

![Jump static pattern](/imgs/jump_static.gif)

