import functions_framework
from flask import jsonify

@functions_framework.http
def greeting(request):
    """HTTP Cloud Function that returns a friendly greeting.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    return jsonify({"message": "Welcome to our service! Have a great day!"}) 