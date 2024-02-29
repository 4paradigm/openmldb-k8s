# Create Docker Image

The `docker/build.sh` script can be used to create a OpenMLDB docker image. 

This script supports two parameters:
- OpenMLDB version number.
- Source of the OpenMLDB package. By default, it pulls the package from a mirror in mainland China. If you want to pull it from GitHub, you can set the second parameter to 'github'.

```bash
cd docker
sh build.sh 0.8.5
```


<details>
<summary>中文</summary>

# 制作镜像

用`docker/build.s`h脚本可以制作OpenMLDB镜像。

该脚本支持两个参数：

- 第一个参数为OpenMLDB版本号。
- 第二个参数是OpenMLDB部署包的源，默认是从中国大陆镜像地址拉取，如果要从 GitHub 拉取可以设置第二个参数为 `github`

```bash
cd docker
sh build.sh 0.8.5
```
</details>
