#
# #now we are creating a graph , the first thing we are creating is state
# import os
#
#
# #1)typed Dict (most common approach used)
#
# from typing import TypedDict
#
# class State(TypedDict):
#     topic : str
#     summary : str = ""
#     score : int
#
#
# #2)pydantic approach
# #it is good at type checking and data validation at runtime
#
# from pydantic import BaseModel,field_validator
#
# class State(BaseModel):
#     topic : str
#     summary : str = ""
#     score : int
#
#     @field_validator
#     def score_positive(cls, v):
#         if v  < 0:
#             raise ValueError("Score must be positive")
# #3)python dataclasses
#
# from dataclasses import dataclass,field
#
# @dataclass
# class State:
#     topic: str
#     summary: str
#     message: list = field(default_factory=list)
#
#
# #4)MessageState
#
# from langgraph.graph import MessagesState
#
# class State(MessagesState):
#     username: str
#     languages:str
#
#
#
