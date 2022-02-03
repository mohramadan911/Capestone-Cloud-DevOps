# Capstone-Cloud-DevOps
Working in AWS Using  Circle CI to implement Continuous Integration and Continuous Deployment Building pipelines Working with Ansible and CloudFormation to deploy clusters Building Kubernetes clusters Building Docker containers in pipelines

#Steps :
1. Build Docker Image
2. Test docker build by lint (Hadolint for docker)
3. Upload Docker to my image repository mohramadan911/mycapstoneproject
4. Deploy Infrastrcture
   > Build EKS Network and ensure if it is exist or not. (Diagram is attached)
   > Build EKS Cluster and ensure if it is exist or not.
   > Build Node Group and enusre if it is exist or not.
   > Build EC2 Managment instances and ensure if it is exist or not.
   > Extract the IPs of the management instances for Ansible
   > Use ansible to configure servers
   > Create a kubeconfig file for the cluster
   > Confiure EKS Cluster
      - Apply deployment of the welcome application docker image
      - Apply Load Balancer Service
   > Upload Docker locally
      - Update the deployment to run the latest Build
      - Check if deployment is successful

Load Balancer IP :
http://a91b7ba67449945529448c4215b23184-546996982.us-east-1.elb.amazonaws.com/


This is was my main capstone project and Next challange for me I have designed a python program to monitor pods which are running more than 7 days with specifc lable to search you can find in the following URL : https://github.com/mohramadan911/Share-Pods-logging.git 
