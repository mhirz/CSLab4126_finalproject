from config import Config
from app import models
from app import routes
from app.models import graph
from app.routes import app


app.config.from_object(Config)
app.config['DB_IP_BOLT'] = "bolt://" + "40.74.61.226" + ":7687"

#graph.schema.create_uniqueness_constraint("User", "email")
#graph.schema.create_uniqueness_constraint("Request", "id")
####graph.schema.create_uniqueness_constraint("Post", "id")




