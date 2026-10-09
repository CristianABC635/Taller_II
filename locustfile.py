from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def homero(self):
        self.client.get("/api/users")