from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import logging
import auth

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/api/*":{"origin":"*"}})

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# Formatter for logger
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh = logging.FileHandler("Track.log")
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.info('=========================START=========================')

api.add_resource(auth.Signup, '/api/v1/sign-up')
api.add_resource(auth.Verify, '/api/v1/verify')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
