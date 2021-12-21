"""
Exmaple of using the sosapi to query Binance.
"""


# class BaseClient:
#     def __init__(self, key=None, secret=None):
#         self.api_key = key if key is not None else env('BINANCE_API_KEY', cast=str)
#         self.api_secret = secret if secret is not None else env('BINANCE_API_SECRET', cast=str)

#         assert self.api_key is not None, "Missing API_KEY"
#         assert self.api_secret is not None, "Missing API_SECRET"

#         self.base_url = 'https://api.binance.com'
#         limit_requests_per_minute = 12000
#         self.request_interval = 1.0 / (limit_requests_per_minute / 60.0)

