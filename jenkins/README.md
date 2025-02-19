# Jenkins setup with docker

## Set up Jenkins Server
Setting up the Jenkins server is the most important part. The following command will download and install the Jenkins server and set it up automaticlly.

```bash
docker run --detach --volume jenkins_home:/var/jenkins_home --name jenkins-server --publish 8080:8080 --publish 50000:50000 --restart=on-failure jenkins/jenkins:lts-jdk17
```
| VALUE                                         | DESCRIPTION                                       |
| :--                                           | :--                                               |
| `--volume jenkins_home:/var/jenkins_home`     | Mounts docker volume to a path in the container   |
| `--name jenkins-server`                       | Gives the container the name `jenkins-server`     |
| `--publish 8080:8080` `--publish 50000:50000` | Opens port 8080 to access the server through the webbrowser [localhost:8080](http://localhost:8080) and port 50000 that the agents will use to communicate with the jenkins server. |
| `--restart=on-failure`                        | When/if the server runs into an error it will automaticlly restart, due to the volume mount no data will be lost |
| `jenkins/jenkins:lts-jdk17`                   | The LTS image the server will be using |

All you have to do is go to [localhost:8080](http://localhost:8080) in your webrowser and go throught the admin account setup which allows you to access the server and set up all plugins that you might want. Do as the installation wizard tells you.

Now you can run your pipelines and set up your CI/CD workflow. Althogh Jenkins do recommend you to have an agent set up for safety reason, what this most likely refere to is that incase a developer creates code that could shut down the agent it runs on it would turn off the entire server instead of just a seperate agent.

So how do you set up an agent?

## Set up Jenkins Client
``` bash
docker run -d --init jenkins/inbound-agent -url http://<IP-ADDRESS>:<PORT>/ <AGENT-SERCET> <AGENT-NAME>
```
|   VALUE           | DESCRIPTION                                                                                        |
|   :--             |    :--                                                                                             |
|`<IP-ADDRESS>`     | The actual IP address that your jenkins server is hosted on. (**NOT LOCALHOST**)                   |
|`<PORT>`           | The port you've hosted the jenkins server on. (default is 8080)                                    |
|`<AGENT-SECRET>`   | The agent secreat that is displayed on the jenkins server under `Dashboard > Nodes > <AGENT_NAME>` |
|`<AGENT-NAME>`     | The name you gave the agent in the jenkins server UI                                               |
> [!TIP] Why doesn't "localhost" work as an IP-address?
> Due to how virtualization works, when refering to "localhost" the system will refere to it's internal network. Which means that when you host a docker container you can reach it with localhost from your webbrowser becuse it acts as a router for your container, but your containers do not nessesarly know that the other ones exists.
>
> ***TL;DR:*** localhost referes to the machine itself, host and containers.

Remember that the agent secret and agent name needs to match, otherwise the agent will not connect correctly. The name of the container does not have to be the same as the angent but is recommended to keep it consistant.

Now you can create as many agents as you need, but before you start the them you need to regester them as new agents on the server.

### But what if I want to have specific libraries and files on the agent to run tests?
The great thing about docker is that you can build your own images on top of already exisitng images by making a `Dockerfile`.

To start creating a docker file you need to begin by creating the `Dockerfile` itself and use the base `jenkins/inbound-agent`.
``` Dockerfile
FROM jenkins/inbound-agent

COPY <source/path> <path/in/container>
```

This will take whatever directory in your system (relative to where the Dockerfile exists) and copies the directory into the container. When if you run `docker build -t <my-jenkins-agent> .` in the directory the file exist it will create a new docker image that you can call instead of `jenkins/inbound-agent` that has the same properties and can be launched in the same way as the official image.

## Why not set up through docker compose?
Due to how how Jenkins links agents that is not possible at the time. You manually have to register an agenet and then link it. This is due to the secret of the agent is generated when the agent is registered. This means that you can't create them along side each other and need to create one at the time.