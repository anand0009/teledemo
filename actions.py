# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from response_from_mysql import get_new_plan,get_user_plan


class CustomRasaAction(Action):

    def name(self) -> Text:
        return "action_new_plan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(get_new_plan())
        # dispatcher.utter_template('utter_your_num',tracker,number=details[str(tracker.get_slot('NAME')).lower()])
        return []
# action_your_plan
class ActionYourPlan(Action):

    def name(self) -> Text:
        return "action_your_plan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        my_plan =get_user_plan (tracker.get_slot('PHONE_NUMBER'))
        print("get_new_plan=", my_plan)

        dispatcher.utter_message(my_plan)
        return []
