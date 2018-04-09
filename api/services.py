"""API services"""

import json
import logging
import traceback
from flask import Blueprint, request
from api import logging_conf

route = Blueprint('route', __name__)


@route.route("/foo", methods=['GET'])
@logging_conf.log_func()
def foo():
    """
    Service sumary.
    Sample call: /foo?id=XXX&id=YYY
    :param id: One or mnay id
    :return: Either the given id or an error code
    """
    try:
        my_id = request.args.getlist('id')
        logging.info(json.dumps({"api_service": {"service": "/foo", "input": str(my_id)}}))
        return json.dumps(f"foo {my_id} ")
    except:
        error = traceback.format_exc()
        logging.error(error)
        return json.dumps({"code": "400", "error": "Something went wrong"})


@route.route("/baar", methods=['POST'])
@logging_conf.log_func()
def baar():
    """
    Service sumary
    :param id: One or many ids in the request
    :return: Either the given id or an error code
    """
    try:
        my_ids = list(request.get_json().values())[0]
        logging.info(json.dumps({"api_service": {"service": "/baar", "input": str(my_ids)}}))
        return json.dumps({"baar" : str(my_ids)})
    except:
        error = traceback.format_exc()
        logging.error(error)
        return json.dumps({"code": "400", "error": "Something went wrong"})
