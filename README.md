## 制作镜像
用docker/build.sh脚本可以制作OpenMLDB镜像。第一个参数为OpenMLDB版本号。第二个参数是OpenMLDB部署包的源，默认是从国内镜像地址拉取，如果要从github拉取可以设置第二个参数为`github`
```bash
cd docker
sh build.sh 0.8.1
```
## 部署OpenMLDB到Kubernetes中
### 部署Zookeeper
如果有可用的Zookeeper可跳过此步
```
kubectl apply -f k8s/yaml/zookeeper.yaml 
```

### 创建configmap
OpenMLDB的配置文件放置在k8s configmap中. 
#### 1. 修改 zookeeper 地址
修改 k8s/conf/conf/tablet.flags 和 k8s/conf/nameserver.flags 文件中 `zk_cluster` 为实际zookeeper地址。默认 `zk_root_path` 为 `/openmldb`
#### 2. 创建 configmap 
```bash
kubectl create cm tablet-config --from-file k8s/conf/tablet.flags -n openmldb
kubectl create cm nameserver-config --from-file k8s/conf/nameserver.flags -n openmldb
```
### 部署OpenMLDB
```
kubectl apply -f k8s/yaml/openmldb.yaml 
```
注:  
- yaml里边用的是0.8.1的版本，如果制作镜像时用的其他版本，需要在openmldb.yaml里修改下
- OpenMLDB 默认会部署3个tablet和2个nameserver。至少需要部署3个k8s node. 如果node不够可以在yaml/openmldb.yaml中设置`replicas`个数
- 目前OpenMLDB的数据默认会放在pod里边的数据盘下，没有挂载PV. 所以pod重启会导致数据丢失。
- 部署的OpenMLDB服务只能在k8s内部访问