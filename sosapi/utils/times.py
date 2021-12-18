import datetime
import dateutil

DESIRED_TIMEZONE = "UTC"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S %Z"

def set_timezone(dt, timezone="UTC"):
    tz = dateutil.tz.gettz(timezone)
    dt = dt.replace(tzinfo=tz)
    return dt

def ms_timestamp_to_datetime(timestamp, timezone="UTC"):
    tz = dateutil.tz.gettz(timezone)
    timestamp = float(timestamp)
    return datetime.datetime.fromtimestamp(timestamp / 1000., tz=tz)

def parse_datetime_str_to_ms_timestamp(datetime_str, timezone="UTC"):
    """
    Given a string in the format of '2021-12-05 12:50:00', it converts a
    datetime string to a timestamp in milliseconds.
    """
    tz = dateutil.tz.gettz(timezone)
    dt = dateutil.parser.parse(datetime_str)
    dt = dt.replace(tzinfo=tz)
    print(dt)
    return int(dt.timestamp() * 1000)

def convert_timearg_as_datetime(t):
    tz = dateutil.tz.gettz(DESIRED_TIMEZONE)
    if isinstance(t, datetime.datetime):
        dt = t
        if dt.tzinfo is not None:
            dt = t.replace(tzinfo=tz)
        else:
            dt = dt.astimezone(tz)
    elif isinstance(t, str):
        dt = dateutil.parser.parse(t)
        dt = dt.replace(tzinfo=tz)
    else:
        ts = float(t)
        dt = datetime.datetime.fromtimestamp(ts, tz=tz)
    return dt

def convert_timearg_as_timestamp(t):
    if isinstance(t, datetime.datetime):
        ts = int(t.timestamp() * 1000)
    elif isinstance(t, str):
        ts = parse_datetime_str_to_ms_timestamp(t, timezone=DESIRED_TIMEZONE)
    else:
        ts = int(float(t))
    return ts