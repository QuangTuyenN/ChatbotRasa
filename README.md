This project use rasa framework to build chatbot

If you want to embedd your chatbot in messenger, get the token, pass of your facebook page and put it in credentials.yml

If you want to embedd the bot baloom in your website, set the code:

    <div id="rasa-chat-widget" data-websocket-url="http://yourIP:5005"></div>
    <script src="https://unpkg.com/@rasahq/rasa-chat" type="application/javascript"></script>

in your website

If you want to send a message to bot, using POST method to:
"http://yourIP:5005/webhooks/rest/webhook"


RUN rasa run --cors "*" to run bot in port 5005 (Or -p your_port)

RUN rasa run actions to run actions server in port 5055 (Or -p your_port)



