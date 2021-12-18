# Extending the Base Client


```python
from sosapi import BaseClient

class MyClient(BaseClient):
    def __init__(self):
        super().__init__(
            base_url="http://www.my-website.com/api",
            headers=None,
            max_requests_per_min=60,
            response_kind="json",
        )

    def price(self, token):
        endpoint = "/token_price"
        url = self.base_url + endpoint
        params = dict(token=token)
        return self.request(url=url, kind="get", params=params)

```