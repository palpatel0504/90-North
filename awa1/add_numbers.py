import json

def lambda_handler(event, context):
    try:
        num1 = event.get("num1")
        num2 = event.get("num2")

        if num1 is None or num2 is None:
            return {
                "statusCode": 400,
                "body": json.dumps("Error: Please provide both num1 and num2")
            }

        result = num1 + num2
        return {
            "statusCode": 200,
            "body": json.dumps({"result": result})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error: {str(e)}")
        }
