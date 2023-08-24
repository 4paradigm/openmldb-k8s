FROM centos/python-38-centos7

ENV LANG=en_US.UTF-8 
ENV COMPONENT="tablet"
RUN pip install --no-cache-dir prettytable
RUN swapoff -a
RUN ulimit -c unlimited

COPY bin/openmldb /openmldb/bin/
COPY tools /openmldb/tools

VOLUME /openmldb/udf

EXPOSE 10921 7527

WORKDIR /openmldb
USER root
ENTRYPOINT ["sh", "-c", "/openmldb/bin/openmldb --flagfile=/openmldb/conf/${COMPONENT}.flags --enable_status_service=true > ${COMPONENT}.log"]
