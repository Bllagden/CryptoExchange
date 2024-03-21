from types_ import Symbol, TickerInfo

from .base_exchange import BaseExchange


class MyExchange(BaseExchange):
    """
    docs:
    https://docs.coingecko.com/v3.0.1/reference/introduction
    https://docs.coingecko.com/v3.0.1/reference/exchanges-id-tickers
    """

    def __init__(self):
        self.id = "fatbtc"
        self.base_url = "https://api.coingecko.com/"
        self.markets = {}  # not needed

    def _convert_symbol_to_ccxt(self, symbols: str) -> Symbol: ...  # not needed

    def _convert_base_and_target_to_ccxt(self, base: str, target: str) -> Symbol:
        if isinstance(base, str) and isinstance(target, str):
            return f"{base}/{target}"
        raise TypeError(f"{base} or/and {target} invalid types")

    def normalize_data(self, data: dict) -> dict[Symbol, TickerInfo]:
        normalized_data = {}
        tickers: list[dict] = data.get("tickers", [])

        for ticker in tickers:
            symbol = self._convert_base_and_target_to_ccxt(
                ticker.get("base", ""),
                ticker.get("target", ""),
            )

            normalized_data[symbol] = TickerInfo(
                last=float(ticker.get("last", 0)),
                baseVolume=float(ticker.get("volume", 0)),
                quoteVolume=0,
            )
        return normalized_data

    async def fetch_tickers(self) -> dict[Symbol, TickerInfo]:
        """data: {'name': 'FatBTC', 'tickers': [   {...}, {...} ..., {...}   ]}"""
        data: dict = await self.fetch_data(
            self.base_url + f"api/v3/exchanges/{self.id}/tickers"
        )
        return self.normalize_data(data)

    async def load_markets(self): ...  # not needed
