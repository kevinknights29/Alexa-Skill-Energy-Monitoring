# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # "Welcome, you can say Hello or Help. Which would you like to try?"
        speak_output = "Bienvenido al Monitor Energetico, puedes decir Hola, Cuanto Es Mi Consumo, Conocer Mas, o Ayuda. Cual te gustaria intentar?"

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # "You can say hello to me! How can I help?"
        speak_output = "Puedes decirme hola! Como puedo ayudarte?"

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # "Goodbye!"
        speak_output = "Hasta Luego!"

        return (
            handler_input.response_builder
            .speak(speak_output)
            .response
        )


class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        # "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        speech = "Hmm, No estoy segura. Puedes decir Hola o Ayuda. Cual te gustaria intentar?"
        # "I didn't catch that. What can I help you with?"
        reprompt = "No puede comprender lo que me pediste. En que puedo ayudarte?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        # "You just triggered " + intent_name + "."
        speak_output = f"Haz disparado {intent_name}."

        return (
            handler_input.response_builder
            .speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        # "Sorry, I had trouble doing what you asked. Please try again."
        speak_output = "Disculpa, Tuve problemas al realizar lo que me pediste. Por favor, intentalo de nuevo."

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


# Custom Intents
class HolaMundoIntentHandler(AbstractRequestHandler):
    """Handler for Hola Mundo Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HolaMundoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hola estimado usuario!"

        return (
            handler_input.response_builder
            .speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )


class ConocerMasIntentHandler(AbstractRequestHandler):
    """Handler for Conocer Mas Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ConocerMasIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Este skill fue desarrollado para el proyecto empresarial del grupo dos para la asignatura de ingeniera de proyectos. Su proposito es brindar detalles sobre el consumo energetico y posibles recomendaciones para reducir el mismo. Esto le permitira al usuario identificar patrones de consumo de energia y crear reglas para optimizar su consumo. Deseas probar alguna funcionalidad?"
        ask_output = "Deseas probar alguna funcionalidad?"

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(ask_output)
            .response
        )


class CuantoConsumoIntentHandler(AbstractRequestHandler):
    """Handler for Cuanto Consumo Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CuantoConsumoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Tu consumo energetico es de 4,15 Watts hora, este consumo proviene de 3 dispositivos de iluminacion. Deseas conocer alguna recomendacion para optimizar tu consumo energetico?"
        ask_output = "Deseas conocer alguna recomendacion para optimizar tu consumo energetico?"

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(ask_output)
            .response
        )


class RecomendacionConsumoIntentHandler(AbstractRequestHandler):
    """Handler for Recomendacion Consumo Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RecomendacionConsumoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "De acuerdo a tu consumo energetico, puedes establecer reglas para delimitar el uso de las luces o toma corrientes. Tu uso promedio es de 6 horas y puede ser reducido con la creacion de reglas. Deseas conocer algo mas sobre tu consumo energetico?"
        ask_output = "Deseas conocer algo mas sobre tu consumo energetico?"

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(ask_output)
            .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
# Custom Intents
sb.add_request_handler(HolaMundoIntentHandler())
sb.add_request_handler(ConocerMasIntentHandler())
sb.add_request_handler(CuantoConsumoIntentHandler())
sb.add_request_handler(RecomendacionConsumoIntentHandler())
# make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
sb.add_request_handler(IntentReflectorHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
