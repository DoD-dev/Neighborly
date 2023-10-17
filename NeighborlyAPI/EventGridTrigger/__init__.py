import json
import logging

import azure.functions as func

def main(event: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')
