import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

log = logging.getLogger(__name__)

from telegram_param_store.webserver import routes_v1

tags_metadata = [
    {
        "name": "",
        "description": "",
    },
]

origins = [
]

   
app = FastAPI(
    title="Parameter Store API",
    openapi_tags=tags_metadata,
)
        
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=routes_v1.router
)

webserver = uvicorn.Server(
    config=uvicorn.Config(
        app=app,
        port=8080,
        # use_colors=False,
        host="0.0.0.0",
    )
)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)