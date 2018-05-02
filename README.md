# GreenTime

GreenTime is a timestamp tool for the fast cast, you can use to cast in Python’s format which from Javascript timestamp format, and get middle night timestamp by other time zones, too.

  - Easy cast
  - Calculate by hour, minute or second

#### Requirements

GreenTime requires Python 3.6.x or >= 3.3 version.

#### Examples

simple
```sh

from green_time import GreenTime

green_time = GreenTime(gtime=1514736000) # general format

print(green_time.gtime())
# Out 1514736000

print(green_time.gtime(take_k=True) # other format, e.g. javascript
# Out 1514736000000

```

calculate
```sh

tomorrow = green_time.after(hour=24)

print(green_time.year(), green_time.month(), green_time.day())
# Out 2018 1 1

print(tomorrow.year(), green_time.month(), green_time.day())
# Out 2018 1 2

green_time.plus(hour=48) # it will change obj default time

print(green_time.year(), green_time.month(), green_time.day())
# Out 2018 1 3

```

License
----

GreenTime is under the MIT License. See LICENSE for more information.
