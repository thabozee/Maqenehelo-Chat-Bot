from src.model.connection.redis import RedisWrapper


class ChatbotRedisHandler:
    def __init__(self):
        self.redis_wrapper = RedisWrapper()

    def set_user_state(self, user_id, state):
        self.redis_wrapper.set(f"user:{user_id}:state", state)
        print(f"user:{user_id}:state")

    def get_user_state(self, user_id):
        return self.redis_wrapper.get(f"user:{user_id}:state")

    def set_deceased_status(self, user_id, status):
        self.redis_wrapper.set(f"user:{user_id}:deceased", status)

    def get_deceased_status(self, user_id):
        return self.redis_wrapper.get(f"user:{user_id}:deceased")

    def set_document_uploaded(self, user_id, uploaded):
        self.redis_wrapper.set(f"user:{user_id}:uploaded_documents", uploaded)

    def get_document_uploaded(self, user_id):
        return self.redis_wrapper.get(f"user:{user_id}:uploaded_documents")

    def upload_document(self, user_id, document_type, document):
        document_key = f"documents:{user_id}:{document_type}"
        self.redis_wrapper.set(document_key, document)

    def verify_document(self, user_id, document_id, status):
        verification_key = f"verification:{user_id}:{document_id}"
        self.redis_wrapper.set(verification_key, status)

    def get_document_verification_status(self, user_id, document_id):
        verification_key = f"verification:{user_id}:{document_id}"
        return self.redis_wrapper.get(verification_key)
