from diagrams import Diagram
from diagrams.onprem.network import Internet
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.onprem.client import Client, Users

with Diagram("Simple app", show=False):
    
    Client() >> Internet("localhost:5000") >> EC2("web") >> RDS("userdb")

