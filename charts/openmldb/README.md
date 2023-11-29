# Install OpenMLDB Chart

```
helm install openmldb ./
```

# Chart Value Configurations
| Name                          | Description                              | Value                   |
| ----------------------------- | ---------------------------------------- | ----------------------- |
| image.openmldbImage           | OpenMLDB iamge, use docker image from Docker Hub by defualt. Support version >= 0.8.2; User can configure it to be a local image | openmldb-online:0.8.4   |
| image.pullPolicy              | OpenMLDB pull policy                         | IfNotPresent            |
| tablet.containerPorts         | Tablet port                                  | 10921                   |
| tablet.replicaCount           | number of Tablet replicas                    | 3                       |
| nameserver.containerPorts     | Nameserver port                              | 7527                    |
| nameserver.replicaCount       | number of Nameserver replicas                | 2                       |
| nameserver.startupDelayTime   | Nameserver Pod startup delay time in seconds | 30                      |
| timezone                      | time zone                                    | Asia/Shanghai           |
| idMountPath                   | id mount path, keep it consistent with `data_dir` in `conf/tablet.flags conf/nameserver.flags` | `/openmldb/id`           |
| dbMountPath                   | data mount path, keep it consistent with db path in `conf/tablet.flags`                        | `/openmldb/data`           |
| logMountPath                  | log mount path, keep it consistent with logs path in `conf/tablet.flags conf/nameserver.flags` | `/openmldb/logs`           |
| udfLibraryDir                 | udf library path                             | `/openmldb/udf`           |
| startupProbe.enabled          | whether to enable tablet startup             | true                    |
| startupProbe.initialDelaySeconds| probe delay seconds                        | 10                      |
| startupProbe.periodSeconds    | probe period in seconds                      | 30                      |
| startupProbe.timeoutSeconds   | probe timeout in seconds                     | 1                       |
| startupProbe.failureThreshold | probe failure threshold                      | 60                      |
| startupProbe.successThreshold | probe suncess threshold                      | 1                       |
| persistence.accessModes       | access mode                                  | ReadWriteOnce           |
| persistence.dataDir.enabled   | whether to enable pvc for data directory     | false                   |
| persistence.dataDir.size      | size of data directory                       | 8Gi                     |
| persistence.dataDir.storageClass| storageClass name for data directory       | ""                      |
| persistence.logDir.enabled   | whether to enable pvc for log directory       | false                   |
| persistence.logDir.size      |  size of log directory                        | 8Gi                     |
| persistence.logDir.storageClass| storageClass name for log directory         | ""                      |

<details>
<summary>中文</summary>
<!-- Chinese Content Goes Here -->

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
| idMountPath                   | 模块id文件mount路径, 需要和`conf/tablet.flags conf/nameserver.flags`配置文件中`data_dir`保持一致 | `/openmldb/id`           |
| dbMountPath                   | 数据目录mount路径, 需要和`conf/tablet.flags`配置文件中db目录对应 | `/openmldb/data`           |
| logMountPath                  | 日志目录mount路径, 需要和`conf/tablet.flags` `conf/nameserver.flags`配置文件中logs目录对应| `/openmldb/logs`           |
| udfLibraryDir                 | udf动态库路径                                | `/openmldb/udf`           |
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

</details>
