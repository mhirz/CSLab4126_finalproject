from py2neo import Graph, Node, Relationship
from passlib.hash import bcrypt
from datetime import datetime
import os
import uuid

# Dave bitte implementiern.
#url = os.environ.get('GRAPHENEDB_URL', 'http://40.68.34.104:7687')
#username = os.environ.get('NEO4J_USERNAME')
#password = os.environ.get('NEO4J_PASSWORD')

graph = Graph("bolt://13.80.109.161:7687", auth=("neo4j", "!Markus_Dave!"))
#graph = Graph(url + '/db/data/', username=username, password=password)
# delete following line
#graph = Graph()

class User:
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password


    def find(self):
        user = graph.find_one("User", "email", self.email)
        return user


    def set_password(self, password):
        self.password = bcrypt.encrypt(password)
        return self


    def register(self):
        if not self.find():
            user = Node("User",
                        firstname=self.firstname,
                        lastname=self.lastname,
                        email=self.email,
                        password=self.password)

            graph.create(user)
            return True
        else:
            return False


    def verify_password(self, password):
        user = self.find()
        if user:
            return bcrypt.verify(password, user['password'])
        else:
            return False


    def add_offer(self, title, tags, text, payment):
        import uuid

        user = self.find()
        offer = Node(
            "offer",
            id=str(uuid.uuid4()),
            title=title,
            text=text,
            tag=tags,
            payment=payment,
            timestamp=timestamp(),
            date=date()
        )
        rel = Relationship(user, "CREATED", offer)
        graph.create(rel)

        tags = [x.strip() for x in tags.lower().split(' ')]
        for t in tags:
            # if label is not found it is created
            tag = graph.merge_one("Tag", "name", t)
            rel = Relationship(tag, "T TAGGED", offer)
            graph.create(rel)


    def add_request(self, title, tags, text, payment):
        import uuid

        user = self.find()
        request = Node(
            "request",
            id=str(uuid.uuid4()),
            author=self.mail,
            title=title,
            text=text,
            tag=tags,
            payment=payment,
            timestamp=timestamp(),
            date=date()
        )
        rel = Relationship(user, "CREATED", request)
        graph.create(rel)

        tags = [x.strip() for x in tags.lower().split(' ')]
        for t in tags:
            tag = graph.merge_one("Tag", "name", t)
            rel = Relationship(tag, "T TAGGED", request)
            graph.create(rel)


class Request:
    pass