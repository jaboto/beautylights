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

## Scroll
Light the LEDs with a scrolling pattern starting always from the same point.

Options available:
* Static
* Right to left

Examples:
* Normal

![Scroll pattern](/imgs/scroll.gif)

* Static

![Scroll static pattern](/imgs/scroll_static.gif)

## Scroll Fade
Light the LEDs with a scrolling pattern starting always from the same point and leaving a light trace.

Options available:
* Fade (number of LEDs on for the trace). A 0 fade presents the same pattern as the normal scroll.
* Right to left

Examples:
* Fade 1 (by default):

![Scroll fade pattern](/imgs/scroll_fade1.gif)

* Fade 2:

![Scroll fade pattern](/imgs/scroll_fade2.gif)


## Sroll Knight
Light the LEDs with a scrolling pattern bouncing at each side in a Kinght Rider effect.

Options available:
* Fade (number of LEDs on for the trace). A 0 fade presents the same pattern as the bounce pattern.
* Right to left

Examples:
* Fade 1 (by default):

![Scroll knight pattern](/imgs/scroll_knight1.gif)

* Fade 2:

![Scroll knight pattern](/imgs/scroll_knight2.gif)


## Bounce
Light the LEDs with a scrolling pattern bouncing at each side.

Options available:
* Right to left

Example:

![Bounce pattern](/imgs/bounce.gif)

## Glow
Light any of the variable intensity LEDs (orange and/or blue) from 0 to the max intensity. The default LED is the blue for this effect.

Example:

![Glow pattern](/imgs/glow.gif)

## Swing
Light the variable intensity LEDs (orange and blue) from 0 to the max intensity and from the max intensity to 0 in a swing effect.

Options available:
* Right to left

Example:

![Swing pattern](/imgs/swing.gif)

## Heart Beat
Light the variable intensity LEDs (orange and/or blue) simulating a heart beat with two peaks per cycle. The default LED is the blue for this effect.


Example:

![Heart beat pattern](/imgs/heart.gif)
