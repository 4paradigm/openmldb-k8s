# OpenMLDB 在线引擎基于 Kubernetes 部署

## 用Helm部署OpenMLDB到Kubernetes中
### 部署Zookeeper
如果有可用的Zookeeper可跳过此步
```
helm install zookeeper oci://registry-1.docker.io/bitnamicharts/zookeeper --set persistence.enabled=false
```
如果要把数据持久化，可以指定已创建的storage class
```
helm install zookeeper oci://registry-1.docker.io/bitnamicharts/zookeeper --set persistence.storageClass=local-storage
```
更多参数设置参考[这里](https://github.com/bitnami/charts/tree/main/bitnami/zookeeper)

### 部署OpenMLDB

#### 修改 zookeeper 地址

修改 charts/openmldb/conf/tablet.flags 和 charts/openmldb/conf/nameserver.flags 文件中 `zk_cluster` 为实际zookeeper地址。默认 `zk_root_path` 为 `/openmldb`

#### 部署OpenMLDB
```
helm install openmldb ./charts/openmldb
```
默认使用临时文件保存数据，如果pod重启数据会丢失。可以通过如下方式绑定pvc到指定storageclass
```
helm install openmldb ./charts/openmldb --set persistence.dataDir.enabled=true --set  persistence.dataDir.storageClass=local-storage
```

默认使用4pdosc/openmldb-online镜像，如果要用自己build的镜像，可以在install时通过 --set image.openmldbImage来指定使用的镜像名称。镜像build方式参考[这里](./docker/README.md)
```
helm install openmldb ./charts/openmldb --set image.openmldbImage=openmldb-online:0.8.2
```
注:  
- 部署的OpenMLDB服务只能在k8s内部同一个namespace下访问
- 通过此方式部署的OpenMLDB集群没有部署TaskManager模块，所以不能用[LOAD DATA](https://openmldb.ai/docs/zh/main/openmldb_sql/dml/LOAD_DATA_STATEMENT.html)和[SELECT INTO](https://openmldb.ai/docs/zh/main/openmldb_sql/dql/SELECT_INTO_STATEMENT.html)语句，也不能使用离线相关功能。如果要将数据导入到OpenMLDB可以使用OpenMLDB的[在线导入工具](https://openmldb.ai/docs/zh/main/tutorial/data_import.html)、[OpenMLDB Connector](https://openmldb.ai/docs/zh/main/integration/online_datasources/index.html)和sdk。如果要导出表的数据，可以使用[在线数据导出工具](https://openmldb.ai/docs/zh/main/tutorial/data_export.html)。
- 如果要上生产环境，需要在k8s部署tablet的node节点上关闭THP，否则可能存在删除的表内存不能完全释放问题。关闭方式参考[这里](https://openmldb.ai/docs/zh/main/deploy/install_deploy.html#thp-transparent-huge-pages)