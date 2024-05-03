import os
import yaml

from appleparser import package_dir, log


class Environment:
    def __init__(self):
        self.__config = None

    def get_config(self):
        if not self.__config:
            conf_path = os.path.join(package_dir, '../', 'apple_config.yml')
            log.info("Package Path: %s", package_dir)
            log.info("Config Path: %s", conf_path)
            with open(conf_path, 'r', encoding='utf-8') as f:
                self.__config = yaml.safe_load(f.read())
        return self.__config
