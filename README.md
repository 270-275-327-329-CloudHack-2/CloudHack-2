<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />


  <h3 align="center">Building Microservice Communication With RabbitMQ</h3>

  



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#code structure">Folder Structure</a></li>
      </ul>
    </li>
    <li>
       <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
       </ul>
       <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
   
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



The microservice architecture is one of the most popular forms of deployment, especially in larger organisations where there are multiple components that can be loosely coupled together. Not only does this make it easier to work on separate components independently, but ensures that issues in one component does not bring down the rest of the service. A microservices architecture consists of a collection of small, autonomous services where each service is self-contained and should implement a single business capability within a bounded context. This also comes with the advantage that a single system can scale thereby limiting the resources to required components. For example, during a shopping sale, the cart and payment microservices might need more resources than the login microservice. However, one of the issues that comes up with microservices is inter-service communication. There is a need to send messages asynchronously and reliably across services, such that they’re delivered even in case of network delays or one of the services failing to receive it immediately. For this reason, we use messaging queues. A message queue is a form of asynchronous service-to-service communication used in serverless and microservices architectures. Messages are stored on the queue until they are processed and deleted. Each message is processed only once, by a single consumer.
### Built With

* [Python](https://python.com)
* [RabbitMQ]
* [Flask]
* [Mongo]

## Folder structure
/*root<br/>
      &emsp;&emsp;|<br/>
     &emsp;&emsp;|---app/<br/>
            &emsp;&emsp;&emsp;&emsp;|---database_consumer.py<br/>
            &emsp;&emsp;&emsp;&emsp;|---docker-compose.yaml<br/>
			&emsp;&emsp;&emsp;&emsp;|---Dockerfile_database<br/>
            &emsp;&emsp;&emsp;&emsp;|---Dockerfile_producer<br/>
			&emsp;&emsp;&emsp;&emsp;|---Dockerfile_ride_matching<br/>
            &emsp;&emsp;&emsp;&emsp;|---producer.py<br/>
			&emsp;&emsp;&emsp;&emsp;|---ride_matching_consumer.py<br/>

      
 





### Prerequisites


  ```sh
  docker-compose up
  ```





<!-- GETTING STARTED -->
## Getting Started
Setup rabbitmq server first
```sh
  docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
  ```

Run /app/producer.py to setup flask app
```sh
  python3 producer.py
  ```
Run docker-compose up
```sh
  docker-compose up
  ```
Send post request to /new_ride
```sh
  curl -X POST -d "location=pesuniversity&destination=krm&time=12&seats=3&cost=300" localhost:54321/new_ride

  ```



<!-- ROADMAP -->

            



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - O P Joy Jefferson - joy.jefferson10@gmail.com

Project Link: TBU



<!-- ACKNOWLEDGEMENTS -->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->



