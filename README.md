# weirdtext

Weirdtext is an application for encoding and decoding given text. 

# Deployment

To deploy application locally, `python` ([download from here](https://www.python.org/downloads/)) and `libpq` ([download from here](https://www.postgresql.org/download/)) will be needed.

First, install requirements by executing command:
```bash
pip install -r requirements.txt
```

Next, run application server:
```bash
python manage.py runserver
```

# API
Weirdtext application API is available on `Heroku` server: https://weirdtext-app.herokuapp.com/. It has 2 endpoints:
- https://weirdtext-app.herokuapp.com/v1/encode/ for text encoding
- https://weirdtext-app.herokuapp.com/v1/decode/ for text decoding

## Encoding

Endpoint https://weirdtext-app.herokuapp.com/v1/encode/ allows only POST requests. To encode text, make POST request on this endpoint with JSON file described below:
```json
{
  "text": "<your text>"
}
```
Place this JSON in request's body. In return, you will get this response:
```json
{
  "result": "<separator><encoded text><separator><sorted words of original text>"
}
```
Default `<separator>` is `\n-weird-\n`.

## Decoding

Endpoint https://weirdtext-app.herokuapp.com/v1/encode/ allows only POST requests. To encode text, make POST request on this endpoint with JSON file described below:
```json
{
  "text": "<encoded text>"
}
```
**Your \<encoded text\> must be in correct format - the same as endpoint /v1/encode/ returns, with correct separator and string of sorted original words.**

Place this JSON in request's body. In return, you will get decoded text in following format:
```json
{
  "result": "<decoded text>"
}
```

