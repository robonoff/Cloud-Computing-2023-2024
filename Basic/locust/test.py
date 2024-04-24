from locust import HttpUser, task
from requests.auth import HTTPBasicAuth
import requests
import random

USER_COUNT = 40

with open("output.txt", "a") as f:
    f.write(f"_________________________________________________\n")

class NextcloudUser(HttpUser):
    auth = None

    def on_start(self):
        self.users_index = random.choice(range(1, USER_COUNT))
        self.user = 'user' + '{:d}'.format(self.users_index)
        print(self.user)
        self.password = 'admin'
        self.auth = HTTPBasicAuth(self.user, self.password)
        self.verify_authentication()


    def verify_authentication(self):
        response = self.client.head("/remote.php/dav", auth=self.auth)
        if response.status_code != 200:
            with open("output.txt", "a") as f:
                f.write(f"Authentication failed for user {self.user}: {response.text}.\n")
            raise Exception(f"Authentication failed for user {self.user}")


     @task
     def propfind(self):
         try:
             response = self.client.request("PROPFIND", "/remote.php/dav", auth=self.auth)
             response.raise_for_status()
         except Exception as e:
            with open("output.txt", "a") as f:
                 f.write(f"Error during PROPFIND request: {e} for user {self.user}.\n")


    # @task
    # def upload_small(self):
    #     filename = "inej.jpg"
    #     with open( filename, 'rb') as f:
    #         response = self.client.put("/remote.php/dav/files/" + self.user + "/" + filename,
    #                                    auth=self.auth, data=f, name="/remote.php/dav/files/[user]/inej.jpg")

    #     if response.status_code != 201 and response.status_code != 204 :
    #         with open("output.txt", "a") as f:
    #             f.write(f"Error during PUT request: {response.status_code} for user {self.user}.\n")
    #         return

    #     for i in range(0,5):
    #         self.client.get("/remote.php/dav/files/" + self.user + "/" + filename,
    #                         auth=self.auth, name="/remote.php/dav/files/[user]/inej.jpg")

    #     self.client.delete("/remote.php/dav/files/" + self.user + "/" + filename,
    #                        auth=self.auth, name="/remote.php/dav/files/[user]/inej.jpg")




    # @task
    # def upload_medium(self):
    #     filename = "UnderstandingDeepLearning.pdf" 
    #     with open('/app/files/' + filename, 'rb') as f:
    #         response = self.client.put("/remote.php/dav/files/" + self.user + "/" + filename,
    #                                 auth=self.auth, data=f, name="/remote.php/dav/files/[user]/UnderstandingDeepLearning.pdf")

    #     if response.status_code != 201 and response.status_code != 204:
    #         with open("/mnt/locust/output.txt", "a") as f:
    #             f.write(f"Error during PUT request: {response.status_code} for user {self.user}.\n")
    #         return

    #     for i in range(0, 5):
    #         self.client.get("/remote.php/dav/files/" + self.user + "/" + filename,
    #                         auth=self.auth, name="/remote.php/dav/files/[user]/UnderstandingDeepLearning.pdf")

    #         self.client.delete("/remote.php/dav/files/" + self.user + "/" + filename,
    #                         auth=self.auth, name="/remote.php/dav/files/[user]/UnderstandingDeepLearning.pdf")




    @task
    def upload_large(self):
        filename = "largefile"
        with open('/app/files/' + filename, 'rb') as f:
            response = self.client.put("/remote.php/dav/files/" + self.user + "/" + filename,
                                       auth=self.auth, data=f, name="/remote.php/dav/files/[user]/largefile")

        if response.status_code not in (201, 204):
            with open("/mnt/locust/output.txt", "a") as f:
                f.write(f"Error during PUT request: {response.status_code} for user {self.user}.\n")
            return

        
        self.client.get("/remote.php/dav/files/" + self.user + "/" + filename,
                        auth=self.auth, name="/remote.php/dav/files/[user]/largefile")

        self.client.delete("/remote.php/dav/files/" + self.user + "/" + filename,
                        auth=self.auth, name="/remote.php/dav/files/[user]/largefile")

