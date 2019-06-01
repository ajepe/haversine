# haversine [![Build Status](https://travis-ci.org/ajepe/haversine.svg?branch=master)](https://travis-ci.org/ajepe/haversine)

Python implementation of haversine formula to determine the great-circle distance between two points on a given 
sphere knowning their longitudes and latitudes.


### Installation
```bash
pip install  aversine
```

### Usage

```python
    from from haversine import haversine

    haversine.Haversine()
    location_a, location_b = (45.7597, 4.8422), (48.8567, 2.3508)
    haversine.distance(location_a, location_b) # => 392.2167178065958
```