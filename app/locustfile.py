from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_home_page(self):
        self.client.get("/")

    @task(2)  # The number indicates this task is twice as likely to be executed
    def add_player_page(self):
        self.client.get("/add_player")
