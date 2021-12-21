# Extending the Base Client

## Basic

```python
from sosi_api import BaseClient

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


## API that requires API key

```python
import decouple   # pip install python-decouple
from sosi_api import BaseClient

# Look for credentials in `.env` file located in working directory
env = decouple.AutoConfig(search_path="./.env")

class MyClient(BaseClient):
    def __init__(self, key=None):
        super().__init__(
            base_url="http://www.my-website.com/api",
            headers=None,
            max_requests_per_min=60,
            response_kind="json",
        )
        self.api_key = key if key is not None else env('MY_API_KEY', cast=str)
        assert self.api_key is not None, "Missing MY_API_KEY"

    def price(self, token):
        endpoint = "/token_price"
        url = self.base_url + endpoint
        params = dict(token=token, api_key=self.api_key)
        return self.request(url=url, kind="get", params=params)

```
