"""Server execution"""

from api import create_app
from api.services import route
from api import logging_conf


# Setting up logging through logging conf file
logging_conf.setup_logging("api/logging_properties.yml")

# Creating app
app = create_app(__name__)

# Attaching services to the app
app.register_blueprint(route)

# Running app
app.run(host="0.0.0.0")
