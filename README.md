# Kubernetes deployment tool for OpenMLDB online engine
## Request
This deployment tool offers a Kubernetes-based deployment solution for the OpenMLDB online engine, implemented using Helm Charts. The tool has been tested and verified with the following versions:

- Kubernetes 1.19+
- Helm 3.2.0+

Additionally, for users who utilize pre-compiled OpenMLDB images from Docker Hub, only OpenMLDB versions >= 0.8.2 are supported. Users also have the option to [create other versions of OpenMLDB images using our tools](https://chat.openai.com/c/docker/README.md).

## Preparation task: Deploy ZooKeeper
If the user already has an available ZooKeeper instance, they can skip this step. Otherwise, proceed with the installation process:

```
helm install zookeeper oci://registry-1.docker.io/bitnamicharts/zookeeper --set persistence.enabled=false
```
If you want to persist data, you can specify the created storage class

```
helm install zookeeper oci://registry-1.docker.io/bitnamicharts/zookeeper --set persistence.storageClass=local-storage
```
For more parameter settings, refer to [here](https://github.com/bitnami/charts/tree/main/bitnami/zookeeper)

## Deploy OpenMLDB

### Download the repo source code

Download the source code of this repository and set the working directory to the root directory of the repository.

```bash
git clone https://github.com/4paradigm/openmldb-k8s.git
cd openmldb-k8s
```

### Configure ZooKeeper address

Modify the `zk_cluster` in the `charts/openmldb/conf/tablet.flags` and `charts/openmldb/conf/nameserver.flags` files to the actual ZooKeeper address, with the default `zk_root_path` set to `/openmldb`.

###  Deploy OpenMLDB
You can achieve one-click deployment using Helm with the following commands:
```
helm install openmldb ./charts/openmldb
```
Users have the flexibility to configure additional deployment options using the `--set` command. Detailed information about supported options can be found in the [OpenMLDB Chart Configuration Documentation](https://chat.openai.com/c/charts/openmldb/README.md).

Important configuration considerations include:

- By default, temporary files are used for data storage, which means that data may be lost if the pod restarts. It is recommended to associate a Persistent Volume Claim (PVC) with a specific storage class using the following method:

```
helm install openmldb ./charts/openmldb --set persistence.dataDir.enabled=true --set  persistence.dataDir.storageClass=local-storage
```

- By default, the `4pdosc/openmldb-online` image from Docker Hub is utilized (supporting OpenMLDB >= 0.8.2). If you prefer to use a custom image, you can specify the image name during installation with `--set image.openmldbImage`. For information on creating custom images, refer to the image production guidelines [here](https://chat.openai.com/c/docker/README.md).

```
helm install openmldb ./charts/openmldb --set image.openmldbImage=openmldb-online:0.8.2
```
### Things to note

Here are some important considerations:

- Deployed OpenMLDB services can only be accessed within the same namespace within Kubernetes.
- The OpenMLDB cluster deployed using this method does not include a TaskManager module. Consequently, functionalities such as [LOAD DATA](https://openmldb.ai/docs/en/main/openmldb_sql/dml/LOAD_DATA_STATEMENT.html) and the statement and offline-related functions of [SELECT INTO](https://openmldb.ai/docs/en/main/openmldb_sql/dql/SELECT_INTO_STATEMENT.html) are not supported. If you need to import data into OpenMLDB, you can use OpenMLDB's [Online Import Tool](https://openmldb.ai/docs/en/main/tutorial/data_import.html), [OpenMLDB Connector](https://openmldb.ai/docs/en/main/integration/online_datasources/index.html), or SDK. For exporting table data, the [Online Data Export Tool](https://openmldb.ai/docs/en/main/tutorial/data_export.html) can be utilized.
- To transition to a production environment, it's necessary to disable Transparent Huge Pages (THP) on the physical node where Kubernetes deploys the tablet. Failure to do so may result in issues where memory from deleted tables cannot be fully released. For instructions on disabling THP, please refer to [this link](https://openmldb.ai/docs/en/main/deploy/install_deploy.html#thp-transparent-huge-pages).
