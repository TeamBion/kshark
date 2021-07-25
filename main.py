import sys
import os
from src.debugger import Debugger

client_cert_cert_path=sys.argv[1]
client_cert_key_path=sys.argv[2]
cluster_address=sys.argv[3]
pod_name = sys.argv[4]

debugger = Debugger(host=cluster_address, client_cert_path=client_cert_path, client_cert_key_path=client_cert_key_path)

if __name__ == "__main__":
    debugger.createDebugContainer()