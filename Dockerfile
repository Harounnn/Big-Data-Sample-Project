ARG NODE_TYPE

FROM sequenceiq/hadoop-docker:2.7.1

COPY conf/* /usr/local/hadoop/etc/hadoop/

RUN if [ "$NODE_TYPE" = "namenode" ]; then \
        sed -i '/^export JAVA_HOME/ s:.*:export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64\nexport HADOOP_PREFIX=/usr/local/hadoop\nexport HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:' /usr/local/hadoop/etc/hadoop/hadoop-env.sh; \
        hdfs namenode -format; \
    fi

CMD ["sh", "-c", "service ssh start; bash"]
