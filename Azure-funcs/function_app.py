import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        num1 = req_body.get('num1')
        num2 = req_body.get('num2')

        if num1 is None or num2 is None:
            raise ValueError("Missing one of the numbers")

        result = num1 + num2

        return func.HttpResponse(
            json.dumps({"result": result}),
            status_code=200,
            mimetype="application/json"
        )

    except ValueError as e:
        return func.HttpResponse(
            str(e),
            status_code=400
        )

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(
            "An error occurred",
            status_code=500
        )
