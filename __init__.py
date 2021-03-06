# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import RPi.GPIO as GPIO

# GPIO-Pins festlegen

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


class GPIOSkill(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.learning = True

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')

    @intent_handler(IntentBuilder('LichtAn').require('LichtAnKeyword'))
    def handle_licht_an_intent(self, message):
        GPIO.output(17,True)
        GPIO.output(27,True)
        GPIO.output(22,True)
        self.speak_dialog("LichtAn")

    @intent_handler(IntentBuilder('LichtAus').require('LichtAusKeyword'))
    def handle_licht_aus_intent(self, message):
        GPIO.output(17,False)
        GPIO.output(27,False)
        GPIO.output(22,False)
        self.speak_dialog("LichtAus")

    @intent_handler(IntentBuilder('gruenesLichtAn').require('gruenesLichtAnKeyword'))
    def handle_gruenes_Licht_an_intent(self, message):
        GPIO.output(17,True)
        self.speak_dialog("gruenesLichtAn")

    @intent_handler(IntentBuilder('gruenesLichtAus').require('gruenesLichtAusKeyword'))
    def handle_gruenes_Licht_aus_intent(self, message):
        GPIO.output(17,False)
        self.speak_dialog("gruenesLichtAus")

    @intent_handler(IntentBuilder('blauesLichtAn').require('blauesLichtAnKeyword'))
    def handle_blaues_Licht_an_intent(self, message):
        GPIO.output(22,True)
        self.speak_dialog("blauesLichtAn")

    @intent_handler(IntentBuilder('blauesLichtAus').require('blauesLichtAusKeyword'))
    def handle_blaues_Licht_aus_intent(self, message):
        GPIO.output(22,False)
        self.speak_dialog("blauesLichtAus")

    @intent_handler(IntentBuilder('orangesLichtAn').require('orangesLichtAnKeyword'))
    def handle_oranges_Licht_an_intent(self, message):
        GPIO.output(27,True)
        self.speak_dialog("orangesLichtAn")

    @intent_handler(IntentBuilder('orangesLichtAus').require('orangesLichtAusKeyword'))
    def handle_oranges_Licht_aus_intent(self, message):
        GPIO.output(27,False)
        self.speak_dialog("orangesLichtAus")

    def stop(self):
        pass

    

def create_skill():
    return GPIOSkill()
