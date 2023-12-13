# NOAA Climate Data Online SDK for Rhino & Grasshopper

Python 2 API for NOAA climate data API v2.

The [original repositories](https://github.com/topics/noaa-api) by _Andreas Sagen_ required `python 3.7`.
This fork target supporting for `python 2.7`, which is compitable with Rhino 7. The modified file can be found in `noaa_gh`. the alternation includes:

- Clear Python3 style type hint
- Change f-string to `str.format()`
- Replace `urllib.request` by `urllib.URLopener`
- Disable `startdate` and `enddate` rephasing because it makes the system crush.

In the same folder, there is another `noaa_example.gh` for usage reference.

## However
I suggest not to use this NOAAv2 API unless you really need it to be a RESTful competiable.
Otherwise, use v1 and parse the `.csv` by yourself. The disadvantage in v2 includes:

1. Maximun duration for each query is one year, e.g. `startdate=1990-01-01` and `enddate=1991-02-02` would be unavailable. If you want to query data for a long period, you may consider break it into multiple query and run a for-loop for it. However, there's a maximum capacity of 5 query/second for each token...

2. The server is not stable. It always fails, which is extremely annoying.

## License
This project is licensed under the `MIT`. For more details see [LICENSE](LICENSE).
