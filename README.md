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

  1. create manifests folder 
  
  2. add some yaml files ... In this project there are four and are commonly used in the context of deploying applications in a Kubernetes cluster: `auth-deploy.yaml` , `configmap.yaml` , `secret.yaml` and  `service.yaml`

  3. run minikube (deploy auth service to clusters) - command `minikube start` 
 
  4. run `k9s` to view minikube Pods(hit 0)

  
  ![minikube Pods](https://github.com/Opengundumstyle/Audio-Alchemist/blob/main/python/src/auth/minikubepods.png)<br>

  5. last but not least run  `kubectl apply -f ./` so we can apply all the Kubernetes resource configurations found in the current directory.<br>
  
 ### what is yaml ? 
YAML (YAML Ain't Markup Language) is a human-readable data serialization format commonly used for configuration files. YAML files use a plain-text syntax that is easy for  both humans and machines to read and write. In my understanding, they are the private and public environment variables that support the clusters
  
 #### how to write them <img width="25" height="25" src="https://img.icons8.com/fluency/48/hand-with-pen.png" alt="hand-with-pen"/>
  first, we start with the require fields: 
  
  - **apiVersion** - Which version of the Kubernetes API you're using to create this object
  
  - **kind** - What kind of object you want to create
  
  - **metadata** - Data that helps uniquely identify the object, including a name string, UID, and optional namespace

  - **spec** - What state you desire for the object
  
  then, we want to configure the spec for specific types of object with [Kubernetes API Reference](https://kubernetes.io/docs/reference/kubernetes-api/)
  
  from here, we have the freedom to use different set ups base on the kind of object. let's say we want to configure deployment, then we should go to **Workload Resources** -> **Deployment**. There we will see all the fields option within the metadata and spec
  
  ### Why Kubernetes ?
Kubernetes eliminates many of the manual processes involved in deploying and scaling containerized applications.For example, if we can configure a service to have four pods, kubernetes will keep track of how many pods are running and if any of the pods goes down for any reason, kubernetes will automatically scale the deployment so that the number of Pods matches the configure amount. 

kubernetes also makes manually scaling pods more streamlined. For ex, say if there's a service that [load balancing](https://aws.amazon.com/what-is/load-balancing/) requests to individual pod using [Round-robin](https://en.wikipedia.org/wiki/Round-robin_scheduling), and that service is experiencing more traffic than the number of available pods can handle. As a result of this, we want to scale our service up from two to five pods. Without kubernetes,in a situation like this we'll likely need to go manually deploy each individual additional pod and then reconfigure the load balancer to include the new pods in the round-robin algorithm. But kubernete handles all of this for us, by running this one line of command `kubectl scale deployment --replicas=6 service `

in summary, with kubernetes we can cluster together a bunch of containerized services and easily orchestrate the deployment and management of these services using what we call kubernetes objects which are persisted entities in the kubernetes system.<br> 
 #### learn more about [kubernetes objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/)

  ### What is a Pod ?    
In Kubernetes, a Pod is the smallest and simplest unit of the platform. It represents a single instance of a running process within the cluster. A Pod encapsulates one or more containers, storage resources, and network settings that are tightly coupled and need to be co-located and co-scheduled. [Learn more](https://kubernetes.io/docs/concepts/workloads/pods/)

### Summary:
Bringing it all together, we can say that kubernetes clusters is comprised of a bunch of objects that we've configured (with the [yaml files](#custom_anchor_name) we mentioned earlier)that describe our cluster's intended state. From there kubernetes will continually compare the current status or state of those objects to the specification or desired state from our original configuration and if that comparison ever differs, kubernetes will automatically make adjustments to match the current status the original record of intent,which is acheived by the [kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/).
 
