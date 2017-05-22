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
            delay (int): the delay in milliseconds between two steps
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
            delay (int): the delay in milliseconds between two steps
            duration (int): for how long (in milliseconds) the method will run
            var_delay (bool): if True it will overwrite the delay for a new
                delay between 0 and the passed delay
        """
        #TODO complete
        until = pyb.millis()+duration

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
        # Speed in miliseconds to complete a full cycle
        until = pyb.millis()+duration

        # A full scroll involves 2 lights so delay = speed/4
        delay = int(speed/2)

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
        # Speed in miliseconds to complete a full cycle
        until = pyb.millis()+duration

        # A full scroll involves 4 lights so delay = speed/4
        delay = int(speed/4)

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
        # Speed in miliseconds to complete a full cycle
        until = pyb.millis()+duration

        # A full bounce involves 4 lights so delay = speed/8
        delay = int(speed/4)

        while(pyb.millis() < until):
            # For simplicity we duplicate the led list
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
        # Speed in miliseconds to complete a full cycle
        until = pyb.millis()+duration

        # A full bounce involves 8 lights so delay = speed/8
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
        # Speed in miliseconds to complete a full cycle
        until = pyb.millis()+duration

        # Fade = 0 is normal scroll

        # A full scroll involves 4 lights so delay = speed/4
        delay = int(speed/4)

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
        # Speed in miliseconds to complete a full cycle
        until = pyb.millis()+duration

        # Fade = 0 is normal scroll

        # A full scroll involves 4 lights so delay = speed/4
        delay = int(speed/8)

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
        Turn on the specified LED by increasing the light until the maximum
        brightness.

        Args:
            delay (int): the delay in milliseconds between two steps
                minimum 500 to appreciate any effect
            duration (int): for how long (in milliseconds) the method will run
        """
        until = pyb.millis()+duration

        while(pyb.millis() < until):
            t_step = delay / 255
            
            for intensity in range(0,255):
                if blue:
                    self.__led_blue.intensity(intensity)
                if orange:
                    self.__led_orange.intensity(intensity)
                intensity = intensity+1

                pyb.delay(int(round(t_step)))

            self.all_off()

        self.all_off()

    def swing(self, delay, duration, r2l=False):
        """
        Turn on the orange LED by increasing the light until the maximum
        brightness while decreasing the blue.

        Args:
            delay (int): the delay in milliseconds between two steps
                minimum 500 to appreciate any effect
            duration (int): for how long (in milliseconds) the method will run
        """
        until = pyb.millis()+duration

        while(pyb.millis() < until):
            t_step = delay / (255 * 2)
            
            if r2l:
                for intensity in range(0,255):
                    self.__led_orange.intensity(255-intensity)
                    self.__led_blue.intensity(intensity)
                    pyb.delay(int(round(t_step)))

                for intensity in range(0,255):
                    self.__led_orange.intensity(intensity)
                    self.__led_blue.intensity(255-intensity)
                    pyb.delay(int(round(t_step)))
            else:
                for intensity in range(0,255):
                    self.__led_orange.intensity(intensity)
                    self.__led_blue.intensity(255-intensity)
                    pyb.delay(int(round(t_step)))

                for intensity in range(0,255):
                    self.__led_orange.intensity(255-intensity)
                    self.__led_blue.intensity(intensity)
                    pyb.delay(int(round(t_step)))

        self.all_off()

    def heart_beat(self, delay, duration):
        """
        Simulate a heartbeat. 
        
        It is consider that a heartbeat consist on four timely equal parts:
        flat zero wave, increasing peak to 60% of the intensity, increasing to
        100% of the intensity and down to zero.

              /\
           /\/  \
        __/      \__

        Args:
            delay (int): the delay in milliseconds between two steps
            duration (int): for how long (in milliseconds) the method will run
            random_delay (bool): if True it will overwrite the delay for a new
                delay between 0 and the passed delay
        """
        until = pyb.millis()+duration
        t_quarter = int(round(delay/4))

        while(pyb.millis() < until):
            pyb.delay(round(delay/4))

            for intensity in range(0, 150):
                self.__led_blue.intensity(intensity)
                pyb.delay(round(150/(delay/8)))
            
            # Decrease from 150 to 30
            for intensity in range(0,120):
                self.__led_blue.intensity(150-intensity)
                pyb.delay(round(120/(delay/16)))

            # Increase from 30 to 255
            for intensity in range(30,255):
                self.__led_blue.intensity(intensity)
                pyb.delay(round(225/(delay/8)))

            # Decrease from 255 to 0
            for intensity in range(0,255):
                self.__led_blue.intensity(255-intensity)
                pyb.delay(round(255/(delay/12)))

            pyb.delay(round(delay/4))

        self.all_off()



if __name__ == '__main__':
    bl = BeautifulLights()
