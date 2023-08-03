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
import sys
from tool import Executor
import logging
import os
log = logging.getLogger(__name__)

def parse_zk_address(conf):
    zk_cluster = ''
    zk_root_path = ''
    db_root_path = ''
    with open(conf, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line == '' or line.startswith('#'):
                continue
            arr = line[2:].split('=')
            if arr[0] == "zk_cluster":
                zk_cluster = arr[1]
            elif arr[0] == "zk_root_path":
                zk_root_path = arr[1]
            elif arr[0] == "db_root_path":
                db_root_path = arr[1]
    return (zk_cluster, zk_root_path, db_root_path)

if __name__ == '__main__':
    conf = sys.argv[1]
    (zk_cluster, zk_root_path, db_root_path) = parse_zk_address(conf)
    if db_root_path == "":
        log.error("db_root_path is empty")
        sys.exit(1)
    else:
        test_file = db_root_path.split(",")[0] + "/prob.lock"
        if not os.path.isfile(test_file):
            log.info(f"{test_file} does not exist")
            with open(test_file, 'w') as f:
                f.write("test file");
            sys.exit(0)
    openmldb_bin_path = "./bin/openmldb"
    if zk_cluster == "" or zk_root_path == "":
        log.error("zk conf is empty")
        sys.exit(1)
    log.info(f"zk_cluster: {zk_cluster}, zk_root_path: {zk_root_path}")
    executor = Executor(openmldb_bin_path, zk_cluster, zk_root_path)
    if not executor.Connect().OK():
        log.error("connect OpenMLDB failed")
        sys.exit(1)
    log.info("connected")
    status, result = executor.ShowOpStatus("", "")
    if status.OK():
        for record in result:
            log.info(record)
            if record[4] == 'kDoing':
                log.info(record)
                sys.exit(1)
        log.info("no doing job")
        sys.exit(0)
    else:
        log.warn(status.GetMsg())
        sys.exit(1)
