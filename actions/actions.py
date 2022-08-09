# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher


#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_more")

        return []


class ActionCheckAuthentication(Action):

    def name(self) -> Text:
        return "action_authentication"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(template="utter_more")
        if tracker.get_slot('code') != 1234:
            dispatcher.utter_message(template="utter_auth_fail")
            return []
        else:
            dispatcher.utter_message(template="utter_auth_success")
            return []


class ActionCheckDiagnosis(Action):

    def name(self) -> Text:
        return "action_diagnosis"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(template="utter_more")
        if tracker.get_slot('vital_sign') == "temperature":
            dispatcher.utter_message(template="utter_temperature")
            return []
        elif tracker.get_slot('vital_sign') == "heart":
            dispatcher.utter_message(template="utter_heart")
            return []
        elif tracker.get_slot('vital_sign') == "pressure":
            dispatcher.utter_message(template="utter_pressure")
            return []

        elif tracker.get_slot('vital_sign') == "respiration":
            dispatcher.utter_message(template="utter_respiration")
            return []

        else:
            dispatcher.utter_message(template="utter_none")
            return []
#
# class ValidateAuthenticationForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_authentication_form"
#
#     def validate_code(
#             self,
#             slot_value: Any,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]
#     ) -> Dict[Text, Any]:
#         """Validate `code` value."""
#
#         # dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
#         if tracker.get_slot('code') != 1234:
#             dispatcher.utter_message(text=f"We only accept 1234")
#             return {"code": None}
#         else:
#             dispatcher.utter_message(template="utter_submit", code=tracker.get_slot('code'))
#
#             return {"authFLag": True}
