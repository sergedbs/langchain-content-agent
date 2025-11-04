from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from langchain_openai import ChatOpenAI

InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


class BaseAgent(ABC, Generic[InputT, OutputT]):
    def __init__(self, llm: ChatOpenAI):
        self.llm = llm

   @abstractmethod
    def get_system_prompt(self) -> str:
        pass
    
    @abstractmethod
    def build_user_prompt(self, input_data: InputT) -> str:
        pass
    
    @abstractmethod
    def get_output_schema(self) -> type[OutputT]:
        pass
