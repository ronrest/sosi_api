# Using

## Basic

```python
from sosi_api import BaseClient
client = BaseClient()

# -------------------------------------
# MAKE A BASIC REQUEST
# -------------------------------------
client.request("http://httpbin.org/json")

# -------------------------------------
# ADD A CUSTOM RESPONSE STATUS HANDLER
# -------------------------------------
def handle_forbidden(response, msg=None, **kwargs):
    print("You are not allowed!")
client.add_status_handlers({403: handle_forbidden})

client.request("http://httpbin.org/status/403")
#> You are not allowed!
```



## Extending

The primary focus of SoSi API is to be used as a base class, for you to extend and create your own API clients.

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


## Creating Client That Requires API Key

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
