import redis


class RedisWrapper:
    def __init__(self):
        connection_string = redis.Redis(host='localhost', port=6379, decode_responses=True)
        self.connection = connection_string

    def set(self, key, value):
        # Set key with default expiration of 24 hours
        self.connection.set(key, value, ex=86400)

    def get(self, key):
        return self.connection.get(key)

    def delete(self, key):
        self.connection.delete(key)



