# Big Data using Hadoop Framework
## Part 1 - Installing a Hadoop cluster using Docker
**Before starting make sure that docker and docker-compose are installed in your system**
```bash
docker version
docker-compose version
```
In this part, we will setup a 4-node hadoop cluster (1 master & 3 slaves)
1. Write the following inside 'docker-compose.yml' file :
```
version: "1.0"

services:
  namenode:
    image: sequenceiq/hadoop-docker  
    hostname: namenode
    ports:
      - "50070:50070"
      - "8088:8088"
    environment:
      HADOOP_NAMENODE_FORMAT: "true" 
    volumes:
      - hadoop-namenode:/hadoop/hdfs/namenode  

  datanode1:
    image: sequenceiq/hadoop-docker 
    hostname: datanode1
    volumes:
      - hadoop-datanode1:/hadoop/hdfs/datanode

  datanode2:
    image: sequenceiq/hadoop-docker  
    hostname: datanode2
    volumes:
      - hadoop-datanode2:/hadoop/hdfs/datanode

  datanode3:
    image: sequenceiq/hadoop-docker  
    hostname: datanode3
    volumes:
      - hadoop-datanode3:/hadoop/hdfs/datanode

volumes:
  hadoop-namenode: {}
  hadoop-datanode1: {}
  hadoop-datanode2: {}
  hadoop-datanode3: {}
```
2. Save and type :
```bash
docker-compose up -d
```