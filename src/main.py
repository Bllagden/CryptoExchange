"""
    Description: For an exchange, get all trading pairs, their latest prices and trading volume for 24 hours
    Task: 
        Create a class inherited from the BaseExchange class. 
        Write the implementation of the methods and fill in the required fields (marked as "todo")
    Note: 
        Feel free to add another internal methods. 
        It is important that the example from the main function runs without errors
    The flow looks like this:
        1. Request data from the exchange
        2. We bring the ticker to the general format
        3. We extract from the ticker properties the last price, 
            the 24-hour trading volume of the base currency 
            and the 24-hour trading volume of the quoted currency. 
            (at least one of the volumes is required)
        4. Return the structure in the format: 
            {
                "BTC/USDT": TickerInfo(last=57000, baseVolume=11328, quoteVolume=3456789),
                "ETH/BTC": TickerInfo(last=4026, baseVolume=4567, quoteVolume=0)
            }
"""

import asyncio

from exchanges import MyExchange, biconomy, toobit
from types_ import Symbol, TickerInfo


async def main():
    """
    Test yourself here. Verify prices and volumes here: https://www.coingecko.com/
    """
    # exchange = biconomy()
    # exchange = toobit()
    exchange = MyExchange()

    await exchange.load_markets()
    tickers = await exchange.fetch_tickers()
    for symbol, prop in tickers.items():
        print(symbol, prop)

    assert isinstance(tickers, dict)
    for symbol, prop in tickers.items():
        assert isinstance(prop, TickerInfo)
        assert isinstance(symbol, Symbol)


if __name__ == "__main__":
    asyncio.run(main())
