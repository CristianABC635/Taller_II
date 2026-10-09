from locust import HttpUser, task

class Tester(HttpUser):
    @task(4)
    def TestUsers(self):
        self.client.get("/api/users")
    @task(3)
    def TestEmails(self):
        self.client.get("/api/users/emails")
    @task(1)
    def TestEdad(self):
        self.client.get("/api/users/over-twenty")
    @task(2)
    def TestBulk(self):
        self.client.post("/api/users/bulk", json={
            "users": [
            {"name": "Test 1", "email": "user1@test.com", "birth_date": "2001-01-01", "password": "password"},
            {"name": "Test 2", "email": "user2@test.com", "birth_date": "2002-02-02", "password": "password"},
            {"name": "Test 3", "email": "user3@test.com", "birth_date": "2003-03-03", "password": "password"},
            ]
        })
