FROM centos:7.9.2009

ENV LANG=en_US.UTF-8 
ENV TZ=Asia/Shanghai
ENV COMPONENT="tablet"

RUN swapoff -a
RUN ulimit -c unlimited

COPY bin/openmldb /openmldb/bin/

RUN mkdir -p /openmldb/udf

EXPOSE 10921 7527

WORKDIR /openmldb
ENTRYPOINT ["sh", "-c", "/openmldb/bin/openmldb --flagfile=/openmldb/conf/${COMPONENT}.flags --enable_status_service=true >> logs/${COMPONENT}.log"]
