# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

quotes = {
    "Charles Dickens" : "Have a heart that never hardens, and a temper that never tires, and a touch that never hurts."
    "Confucius" : "The Superior Man is aware of Righteousness, the inferior man is aware of advantage."
    "Parker Palmer" : "America's freedom of religion, and freedom from religion, offers every wisdom tradition an opportunity to address our soul-deep needs: Christianity, Judaism, Islam, Buddhism, Hinduism, secular humanism, agnosticism and atheism among others.",
    "George Orwell" : "Myths which are believed in tend to become true."
    "Carl Jung" : "In all chaos there is a cosmos, in all disorder a secret order."
    "George Washington" : "Be courteous to all, but intimate with few, and let those few be well tried before you give them your confidence."
    "Robert Fulghum" : "If you break your neck, if you have nothing to eat, if your house is on fire, then you got a problem. Everything else is inconvenience."
    "Eckhart Tolle" : "The past has no power to stop you from being present now. Only your grievance about the past can do that."
    "Marcus Aurelius" : "There is nothing happens to any person but what was in his power to go through with."
    "Oscar Wilde" : "The smallest act of kindness is worth more than the grandest intention."
    "Richard Bach" : "Every problem has a gift for you in its hands."
    "René Descartes" : "The greatest minds are capable of the greatest vices as well as of the greatest virtues."
    "Ralph Waldo Emerson" : "The world makes way for the man who knows where he is going."
    "W. Clement Stone" : "You are a product of your environment. So choose the environment that will best develop you toward your objective. Analyze your life in terms of its environment. Are the things around you helping you toward success - or are they holding you back?"
    "Confucius" : "The cautious seldom err."
    "Sigmund Freud" : "The most complicated achievements of thought are possible without the assistance of consciousness."       
}

class ActionAuthor(Action):

    def name(self) -> Text:
        return "utter_author_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        author = tracker.get_slot("author")
        quote = quotes.get(author)
        if quote is None:
            output = "Could not find the quote for {}".format(author)
        else:
            output = "The quote for {} is {}".format(author, quote)

        dispatcher.utter_message(text=output)

        return []
