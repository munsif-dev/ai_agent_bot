# In this project I am using uv and fastapi to create a simple bot that can answer questions.
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional 

# uv init - command to initialize the project
# uv run - command to run the project