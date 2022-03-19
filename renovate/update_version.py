#!/usr/bin/env python3
from ast import List
import glob
import json
import logging
import re
import pathlib
from typing import Optional

logging.basicConfig(level=logging.INFO)

RE_SHARED = re.compile(r"github>habx/devops-repo-shared-configs//([^#]*)(#.*)?$")

package_file = pathlib.Path("package.json")
version = json.loads(package_file.read_text())["version"]

for file_name in glob.glob("renovate/*.json"):
    logging.info("Reading file: %s", file_name)
    file = pathlib.Path(file_name)
    j = json.loads(file.read_text())
    extends = j.get("extends")
    if not extends:
        logging.info("No extends found in file: %s", file_name)
        continue
    
    for k, ext in enumerate(extends):
        if m := RE_SHARED.match(ext):
            j["extends"][k] = f"github>habx/devops-repo-shared-configs//{m.group(1)}#v{version}"

    logging.info("Writing file: %s", file_name)
    file.write_text(json.dumps(j, indent=4))
