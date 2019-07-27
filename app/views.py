import json
from json import JSONDecodeError

from django.http import HttpResponse
from rest_framework.views import APIView

from app.decoder import Decoder, IncorrectInputException
from app.encoder import Encoder


class EncodeView(APIView):
    encoder = Encoder()

    def post(self, request):
        try:
            text = json.loads(request.body)["text"]
        except JSONDecodeError:
            return HttpResponse("Incorrect input format", status=400)
        result = self.encoder.create_encoded_response(text)
        return HttpResponse(json.dumps({"result": result}))


class DecodeView(APIView):
    decoder = Decoder()

    def post(self, request):
        try:
            text = json.loads(request.body)["text"]
            result = self.decoder.decode_text(text)
        except JSONDecodeError:
            return HttpResponse("Incorrect input format", status=400)
        except IncorrectInputException as error:
            return HttpResponse(error, status=400)
        return HttpResponse(json.dumps({"result": result}))
