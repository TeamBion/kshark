# kshark

A kubectl plugin that allows us to gather network information with tcpdump command without no binary injection on your pods.

This plugin use the debug containers to inject your pods and gather tcpdump data.

# Usage

This the current example usage of kubectl shark command.This command allows us to run different kind a analysis on wireshark.

<img src="img/main.gif"></img>

```sh
    kubectl shark -p <POD-NAME> -n kube-system -i eth0
```

## Prerequirements
If you want to run debug containers on your Kubernetes cluster you need to enable FeatureGates on your components shown as below on <b>api-server</b> and <b>controller-manager</b>.

```yaml
   ... 
   ...
   --feature-gates=EphemeralContainers=true
```

## Installation

kubectl-shark has got very simple installation type like shown as below;

```sh
    make all-deps
    make install
```