



```python
def my_func(self, symbol, min_id=0, limit=1000, t1=None, t2=None):
    endpoint = "/api/v3/allOrders"
    url = self.base_url + endpoint
    params = dict(symbol=symbol, min_id=min_id)
    items = self._time_range_batched_request(url=url, params=params, kind="get", t1=t1, t2=t2, window=datetime.timedelta(days=28), limit=1000)
    return items

def my_func2(self, symbol):
    endpoint = "/api/v3/allOrders"
    url = self.base_url + endpoint
    params = dict(symbol=symbol)
    return self.request(url=url, params=params, kind="get")

```