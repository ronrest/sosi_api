# Basic Usage

```python
from sosi_api import BaseClient

# Create a client with no base url, but specify the full url for each request
client = BaseClient()
client.request("http://httpbin.org/json")


# Specify a base url, and then only specify the endpoint for each request
client = BaseClient("http://httpbin.org")
client.request(endpoint="/json")
```
