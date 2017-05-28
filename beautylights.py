# -*- coding: utf-8 -*-
"""
BeautyLights, a LED control library for your PYBLITE board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BeautyLights is a Python library for your PYBLITE v1.0 board
which contains 4 LED (red, green, orange, blue) and runs
MicroPython (http://micropython.org).
"""

__title__ = 'BeautyLights'
__version__ = '0.9'
__author__ = 'Jaime Bosque Torrecilla'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2017 Jaime Bosque Torrecilla'

import pyb
import urandom

class BeautyLights(object):
    """
    BeautyLights is a library to control the ligths (LEDs) of your PYBLITE v1.0
    """

    def __init__(self):
        """
        Define the LEDs that will be used (4 for the PYBLITE v1.0)
        """
        self.__led_red = pyb.LED(1)
        self.__led_green = pyb.LED(2)
        self.__led_orange = pyb.LED(3)
        self.__led_blue = pyb.LED(4)
        self.__leds = [self.__led_red, self.__led_green, self.__led_orange,
                self.__led_blue]

    def all_off(self):
        """
        Turn all the LEDs off
        """
        for led in self.__leds:
            led.off()

    def all_on(self):
        """
        Turn all the LEDs on
        """
        for led in self.__leds:
            led.on()

    def random_single(self, delay, duration, random_delay=False):
        """
        Turn on and off a single LED randomly

        Args:
            delay (int): the delay in milliseconds between two LED being
            lighted
            duration (int): for how long (in milliseconds) the method will run
            random_delay (bool): if True it will overwrite the delay for a new
                delay between 0 and the passed delay
        """
        until = pyb.millis()+duration

        while(pyb.millis() < until):
            if (random_delay):
                delay = urandom.randint(0,delay)
            led = urandom.choice(self.__leds)
            led.on()
            pyb.delay(delay)
            led.off()
        self.all_off()
        
    def random_multiple(self, delay, duration, random_delay=False):
        """
        Turn on and off multiple LED randomly

        Args:
            delay (int): the delay in milliseconds between two cycles
            duration (int): for how long (in milliseconds) the method will run
            random_delay (bool): if True it will overwrite the delay for a new
                delay between 0 and the passed delay
        """
        until = pyb.millis()+duration

        while(pyb.millis() < until):
            if (random_delay):
                delay = urandom.randint(0,delay)
            led = urandom.choice(self.__leds)
            if urandom.randint(0,1) == 0:
                led.on()
            else:
                led.off()
            pyb.delay(delay)
        self.all_off()

    def explode(self, delay, duration):
        """
        Draw a pattern from the two inner LED towards the outside

        Args:
            delay (int): the delay in milliseconds between two cycles
            duration (int): for how long (in milliseconds) the method will run
        """
        until = pyb.millis()+duration
        
        # A full cycle has 3 steps so set delay accordingly
        delay = int(delay/3)

        while(pyb.millis() < until):
            self.__led_green.on()
            self.__led_orange.on()
            pyb.delay(delay)

            self.__led_green.off()
            self.__led_orange.off()
            self.__led_red.on()
            self.__led_blue.on()
            pyb.delay(delay)

            self.__led_red.off()
            self.__led_blue.off()
            pyb.delay(delay)

        self.all_off()

    def implode(self, speed, duration):
        """
        Draw a pattern from the two outside LED towards the outside

        Args:
            delay (int): the delay in milliseconds between two cycles
            duration (int): for how long (in milliseconds) the method will run
        """
        until = pyb.millis()+duration

        # A full cycle has 3 steps so set delay accordingly
        delay = int(delay/3)

        while(pyb.millis() < until):
            self.__led_red.on()
            self.__led_blue.on()
            pyb.delay(delay)

            self.__led_red.off()
            self.__led_blue.off()
            self.__led_green.on()
            self.__led_orange.on()
            pyb.delay(delay)

            self.__led_green.off()
            self.__led_orange.off()
            pyb.delay(delay)

        self.all_off()

    def scroll(self, speed, duration, static=False, r2l=False):
        """
        Draw a pattern from the two outside LED towards the outside

        Args:
            delay (int): the delay in milliseconds between two cycles
            duration (int): for how long (in milliseconds) the method will run
            static (bool): if enabled lights will remain on for the whole cycle
            r2l (bool): draw the pattern from right to left
        """
        until = pyb.millis()+duration

        # A full cycle has 5 steps so set delay accordingly
        delay = int(speed/5)

        while(pyb.millis() < until):
            leds = self.__leds[::-1] if r2l else self.__leds
            for led in leds:
                led.on()
                pyb.delay(delay)
                if not static:
                    led.off()
            self.all_off()
            pyb.delay(delay)

    def jump(self, speed, duration, static=False, r2l=False):
        """
        Draw a pattern jumping to the furthest that hasn't been  lighted yet.

        Args:
            delay (int): the delay in milliseconds between two cycles
            duration (int): for how long (in milliseconds) the method will run
            static (bool): if enabled lights will remain on for the whole cycle
            r2l (bool): draw the pattern from right to left
        """
        until = pyb.millis()+duration

        # A full cycle has 5 steps so set delay accordingly
        delay = int(speed/5)

        while(pyb.millis() < until):
            # For simplicity we duplicate the led list to operate
            #   popping and pushing
            jumping_leds = list(self.__leds)
            while(len(jumping_leds) > 0):
                led = jumping_leds.pop(0)
                led.on()
                pyb.delay(delay)
                if not static:
                    led.off()
                led = jumping_leds.pop()
                led.on()
                pyb.delay(delay)
                if not static:
                    led.off()
            self.all_off()
            pyb.delay(delay)

        self.all_off()

    def bounce(self, speed, duration, r2l=False):
        """
        Draw a pattern lighting from one to the other side simulating a bounce.

        Args:
            delay (int): the delay in milliseconds between two cycles
            duration (int): for how long (in milliseconds) the method will run
            r2l (bool): draw the pattern from right to left
        """
        until = pyb.millis()+duration

        # A full cycle has 8 steps so set delay accordingly
        delay = int(speed/8)

        while(pyb.millis() < until):
            for led in self.__leds:
                led.on()
                pyb.delay(delay)
                led.off()

            for led in reversed(self.__leds):
                led.on()
                pyb.delay(delay)
                led.off()

        self.all_off()

    def scroll_fade(self, speed, duration, fade=1, r2l=False):
        """
        Draw a pattern lighting from one to the other leaving a fade trace. A
        scroll equal to 0 has the same effect as using the scroll method.

        Args:
            delay (int): the delay in milliseconds between two cycles
            duration (int): for how long (in milliseconds) the method will run
            fade (int): how many lights are left on while scrolling. Default = 1
            r2l (bool): draw the pattern from right to left
        """
        until = pyb.millis()+duration

        # A full cycle has 5 steps so set delay accordingly
        delay = int(speed/5)

        while(pyb.millis() < until):
            steps = len(self.__leds)+fade
            for i in range(0,steps):
                index = 0 if (i - fade <= 0) else i - fade
                for led in self.__leds[index:i+1]:
                    led.on()
                pyb.delay(delay)
                self.all_off()

        self.all_off()

    def scroll_knigth(self, speed, duration, fade=1, r2l=False):
        """
        Draw a pattern lighting from one to the other leaving a fade trace and
        return. This effect simulates the knight rider effect. A scroll equal 
        to 0 has the same effect as using the bounce method.

        Args:
            delay (int): the delay in milliseconds between two cycles
            duration (int): for how long (in milliseconds) the method will run
            fade (int): how many lights are left on while scrolling (default
                        option)
            r2l (bool): draw the pattern from right to left
        """
        until = pyb.millis()+duration

        # A full cycle has 5 steps so set delay accordingly
        delay = int(speed/5)

        while(pyb.millis() < until):
            steps = len(self.__leds)+fade
            for i in range(0,steps):
                index = 0 if (i - fade <= 0) else i - fade
                for led in self.__leds[index:i+1]:
                    led.on()
                pyb.delay(delay)
                self.all_off()

            reversed_leds = self.__leds[::-1]
            for i in range(0,steps):
                index = 0 if (i - fade <= 0) else i - fade
                for led in reversed_leds[index:i+1]:
                    led.on()
                pyb.delay(delay)
                self.all_off()

        self.all_off()

    def glow(self, delay, duration, blue=True, orange=False):
        """
        Turn on any of the variable intensity LED by increasing the light from
        zero until the maximum brightness.

        Recommended a delay of minimum 500 to appreciate the effect.

        Args:
            delay (int): the delay in milliseconds between two cycles
            duration (int): for how long (in milliseconds) the method will run
            blue (bool): use the blue LED (default option) 
            orange (bool): use the organte LED
        """
        until = pyb.millis()+duration

        # A full cycle has 51 steps so set delay accordingly
        delay = int(delay/51)

        while(pyb.millis() < until):
            # From 0 to 255 with steps of 5 (0..51)
            for intensity in range(0,52):
                if blue:
                    self.__led_blue.intensity(intensity*5)
                if orange:
                    self.__led_orange.intensity(intensity*5)
                intensity = intensity+1

                pyb.delay(delay)

            self.all_off()

        self.all_off()

    def swing(self, delay, duration, r2l=False):
        """
        Turn on the orange LED by increasing the light until the maximum
        brightness while decreasing the blue and then the other way around.

        Recommended a delay of minimum 500 to appreciate the effect.

        Args:
            delay (int): the delay in milliseconds between two cycles
            duration (int): for how long (in milliseconds) the method will run
            r2l (bool): draw the pattern from right to left
        """
        until = pyb.millis()+duration

        # A full cycle has 102 steps so set delay accordingly
        delay = int(delay/102)

        while(pyb.millis() < until):
            if r2l:
                # From 0 to 255 with steps of 5 (0..51)
                for intensity in range(0,52):
                    self.__led_orange.intensity(255-intensity*5)
                    self.__led_blue.intensity(intensity*5)
                    pyb.delay(delay)

                # From 0 to 255 with steps of 5 (0..51)
                for intensity in range(0,52):
                    self.__led_orange.intensity(intensity*5)
                    self.__led_blue.intensity(255-intensity*5)
                    pyb.delay(delay)
            else:
                # From 0 to 255 with steps of 5 (0..51)
                for intensity in range(0,52):
                    self.__led_orange.intensity(intensity*5)
                    self.__led_blue.intensity(255-intensity*5)
                    pyb.delay(delay)

                # From 0 to 255 with steps of 5 (0..51)
                for intensity in range(0,52):
                    self.__led_orange.intensity(255-intensity*5)
                    self.__led_blue.intensity(intensity*5)
                    pyb.delay(delay)

        self.all_off()

    def heart_beat(self, delay, duration, blue=True, orange=False):
        """
        Turn on any of the variable intensity LED simulating a heart beat
        Simulate a heartbeat. 
        
        It is consider that a heartbeat consist on four timely unequal parts:
        flat zero wave (takes 1/6 of the time), increasing peak to 60% of the
        intensity (takes 1/8 of the time), reducing peak to 30% of the intesity
        (takes 1/16 of the time) increasing to 100% of the intensity (takes 
        1/12 of the time) and down to zero (takes 1/4 of the time) and a flat
        zero wave (takes 1/6 of the time)

              /\
           /\/  \
        __/      \__


        Recommended a delay of minimum 800 to appreciate the effect.

        Args:
            delay (int): the delay in milliseconds between two steps
            duration (int): for how long (in milliseconds) the method will run
            blue (bool): use the blue LED (default option) 
            orange (bool): use the organte LED
        """
        until = pyb.millis()+duration

        while(pyb.millis() < until):
            # Flat area that takes a quarter of the time
            pyb.delay(round(delay/6))

            # Increase from 0 to 150 (0..30 * 5)
            for intensity in range(0, 31):
                if blue:
                    self.__led_blue.intensity(intensity*5)
                if orange:
                    self.__led_orange.intensity(intensity*5)
                pyb.delay(round((delay/8)/30))
            
            # Decrease from 150 to 30 (0..24 * 5)
            for intensity in range(0,25):
                if blue:
                    self.__led_blue.intensity(150-intensity*5)
                if orange:
                    self.__led_orange.intensity(150-intensity*5)
                pyb.delay(round((delay/16)/24))

            # Increase from 30 to 255 (6..50 * 5)
            for intensity in range(6,52):
                if blue:
                    self.__led_blue.intensity(intensity*5)
                if orange:
                    self.__led_orange.intensity(intensity*5)
                pyb.delay(round((delay/12)/45))

            # Decrease from 255 to 0 (0..51 * 5)
            for intensity in range(0,52):
                if blue:
                    self.__led_blue.intensity(255-intensity*5)
                if orange:
                    self.__led_orange.intensity(255-intensity*5)
                pyb.delay(round((delay/4)/52))

            pyb.delay(round(delay/6))
            #self.all_off()

        self.all_off()

if __name__ == '__main__':
    bl = BeautifulLights()
