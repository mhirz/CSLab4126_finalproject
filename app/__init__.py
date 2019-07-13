from config import Config
from app import routes, models
from app.models import graph
from app.routes import app


app.config.from_object(Config)

#graph.schema.create_uniqueness_constraint("User", "email")
#graph.schema.create_uniqueness_constraint("Request", "id")
####graph.schema.create_uniqueness_constraint("Post", "id")




