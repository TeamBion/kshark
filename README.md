<h1 align="center">kshark </h1>


<p align="center">
<img src="img/logo.png"></img>
</p>

A kubectl plugin that allows us to gather network information with tcpdump command without no binary injection on your pods.

This plugin use the debug containers to inject your pods and gather tcpdump data.

# Usage

This the current example usage of kubectl shark command.This command allows us to run different kind a analysis on wireshark.

<img src="img/main.gif"></img>

```sh
    kubectl shark -p <POD-NAME> -n kube-system -i eth0
```

## Usage
If you want to run debug containers on your Kubernetes cluster you need to enable FeatureGates on your components shown as below on <b>api-server</b> and <b>controller-manager</b>.

```yaml
   ... 
   ...
   --feature-gates=EphemeralContainers=true
```
### In EKS;
EKS allows us to use debug with the newer versions on Kubernetes so that ability will be managed kubernetes users.

## Installation

kubectl-shark has got very simple installation type like shown as below;

```sh
    pip3 install . --upgrade
```
