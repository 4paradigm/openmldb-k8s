## 制作镜像
用docker/build.sh脚本可以制作OpenMLDB镜像。第一个参数为OpenMLDB版本号。第二个参数是OpenMLDB部署包的源，默认是从国内镜像地址拉取，如果要从github拉取可以设置第二个参数为`github`
```bash
cd docker
sh build.sh 0.8.2
```
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
helm install openmldb ./openmldb --set persistence.dataDir.enabled=true --set  persistence.dataDir.storageClass=local-storage
```

注:  
- 部署的OpenMLDB服务只能在k8s内部同一个namespace下访问
- 通过此方式部署的OpenMLDB集群没有部署TaskManager模块，所以不能用[LOAD DATA](https://openmldb.ai/docs/zh/main/openmldb_sql/dml/LOAD_DATA_STATEMENT.html)和[SELECT INTO](https://openmldb.ai/docs/zh/main/openmldb_sql/dql/SELECT_INTO_STATEMENT.html)语句，也不能使用离线相关功能。
- 如果要上生产环境，需要在k8s部署tablet的node节点上关闭THP，否则可能存在删除的表内存不能完全释放问题. 关闭方式参考[这里](https://openmldb.ai/docs/zh/main/deploy/install_deploy.html#thp-transparent-huge-pages)