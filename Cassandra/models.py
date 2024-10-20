from django.db import models
from .cassandra_config import get_cassandra_session
import uuid
from datetime import datetime

# Create your models here.
class Article(models.Model):
    def __init__(self, titre, contenu, datepub):
      self.titre = titre
      self.contenu = contenu
      self.datepub = datepub
      
    def save(titre,contenu):
        session = get_cassandra_session()
        id = uuid.uuid4()
        datepub = datetime.now()
        query = """
        INSERT INTO articles (id,titre, contenu, date_publication)
        VALUES (%s, %s, %s, %s)
        """
        session.execute(query, (id,titre,contenu,datepub))
        
    def get_all():
        session = get_cassandra_session()
        query = "SELECT * FROM articles"
        rows = session.execute(query)
        return rows
      
    def delete(id):
      session = get_cassandra_session()
      query = "DELETE FROM articles WHERE id=%s"
      session.execute(query, (id,))
      
    def update(id):
      session = get_cassandra_session()
      query = "UPDATE articles SET titre=%s, contenu=%s WHERE id=%s"
      session.execute(query, (titre, contenu, id))