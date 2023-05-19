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

- `pyhton3 -m venv venv`
- `source ./venv/bin/activate`
 
**For new environment:**

- `env | grep ENV`
- `pip install jedi`
- `pip install pylint`

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
  <a href="https://skillicons.dev" style="text-align: center;"><img src="https://github.com/aquasecurity/cloudsec-icons/blob/main/src/Images_Aqua.svg" alt="Docker Icon" width="50" height="50" /></a>
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

 <img src="https://github.com/aquasecurity/cloudsec-icons/blob/main/src/Kubernetes_Aqua.svg" alt="Kubernate Icon" width="50" height="50"/>

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
 <p align="center">
    <img src="https://github.com/Opengundumstyle/Audio-Alchemist/blob/main/spec.png" width="400" height="300">
  </p>
  
Proceed to  - **spec(DeploymentSpec):**
      <p align="center">
         <img src="https://github.com/Opengundumstyle/Audio-Alchemist/blob/main/dynamicspc.png" width="400" height="350">
      </p>
    
  #### See how the shape of the structure is matched :point_down:
    
   
                                             apiVersion: apps/v1
                                                kind: Deployment
                                                metadata:
                                                  name: auth
                                                  labels:
                                                    app: auth
                                                spec:
                                                  replicas: 2
                                                  selector:
                                                    matchLabels:
                                                      app: auth
                                                  strategy:
                                                    type: RollingUpdate
                                                    rollingUpdate:
                                                      maxSurge: 3
                                                  template:
                                                    metadata:
                                                      labels:
                                                        app: auth


    
  ### Why Kubernetes ?
Kubernetes eliminates many of the manual processes involved in deploying and scaling containerized applications.For example, if we can configure a service to have four pods, kubernetes will keep track of how many pods are running and if any of the pods goes down for any reason, kubernetes will automatically scale the deployment so that the number of Pods matches the configure amount. 

kubernetes also makes manually scaling pods more streamlined. For ex, say if there's a service that [load balancing](https://aws.amazon.com/what-is/load-balancing/) requests to individual pod using [Round-robin](https://en.wikipedia.org/wiki/Round-robin_scheduling), and that service is experiencing more traffic than the number of available pods can handle. As a result of this, we want to scale our service up from two to five pods. Without kubernetes,in a situation like this we'll likely need to go manually deploy each individual additional pod and then reconfigure the load balancer to include the new pods in the round-robin algorithm. But kubernete handles all of this for us, by running this one line of command `kubectl scale deployment --replicas=6 service `

in summary, with kubernetes we can cluster together a bunch of containerized services and easily orchestrate the deployment and management of these services using what we call kubernetes objects which are persisted entities in the kubernetes system.<br> 
 #### learn more about [kubernetes objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/)

  ### What is a Pod ?    
In Kubernetes, a Pod is the smallest and simplest unit of the platform. It represents a single instance of a running process within the cluster. A Pod encapsulates one or more containers, storage resources, and network settings that are tightly coupled and need to be co-located and co-scheduled. [Learn more](https://kubernetes.io/docs/concepts/workloads/pods/)

### Summary:
Bringing it all together, we can say that kubernetes clusters is comprised of a bunch of objects that we've configured (with the [yaml files](#custom_anchor_name) we mentioned earlier)that describe our cluster's intended state. From there kubernetes will continually compare the current status or state of those objects to the specification or desired state from our original configuration and if that comparison ever differs, kubernetes will automatically make adjustments to match the current status the original record of intent,which is acheived by the [kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/).
<hr/>

<div style="display: flex; flex-direction: row; align-items: center; justify-content: center;">
  <h3 style="text-align: center;">Gateway</h3>
  <img src="https://github.com/aquasecurity/cloudsec-icons/blob/main/src/Gateway_Aqua.svg" alt="jwt" width="50" height="50" />
</div>

#### MongoDB
connect mongo with gateway server:

      server  = Flask(__name__)
      server.config['MONGO_URI'] = 'mongodb://host.minikube.internal:27017/videos'
      mongo = PyMongo(server)
      
use [**Gridfs**](https://www.mongodb.com/docs/manual/core/gridfs/) to wrap mongoDB,so we can store and retreive files that exceedthe BSON-document size limit of 16MB 

``` fs = gridfs.GridFS(mongo.db) ```

#### RabbitMQ
create connection:

```
   connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
   channel = connection.channel()
```
<h5>how rabbitMQ works?</h5>
At its core, RabbitMQ acts as a mediator between various components of a distributed system, allowing them to send and receive messages in a reliable and asynchronous manner. It provides a flexible and scalable solution for building robust, decoupled systems by facilitating communication between different services or applications.<br><br>

**Intergration of rabbitMQ for this project:** 

 <p align="center">
    <img src="https://github.com/Opengundumstyle/Audio-Alchemist/blob/main/rabbitMQ.png" width="400" height="450">
  </p>

#### End Points
- log in
  `@server.route("/login",methods=["POST"])`
- upload
  `@server.route("/upload",method=["POST"])`
- download
  `@server.route("/download",methods=["GET"])`

## key Terms
### Synchronous & Asynchronous Interservice Communication
- #### Synchronous Interservice Communication

   Synchronous interservice communication refers to a communication pattern where services exchange information in a request-response manner, waiting for a response before proceeding. In this pattern, one service sends a request to another service and waits until it receives a response.

   Here are a few common approaches for achieving synchronous interservice communication:

   **HTTP Request-Response**: Services can communicate synchronously over HTTP using request-response protocols such as REST (Representational State Transfer) or GraphQL. One service sends an HTTP request to another service and waits for the corresponding response. This approach is widely used and supported by most programming languages and frameworks.

   **gRPC**: gRPC is a modern high-performance framework that enables synchronous communication between services using a binary protocol over HTTP/2. It allows you to define service interfaces and generate client and server code in various programming languages. gRPC provides strong typing, efficient serialization, and features like bidirectional streaming.

   **Messaging Queues with Request-Reply**: Messaging queues can also be used for synchronous communication. One service publishes a request message to a message queue, and the receiving service processes the request and sends back a response message to a designated reply queue. The requesting service waits for the response by consuming messages from the reply queue. RabbitMQ and Apache Kafka are popular messaging queue systems that can support this pattern.

   **Remote Procedure Call (RPC)**: RPC frameworks provide a way to invoke remote methods or functions on other services and wait for the result. This approach abstracts the communication details and allows you to work with remote services as if they were local. Examples of RPC frameworks include Apache Thrift, Apache Avro, and gRPC (mentioned earlier).

   When implementing synchronous interservice communication, consider the latency and potential failure scenarios that could impact the overall performance and reliability of your system. It's essential to design your services and choose appropriate technologies based on your specific requirements, scalability needs, and performance expectations. __One place we use such mechanism was with user login - our gateway service communicate with our auth service synchronously, so when we send a post request to auth serice from the gateway to retreive a jwt token,our gateway service is blocked until auth service return a jwt or error.__ Making those two services tightly coupled increases the system security. 
   
 - #### Asynchronous Interservice Communication
   Asynchronous interservice communication refers to a communication pattern where services exchange information without waiting for an immediate response. Instead of blocking and waiting for a response, the requesting service continues its execution and can handle other tasks. The response, when available, is typically sent to the requesting service through a callback mechanism or by publishing it to a message queue.

   Our approach for achieving asynchronous interservice communication is to use a 
   **Message Queue**: Services can communicate asynchronously using message queue systems such as RabbitMQ, Apache Kafka, or ActiveMQ. One service publishes a message to a specific queue or topic, and other services interested in that message consume it when they are ready. This decouples the sender and receiver, allowing them to operate independently.
   For our current architecture, out api gateway sends request to the converter service in the form of messages on the queue, but it doesn't need to wait for the response from the converter service. It essentially just sends and forget the service.  Same with the convertor serice and notification service.

### Strong Consistency & Eventual Consistency

**Strong Consistency:** In a system that enforces strong consistency, all replicas or nodes in the system will have the same consistent view of data at all times. Any read operation will return the most recent write or update, ensuring that clients always observe a globally agreed-upon state. Strong consistency provides linearizability, which means that the order of operations appears as if they happened one after another, even in a distributed system. Achieving strong consistency often requires coordination mechanisms like distributed locks or consensus protocols such as the Raft or Paxos algorithm. However, enforcing strong consistency can introduce increased latency and potential availability issues, especially in geographically distributed systems.

**Eventual Consistency:** In an eventually consistent system, there is a relaxation of the immediate consistency requirement. It allows replicas or nodes to have temporary inconsistencies and divergent views of data. However, over time, with the absence of further updates, all replicas will converge to the same consistent state. Eventual consistency prioritizes availability and performance over strict consistency. It is often achieved through replication techniques like asynchronous replication or gossip protocols, where updates are propagated asynchronously across the system. Eventual consistency is suitable for scenarios where real-time consistency is not critical, and conflicts or inconsistencies can be resolved later during synchronization or conflict resolution processes.

  
