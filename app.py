from flask import Flask

from chat.chat import chat_bp

app = Flask(__name__)
app.register_blueprint(chat_bp, url_prefix="/chat")

if __name__ == "__main__":
    app.run()
