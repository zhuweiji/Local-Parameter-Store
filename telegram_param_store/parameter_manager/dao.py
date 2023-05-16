import logging
from pathlib import Path

import tomli
import tomli_w

log = logging.getLogger(__name__)

class DAO:
    data_file_path = Path(__file__).parents[2] / 'params.toml'
    
    @classmethod
    def load(cls):
        if not cls.data_file_path.is_file(): cls.data_file_path.touch()
        
        with open(cls.data_file_path, mode="rb") as fp:
            return tomli.load(fp)
        
    @classmethod
    def update(cls, d:dict):
        with open(cls.data_file_path, mode="r+b") as fp:
            tomli_w.dump(d, fp)
            
        return d