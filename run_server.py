from api import create_app
from api.services import route
from api import logging_conf


logging_conf.setup_logging("api/logging_properties.yml")
app = create_app(__name__)
app.register_blueprint(route)

app.run(host="0.0.0.0")
