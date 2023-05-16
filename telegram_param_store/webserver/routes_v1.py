
import logging

from fastapi import APIRouter, HTTPException, Request, Response, status
from pydantic import BaseModel

from telegram_param_store.parameter_manager.parameter_manager import (
    ParameterManager,
    ParamRequestManager,
)
from telegram_param_store.telegram_bot.services.send_message import (
    send_message_to_defined_user,
)
from telegram_param_store.webserver.responses import text_response

log = logging.getLogger(__name__)
ROUTE_PREFIX = '/param_store/v1'

router = APIRouter(
    prefix=ROUTE_PREFIX,
)


@router.get('/')
def heartbeat():
    return text_response("we're up!")

@router.get('/get_param')
async def endpoint(request: Request, response: Response, name:str):
    log.info(f'requested parameter with name: {name}')
    param = ParameterManager.get_param(name)
    
    if not param: 
        response.status_code = status.HTTP_404_NOT_FOUND
        return text_response(f'parameter with name {name} not found')
    
    
    auth_request = ParamRequestManager.generate_auth_request(name)
    send_message_to_defined_user(f'authenticate param request for {name}')
    send_message_to_defined_user(f'{auth_request.request_id}')
    
    param_value = await ParamRequestManager.get_parameter_if_completed(auth_request)
    if param_value:
        return text_response(param_value)
    
    return text_response(f'value could not be fetched: {param_value}')