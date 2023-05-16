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


## key components
- ### basic authentication
 - client will receive jwt as login: 
      A JWT consists of three parts: the header, the payload, and the signature. Each part is Base64Url encoded and concatenated with periods to form the complete JWT.

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

- ### docker image
   <br>
   ```
FROM python:3.10-slim-bullseye <br>
   RUN apt-get update \<br>
   && apt-get install -y --no-install-recommends --no-install-suggests \<br>
   build-essentials default-libmysqlclient-dev \<br>
   && pip install --no-cache-dir --upgrade pip<br>
   <br>
   <br>
   WORKDIR /app<br>
   COPY ./requirements.txt /app<br>
   RUN pip install --no-cache-dir --requirement /app/requirements.txt<br>
   COPY . /app<br>
   EXPOSE 5000<br>
   <br><br>
   CMD [ "python3","server.py"]
