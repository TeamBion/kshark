# Kubectl Tcpdump

That is a kubectl plugin which allows you to get pcap file output to watch network activity in pod level.You can easily connect your pods and execute TCPDUMP outputs without install anyof tool inside of the application pods.

## How you can use this ?
<img src="./img/usage.png"></img>


### How to install ?

```

#!/bin/bash
git clone git@github.com:WoodProgrammer/k8s-tcpdumper.git 
sudo mkdir -p /usr/local/bin/k8s-tcpdumper/src

sudo mv k8s-tcpdumper/src/ephemeral_container.py /usr/local/bin/k8s-tcpdumper/src/
sudo mv k8s-tcpdumper/main.py /usr/local/bin/k8s-tcpdumper/main.py

sudo mv k8s-tcpdumper/plugin/kubectl-tcpdump /usr/local/bin/kubectl-tcpdump

```

# TODO

* Dashboards
* stdin stdout controls
* Log Messages
and ...

<b>Kubernetes Controller</b> to track scheduled or ondemand network traffic sniffing
