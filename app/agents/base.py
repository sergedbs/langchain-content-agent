from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

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

    def generate(self, input_data: InputT) -> OutputT:
        system_prompt = self.get_system_prompt()
        user_prompt = self.build_user_prompt(input_data)

        output_schema = self.get_output_schema()

        structured_llm = self.llm.with_structured_output(output_schema)

        messages = [("system", system_prompt), ("human", user_prompt)]

        result = structured_llm.invoke(messages)
        return cast(OutputT, result)
