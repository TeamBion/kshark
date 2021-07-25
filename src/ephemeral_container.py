import requests
import json
from kubernetes import config

class Debugger(object):
    def __init__(self, host="", port=6443, client_cert_path="/home/ubuntu/.kube/usr.crt",client_cert_key_path="/home/ubuntu/.kube/usr.key"):
        self.port = port
        self.host = host
        self.client_cert_path = client_cert_path
        self.client_cert_key_path = client_cert_key_path
        self.ephemeral_pod_json = {
            "apiVersion": "v1",
            "kind": "EphemeralContainers",
            "metadata": {
                "name": "TARGET_POD_NAME",
                "namespace": "NAMESPACE"
            },
            "ephemeralContainers": [{
                "command": [
                    "sh"
                ],
                "image": "emirozbir/tcpdumper:latest",
                "imagePullPolicy": "IfNotPresent",
                "name": "debugger",
                "stdin": True,
                "targetContainerName": "CONTAINER_NAME",
                "tty": True,
                "terminationMessagePolicy": "File"
            }]
        }


    def createDebugContainer(self, podName, namespace, containerName, **kwargs):
        print("Namespace {} {} ".format(namespace, podName))
        self.ephemeral_pod_json["metadata"]["name"] = podName
        self.ephemeral_pod_json["metadata"]["namespace"] = namespace
        self.ephemeral_pod_json["ephemeralContainers"][0]["targetContainerName"] = containerName
        header = {
            "Content-Type": "application/json",
            "Accept": "application/json, */*",
            "User-Agent": "kubectl/v1.21.3 (linux/amd64) kubernetes/ca643a4" ##version must be over than 1.18
        }
        cert = (self.client_cert_path, self.client_cert_key_path)
        resp = requests.put(headers=header,
                url="{}/api/v1/namespaces/{}/pods/{}/ephemeralcontainers".format(self.host, namespace, podName),
                data=json.dumps(self.ephemeral_pod_json),
                cert=cert,
                verify=False)


        return resp.status_code, resp.content