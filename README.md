# Audio-Alchemist

## technology:
- python
- mysql
- Kubernetes
- RabbitMQ
- MongoDB
- docker

## Setting up:
   in python environment folder under /auth:
    1.`source ./venv/bin/activate`,
    2. `env | grep VIRTUAL`,
    3. `pip install pylint`,
    4. `pip install --upgrade pip`,
    5. `pip install --upgrade pip` if needed

   ### useful commands <br><br>
   - `pip3 freeze > requirements.txt`:list of all the packages and their versions, allowing for easy replication of the environment in another location or by another user.
   - `docker build`:A fundamental command in Docker that allows you to create a reproducible image containing all the necessary dependencies and configurations for your application.
   - `docker tag`:create a new tag for an existing Docker image. Tags are used to give meaningful names to different versions or variations of an image.
   - `docker push`:This command is used to push a Docker image to a Docker repository, making it available for others to use or deploy.<br><br>Syntax: docker push [OPTIONS] NAME[:TAG] <br><br>
It uploads the specified image to the Docker repository. The image is identified by its name and optional tag.
Before pushing the image, ensure that you are authenticated with the Docker registry using docker login and have the necessary permissions to push to the repository.<br><br>
   - `docker pull`:
      This command is used to pull a Docker image from a Docker repository, downloading it to the local Docker host.<br><br>
Syntax: docker pull [OPTIONS] NAME[:TAG|@DIGEST]<br><br>
It fetches the specified image from the Docker repository and saves it locally on the Docker host.<br>
The image is identified by its name, optional tag, or digest.
If the tag is not specified, it defaults to the "latest" tag.
Before pulling the image, ensure that you have access to the Docker repository and are authenticated if necessary.<br><br>



## key components
<div style="display: flex; flex-direction: row; align-items: center; justify-content: center;">
  <h3 style="text-align: center;">Basic Authentication</h3>
  <img src="https://user-images.githubusercontent.com/5418178/177059352-fe91dcd5-e17b-4103-88ae-70d6d396cf85.png" alt="jwt" width="50" height="50" />
</div>

  #### client will receive jwt as login - A JWT consists of three parts: the header, the payload, and the signature. Each part is Base64Url encoded and concatenated with periods to form the complete JWT.

  Here's an example JWT:

   `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.  SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`
     <br>
      Let's break down each part:

   #### Header:

   `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`
   <br>
   This is the JSON object containing the algorithm used for signing the token (in this case, "HS256" which stands for HMAC-SHA256) and the token type ("JWT").

   #### Payload:

   `eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ`
    <br>
   This is the JSON object containing the claims or statements about the user. Claims can include user ID, name, expiration time, and any other custom data you want to include.

   #### Signature:

   `SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`
    <br>
   This is the signature created by combining the encoded header, encoded payload, and a secret key. The server can use the secret key to verify the integrity of the token and ensure it hasn't been tampered with.
 <hr>
<div style="display: flex; flex-direction: row; align-items: center; justify-content: center;">
  <h3 style="text-align: center;">docker image</h3>
  <a href="https://skillicons.dev" style="text-align: center;"><img src="https://skillicons.dev/icons?i=docker" alt="Docker Icon" /></a>
</div>

   #### this Dockerfile sets up a container environment with Python 3.10, installs system dependencies, copies the application code and requirements, and specifies the command to run the application. It provides a reproducible and isolated environment for running the Python application using Docker.
   ``` FROM python:3.10-slim-bullseye 
      RUN apt-get update \
      && apt-get install -y --no-install-recommends --no-install-suggests \
      build-essentials default-libmysqlclient-dev \
      && pip install --no-cache-dir --upgrade pip<br>
      
      WORKDIR /app
      COPY ./requirements.txt /app
      RUN pip install --no-cache-dir --requirement /app/requirements.txt
      COPY . /app
      EXPOSE 5000
     
      CMD [ "python3","server.py"]
   ```
   ##### side note: It is essential to consider that each instruction in a Dockerfile creates a separate image layer, leading to optimization through caching layers for buildtime within CI/CD pipeline. Learn more <ins>[here](https://docs.docker.com/build/cache/)</ins>
   
  <hr>
 <div style="display: flex; flex-direction: row; align-items: center; justify-content: center;">
  <h3 style="text-align: center;">Kubernetes Configuration</h3>
  <a href="https://skillicons.dev" style="text-align: center;"><img src="https://skillicons.dev/icons?i=kubernetes" alt="Kubernate Icon" /></a>
</div>
   
  
