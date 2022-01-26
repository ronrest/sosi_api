# Status Handlers

Status handlers are functions that allow for custom behaviour when a reponse is received with a particular HTTP response code (eg. `404`).


## Argument Signature

All status handler functions should have the following arguments signature:

```python
def handle_something(response, msg=None, **kwargs):
    ...
```

```bash
response    # The raw response object from requests library
msg         # The parsed mesage extracted from the response object. 
            # Eg, using response.json() or response.text()
**kwargs    # To future-proof the handler function, since aditional arguments 
            # might be passed to it in the future.
```

## Examples

Suppose there is an API that assigns the following status codes: 

- `434`
  - You are making a bit too many requests per second.
  - But it is just a soft rate-limit.
  - You are advised to slow down the API calls before you reach the hard rate-limit.
- `429`
  - You have made too many requests in the last minute.
  - This is a hard limit.
  - If you continue violating this rate limit you will be blocked.
- `435`
  - You have been blocked.
  - Because you have continually violated the hard limit.



```python
import time
import requests

def handle_soft_limit(response, msg=None, **kwargs):
    """
    Return the extracted message, but pause for a little bit to prevent 
    subsequent requests from being made too quickly.
    """
    print("WARNING: soft limit reached. Pausing for a second.")
    time.sleep(1)
    return msg

def handle_hard_limit(response, msg=None, **kwargs):
    raise requests.HTTPError("You have reached the hard limit.")

def handle_blocked(response, msg=None, **kwargs):
    raise requests.HTTPError("You have been blocked.")


# Create client and assign status handlers
status_handlers = {
    434: handle_soft_limit,
    429: handle_hard_limit,
    435: handle_blocked,
}
client = BaseClient(status_handlers=status_handlers)
```

