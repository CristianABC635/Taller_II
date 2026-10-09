from locust import HttpUser, task

class Tester(HttpUser):
    @task(4)
    def TestUsers(self):
        self.client.get("api/users")
    @task(3)
    def TestEmails(self):
        self.client.get("api/users/emails")
    @task(1)
    def TestEdad(self):
        self.client.get("/users/over-twenty")
    @task(2)
    def TestBulk(self):
        self.client.post(json={
            "emails": ["test1@loadtest.local","test2@loadtest.local","test3@loadtest.local"]
        })
