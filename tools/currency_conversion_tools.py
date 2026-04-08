from utils.currency_converter import CurrencyConvertor
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv
import os

class CurrencyConvertorTool:

    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get('EXCHANGE_RATE_API_KEY')
        self.currency_service = CurrencyConvertor(self.api_key)
        self.currency_convertor_tool_list = self._setuptools()

    def _setuptools(self) -> List:
        """Setup all tools for the currency convertor tool"""

        @tool
        def convert_currency(amount: float, from_currency: str, to_currency:str):
            """Convert amount from one currency to another"""

            return self.currency_service.convert(amount, from_currency, to_currency)
        
        return [convert_currency]
    
    