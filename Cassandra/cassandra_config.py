from cassandra.cluster import Cluster

def get_cassandra_session():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('bouddhacass')
    return session