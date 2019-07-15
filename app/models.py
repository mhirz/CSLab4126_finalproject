from py2neo import Graph, Node, Relationship
from py2neo.ogm import *
from passlib.hash import bcrypt
from datetime import datetime
#from app import app
import os
import uuid
import bcrypt

# Dave bitte implementiern.
#url = os.environ.get('GRAPHENEDB_URL', 'http://40.68.34.104:7687')
#username = os.environ.get('NEO4J_USERNAME')
#password = os.environ.get('NEO4J_PASSWORD')

graph = Graph("bolt://" + "213.199.133.252" + ":7687", auth=("neo4j", "!Markus_Dave!"))
# graph = Graph(app.config['DB_IP_BOLT'], auth=("neo4j", "!Markus_Dave!"))
# graph = Graph(url + '/db/data/', username=username, password=password)
# delete following line
#graph = Graph()

class User(GraphObject):
    __primarykey__ = "email"

    firstname = Property()
    lastname = Property()
    email = Property()
    password = Property()

    requests = RelatedTo("Request")
    offers = RelatedTo("Request")
    
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password


    def find(self):
        # user = graph.find_one("User", "email", self.email) - old
        user = User.match(graph, self.email).first()
        return user

    def find_by_email(email):
        # user = graph.find_one("User", "email", self.email) - old
        user = User.match(graph, email).first()
        return user


    def set_password(self, password):
        self.password = bcrypt.encrypt(password)
        return self


    def register(self):
        if not self.find():
            # user = User("User", #before a Node was created ogm uses the class itself
            #             firstname=self.firstname,
            #             lastname=self.lastname,
            #             email=self.email,
            #             password=self.password)

            graph.push(self)
            return True
        else:
            return False


    def verify_password(self, plainpw):
        user = self.find()
        if user:
            return bcrypt.checkpw(plainpw.encode('utf-8'), user.password)
        else:
            return False


    def add_offer(self, title, text): # deactivated whiile in development payment tags,
        import uuid

        user = self.find()
        offer = Request(title, text, user)

        user.offers.add(offer)
        graph.push(user)

    #TODO
        # tags = [x.strip() for x in tags.lower().split(' ')]
        # for t in tags:
        #     # if label is not found it is created
        #     tag = graph.merge_one("Tag", "name", t)
        #     rel = Relationship(tag, "T TAGGED", offer)
        #     graph.create(rel)


    def add_request(self, title, text): # deactivated whiile in development payment tags,
        import uuid

        user = self.find()
        request = Request(title, text, user)

        user.requests.add(request)
        graph.push(user)

    #TODO
        # tags = [x.strip() for x in tags.lower().split(' ')]
        # for t in tags:
        #     tag = graph.merge_one("Tag", "name", t)
        #     rel = Relationship(tag, "T TAGGED", request)
        #     graph.create(rel)
            


class Request(GraphObject):
    __primarykey__ = "slug"

    name = Property()
    text = Property()
    slug = Property() # = creatingUser# + name | Num of created requests

    offering = RelatedFrom(User)
    requesting = RelatedFrom(User)

    def __init__(self, name, text, creatingUser):
        self.name = name
        self.text = text
        self.slug = creatingUser.email + "_" + name

    def get_all_offers():
        offers = graph.run("MATCH (u:User)-[:OFFERS]->(r:Request) RETURN r, u")
        results_list = []

        for record in offers:
            record_dir = {"title": record["r"]["name"],
                            "text": record["r"]["text"],
                            "tag": "#tester"}
            results_list.append(record_dir)
            
        return results_list

    def get_all_requests():
        requests = graph.run("MATCH (u:User)-[:REQUESTS]->(r:Request) RETURN r, u")
        results_list = []

        for record in requests:
            record_dir = {"title": record["r"]["name"],
                            "text": record["r"]["text"],
                            "tag": "#tester"}
            results_list.append(record_dir)

        return results_list