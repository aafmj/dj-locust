import time, random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(2)
    def fast(self):
        self.client.get("/fast")

    @task
    def slow(self):
        self.client.get("/slow")

    @task(3)
    def view_items(self):
        random_int = random.randint(0, 4)
        self.client.get("/get_item/"+str(random_int), name="/item")
        time.sleep(1)
