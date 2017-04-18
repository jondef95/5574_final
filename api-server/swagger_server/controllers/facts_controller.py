import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from flask import jsonify
from flask_api import status
import fact_generator as FG

def get_fact_random():
    """
    Generates a random fact about a random subject
    

    :rtype: int
    """
    try:
        subject, facts = FG.get_fact_random()
    except:
        return jsonify(Error(502, "An internal error occurred while attempting to contact Wikipedia")), status.HTTP_502_BAD_GATEWAY
    response = {}
    if (subject is not "error"):
        response["subject"] = subject
        response["facts"] = facts
        code = status.HTTP_200_OK
    else:
        response["error"] = facts
        code = status.HTTP_404_NOT_FOUND
    return jsonify(response), code


def get_fact_subject(topic):
    """
    Generates a random fact about a particular topic
    
    :param topic: The topic that a fact should be related to
    :type topic: str

    :rtype: int
    """
    try:
        subject, facts = FG.get_fact_subject(topic)
    except:
        return jsonify(Error(502, "An internal error occurred while attempting to contact Wikipedia")), status.HTTP_502_BAD_GATEWAY
    response = {}
    if (subject is not "error"):
        response["subject"] = subject
        response["facts"] = facts
        code = status.HTTP_200_OK
    else:
        response["error"] = facts
        code = status.HTTP_404_NOT_FOUND
    return jsonify(response), code
