# 安装 OpenMLDB Chart

```
helm install openmldb ./
```

# 配置Chart Values
| Name                          | Description                              | Value                   |
| ----------------------------- | ---------------------------------------- | ----------------------- |
| image.openmldbImage           | OpenMLDB 镜像，默认使用 Docker Hub 上的镜像，支持 OpenMLDB >= 0.8.2；用户也可以设置为本地仓库的镜像 | openmldb-online:0.8.4   |
| image.pullPolicy              | OpenMLDB镜像拉取策略                       | IfNotPresent            |
| tablet.containerPorts         | Tablet端口号                              | 10921                   |
| tablet.replicaCount           | Tablet副本数                              | 3                       |
| nameserver.containerPorts     | Nameserver端口号                          | 7527                    |
| nameserver.replicaCount       | Nameserver副本数                          | 2                       |
| nameserver.startupDelayTime   | Nameserver Pod延时启动时间，单位秒          | 30                      |
| timezone                      | 时区                                      | Asia/Shanghai           |
| idMountPath                   | 模块id文件mount路径, 需要和conf/tablet.flags conf/nameserver.flags配置文件中data_dir保持一致 | /openmldb/id           |
| dbMountPath                   | 数据目录mount路径, 需要和conf/tablet.flags配置文件中db目录对应 | /openmldb/data           |
| logMountPath                  | 日志目录mount路径, 需要和conf/tablet.flags conf/nameserver.flags配置文件中logs目录对应| /openmldb/logs           |
| udfLibraryDir                 | udf动态库路径                                | /openmldb/udf           |
| startupProbe.enabled          | 是否开启tablet startup探针                   | true                    |
| startupProbe.initialDelaySeconds| 探针延时秒数                               | 10                      |
| startupProbe.periodSeconds    | 探针的探测间隔                                | 30                      |
| startupProbe.timeoutSeconds   | 探针超时时间                                  | 1                       |
| startupProbe.failureThreshold | 探针失败阈值                                  | 60                      |
| startupProbe.successThreshold | 探针成功阈值                                  | 1                       |
| persistence.accessModes       | 配置存储卷访问模式                             | ReadWriteOnce           |
| persistence.dataDir.enabled   | 数据目录是否使用pvc                            | false                   |
| persistence.dataDir.size      | 配置数据目录存储卷大小                          | 8Gi                     |
| persistence.dataDir.storageClass|配置数据目录storageClass名字                  | ""                      |
| persistence.logDir.enabled   | 日志目录是否使用pvc                             | false                   |
| persistence.logDir.size      | 配置日志目录存储卷大小                           | 8Gi                     |
| persistence.logDir.storageClass| 配置日志目录storageClass名字                  | ""                      |
