import subprocess
import logging

class Debug(object):
    def __init__(self):
        pass
    
    def getDump(self, params):
        pod = params["pod"]
        namespace = params["namespace"]
        interface = params["interface"]
        mode = params["mode"]

        try:
            subprocess.run(["./kubectl-shark", "-p", pod, "-n", namespace, "-i", interface])
        except Exception as exp:
            logging.error(exp)