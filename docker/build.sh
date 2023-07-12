#!/bin/bash

# Copyright 2021 4Paradigm
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

VERSION=$1
if [[ ! ${VERSION} =~ ^[0-9]\.[0-9]\.[0-9]$ ]]
then
    echo "invalid version ${VERSION}"
    exit 0
fi
DOWNLOAD_URL="http://43.138.115.238/download/v${VERSION}/openmldb.tar.gz"
if [[ $# -eq 2 ]] && [[ $2 = "github" ]]
then
    DOWNLOAD_URL="https://github.com/4paradigm/OpenMLDB/releases/download/v${VERSION}/openmldb-${VERSION}-linux.tar.gz"
fi
curl -SLo openmldb.tar.gz ${DOWNLOAD_URL}
mkdir openmldb
tar xzf openmldb.tar.gz -C "openmldb" --strip-components 1
cp Dockerfile openmldb/
rm -rf openmldb.tar.gz
pushd openmldb
docker build -t openmldb-online:${VERSION} .
popd
