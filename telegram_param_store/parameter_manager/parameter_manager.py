import asyncio
import logging
import uuid
from dataclasses import dataclass, field
from typing import Dict, List, Set, Union

from telegram_param_store.parameter_manager.dao import DAO

log = logging.getLogger(__name__)

class ParameterManager:
    dao = DAO
    params = DAO.load()
    
    @classmethod
    def get_all(cls):
        return cls.params
    
    @classmethod
    def get_param(cls, name:str):
        return cls.params.get(name, None)
    
    @classmethod
    def check_param_name(cls, name:str):
        return name in cls.params
    

@dataclass
class ParamRequest:
    param_name: str
    request_id: uuid.UUID = uuid.uuid4()
    
    def __hash__(self) -> int:
        return hash(self.request_id)
    
    
class ParamRequestManager:
    outstanding_requests  : Set[ParamRequest] = set()
    authenticated_requests: Set[ParamRequest] = set()
    rejected_requests     : Set[ParamRequest] = set()
    
    @classmethod
    def generate_auth_request(cls, param_name:str):
        new_request = ParamRequest(param_name=param_name)
        cls.outstanding_requests.add(new_request)
        return new_request
        
    @classmethod
    def complete_auth_request(cls, param_request: ParamRequest):
        if param_request not in cls.outstanding_requests:
            log.warning(f"received auth_request completition {param_request} but this request was not found in outstanding list")
            return
            
        cls.outstanding_requests.remove(param_request)
        cls.authenticated_requests.add(param_request)
        return True

    @classmethod
    def complete_auth_request__id(cls, param_request_id: Union[str, uuid.UUID]):
        matching_param_requests = [i for i in cls.outstanding_requests if str(i.request_id) == str(param_request_id)]
        if not matching_param_requests: 
            log.warning(f'could not find param_request from id {param_request_id}')
            return 
        if len(matching_param_requests) > 1:
            log.warning('more than one matching auth param request')
        
        param_request = matching_param_requests[0]
        cls.outstanding_requests.remove(param_request)
        cls.authenticated_requests.add(param_request)
        return True

    @classmethod
    async def get_parameter_if_completed(cls, param_request: ParamRequest):
        while True:
            if param_request in cls.authenticated_requests: 
                return ParameterManager.get_param(param_request.param_name)
            elif param_request in cls.rejected_requests:
                return False
            await asyncio.sleep(0.5)
