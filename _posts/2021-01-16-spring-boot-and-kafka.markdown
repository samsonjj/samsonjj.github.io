---
layout: post
title: Spring Boot and Kafka
---

Finally I've been able to run a local project with Spring Boot. My frustrations are really just with the documentation out there. There's nothing that explains the pieces that are required to get one of these things to start. It's really not that obvious. The key is to generate a project with Spring Initialzr (which is a good way to start any spring project), but make sure you include the Spring Web dependency, which includes a containerized tomcat server as a dependency. If you do this
wrong, you might not install any deployment server, or maybe tomcat will be listed in the pom.xml as a dependency, but as provided by the host (so it won't install and run automatically). Imo there are probably advantages to having this kind of architecture. It splits resposibility of components, and you can swap out server technologies easily (the idea of swapping at deploy time seems to be central to Java Spring). But why can't there be a decent tutorial out there explaining this
>:(. Ima just assume its because Java is, technically, old. Every old language is bound to have terrible documentation, from former years of piling garbage pages on the internet, and declining interest in creating modern documentation when there is already the old stuff out there. Plus, it doesn't help that Java has swapped hands over the years, and is now owned by Oracle <- :/. Documentation is as important as the language itself. If I can't find an officially supported straightforward tutorial I'm out. Out with the old,
in with the new!

Sprint Boot tutorial
https://www.youtube.com/watch?v=9SGDpanrc8U

Tutorial for event sourcing in Spring Boot (Kafka)
https://spring.io/blog/2019/10/15/simple-event-driven-microservices-with-spring-cloud-stream
