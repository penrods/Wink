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

from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'spenrod'

LOGGER = getLogger(__name__)


class WinkSmartHomeSkill(MycroftSkill):

    def __init__(self):
        super(WinkSmartHomeSkill, self).__init__(name="WinkSmartHomeSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        turn_on_intent = IntentBuilder("TurnOnIntent").\
            require("TurnOnKeyword").build()
        self.register_intent(turn_on_intent, self.handle_turn_on_intent)

        turn_off_intent = IntentBuilder("TurnOffIntent").\
            require("TurnOffKeyword").build()
        self.register_intent(turn_off_intent,
                             self.handle_turn_off_intent)

    def handle_thank_you_intent(self, message):
        self.speak_dialog("turning.on")

    def handle_how_are_you_intent(self, message):
        self.speak_dialog("turning.off")

    def stop(self):
        pass


def create_skill():
    return WinkSmartHomeSkill()
