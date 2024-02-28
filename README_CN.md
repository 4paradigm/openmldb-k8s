# OpenMLDB 在线引擎的 Kubernetes 部署工具
## 要求
本部署工具提供 OpenMLDB 在线引擎基于 Kubernetes 的部署方案，基于 Helm Charts 实现。在以下版本通过测试（其他低版本未验证）：
- Kubernetes 1.19+
- Helm 3.2.0+

另外，如果用户使用 Docker Hub 上的预编译 OpenMLDB 镜像，目前仅支持 OpenMLDB >= 0.8.2。用户也可以通过我们的工具自己[制作其他版本的 OpenMLDB 镜像](./docker/README.md)。

## 准备工作：部署 ZooKeeper
如果用户已经有可用的 ZooKeeper，可跳过此步。否则进行安装：
```
helm install zookeeper oci://registry-1.docker.io/bitnamicharts/zookeeper --set persistence.enabled=false
```
如果要把数据持久化，可以指定已创建的storage class
```
helm install zookeeper oci://registry-1.docker.io/bitnamicharts/zookeeper --set persistence.storageClass=local-storage
```
更多参数设置参考[这里](https://github.com/bitnami/charts/tree/main/bitnami/zookeeper)

## 部署OpenMLDB

### 下载 repo 源代码

下载本 repo 源代码，并且将后续工作目录设置在本 repo 的根目录：

```bash
git clone https://github.com/4paradigm/openmldb-k8s.git
cd openmldb-k8s
```

### 配置 ZooKeeper 地址

修改 `charts/openmldb/conf/tablet.flags` 和 `charts/openmldb/conf/nameserver.flags` 文件中 `zk_cluster` 为实际 ZooKeeper 地址，其默认 `zk_root_path` 为 `/openmldb` 。

### 部署OpenMLDB
使用 Helm 基于如下命令，可以进行一键化部署：
```
helm install openmldb ./charts/openmldb
```
用户可以通过 `--set` 命令设置更多的部署选项 ，具体支持的选项查看 [OpenMLDB Chart 配置文档](charts/openmldb/README.md)。

其中比较重要的配置项需要注意：

- 默认使用临时文件保存数据，因此当pod重启后数据会丢失。推荐通过如下方式绑定pvc到指定storageclass

```
helm install openmldb ./charts/openmldb --set persistence.dataDir.enabled=true --set  persistence.dataDir.storageClass=local-storage
```

- 默认使用 Docker Hub 上的 `4pdosc/openmldb-online` 镜像（仅支持 OpenMLDB >= 0.8.2），如果要用自己的镜像，可以在 `install` 时通过 `--set image.openmldbImage` 来指定使用的镜像名称。镜像制作方式参考[这里](./docker/README.md)。

```
helm install openmldb ./charts/openmldb --set image.openmldbImage=openmldb-online:0.8.5
```
### 注意事项

- 部署的 OpenMLDB 服务只能在 Kubernetes 内部同一个 namespace 下访问
- 通过此方式部署的 OpenMLDB 集群没有部署 TaskManager 模块，所以不能用[LOAD DATA](https://openmldb.ai/docs/zh/main/openmldb_sql/dml/LOAD_DATA_STATEMENT.html)和[SELECT INTO](https://openmldb.ai/docs/zh/main/openmldb_sql/dql/SELECT_INTO_STATEMENT.html)语句，也不能使用离线相关功能。如果要将数据导入到 OpenMLDB 可以使用 OpenMLDB 的[在线导入工具](https://openmldb.ai/docs/zh/main/tutorial/data_import.html)、[OpenMLDB Connector](https://openmldb.ai/docs/zh/main/integration/online_datasources/index.html) 或者 SDK。如果要导出表的数据，可以使用[在线数据导出工具](https://openmldb.ai/docs/zh/main/tutorial/data_export.html)。
- 如果要上生产环境，需要在 Kubernetes 部署 tablet 的物理节点上关闭 THP，否则可能存在删除的表内存不能完全释放问题。关闭方式参考[这里](https://openmldb.ai/docs/zh/main/deploy/install_deploy.html#thp-transparent-huge-pages)
