# 制作镜像

用docker/build.sh脚本可以制作OpenMLDB镜像。

该脚本支持两个参数：

- 第一个参数为OpenMLDB版本号。
- 第二个参数是OpenMLDB部署包的源，默认是从中国大陆镜像地址拉取，如果要从 GitHub 拉取可以设置第二个参数为 `github`

```bash
cd docker
sh build.sh 0.8.4
```
