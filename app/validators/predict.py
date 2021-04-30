from typing import List
from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

class PredictInputs(Inputs):
    json = [JsonSchema(schema={
        "type": "object",
        "properties": {
            "text": {"type": "string"}
        },
        "required": ["text"]
    })]

def validate_predict(request) -> List[str]:
    inputs = PredictInputs(request)

    if inputs.validate(): return []
    else: return inputs.errors
