from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests

__author__ = 'tjoen'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)

class NumberSkillSkill(MycroftSkill):
    def __init__(self):
        super(NumberSkillSkill, self).__init__("NumberSkillSkill")

    def initialize(self):


	number_intent = IntentBuilder("NumberIntent").\
            require("NumberKeyword").optionally("numbers").optionally("Numbers").build()
        self.register_intent(number_intent, self.handle_number_intent)



   # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.
    def handle_number_intent(self, message):
    
        nrs = message.data.get("Numbers")
        LOGGER.debug("The message data is: {}".format(message.data))
        url = "http://numbersapi.com/"+nrs;
        #headers = {'Accept': 'text/plain'}
        r = requests.get(url)
        fact = r.content
        self.speak( fact )

    def stop(self):
        pass


def create_skill():
    return NumberSkillSkill()
