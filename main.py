import os
import json
import logging
from flask import Flask, render_template, request, session, make_response, Response
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse


app = Flask(__name__)
app.secret_key = 'SECRET'
logging.basicConfig(level=logging.DEBUG, filename='main.log',
                    format='%(asctime)s %(levelname)-5s %(message)s')
log = logging.getLogger()


@app.route("/", methods=['POST'])
def home():
    log.info("going home!!")
    response = MessagingResponse()
    message = Message()
    message.body('Hello World!')
    response.append(message)
    return Response(response.to_xml(),
                    200, mimetype='application/xml')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 9830))
    app.run(host='0.0.0.0', port=port, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
