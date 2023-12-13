import sys
import datetime
import json
import urllib

class NOAAAPI:
    """Class for interfacing with NOAA climate data API

    :param key: Access token from NOAA
    :type key: str
    """

    def __init__(self, key):
        """
        :type key: str
        :param key: Access token from NOAA
        """
        self._api_header = {
            "token": key
        }
        self._host = "https://www.ncdc.noaa.gov/cdo-web/api/v2/"

    def get_datasets(
        self,
        dataset_id = None,
        data_type_id = None,
        location_id = None,
        station_id = None,
        start_date = None,
        end_date = None,
        sort_field = None,
        sort_order = "asc",
        limit = 25,
        offset = 0
    ):
        """Get list of available datasets in CDO or info on a specific dataset

        :param dataset_id: Identification to dataset in CDO, defaults to None
        :type dataset_id: str, optional
        :param data_type_id: Identification to datatype(s) in CDO, defaults to None
        :type data_type_id: str, list, tuple, optional
        :param location_id: Identification to location(s) in CDO, defaults to None
        :type location_id: str, list, tuple, optional
        :param station_id: Identification to station(s) in CDO, defaults to None
        :type station_id: str, list, tuple, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional
        :raises TypeError: If dataset_id is not string or None, raises an error.

        :return: Return a object with data from response
        :rtype: dict
        """
        if not isinstance(dataset_id, str) and dataset_id is not None:
            raise TypeError("dataset_id should be string's")

        endpoint = "datasets"
        if dataset_id is not None:
            endpoint += "/{dataset_id}".format(dataset_id=dataset_id)

        return self._call_api(
            endpoint=endpoint,
            data_type_id=data_type_id,
            end_date=end_date,
            limit=limit,
            location_id=location_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date,
            station_id=station_id
        )

    def get_data_categories(
        self,
        category_id = None,
        dataset_id = None,
        location_id = None,
        station_id = None,
        start_date = None,
        end_date = None,
        sort_field = None,
        sort_order = "asc",
        limit = 25,
        offset = 0
    ):
        """Get list of available categories in CDO or info on a specific category

        :param category_id: Identification to category in CDO, defaults to None
        :type category_id: str, optional
        :param dataset_id: Identification to dataset(s) in CDO, defaults to None
        :type dataset_id: str, list, tuple, optional
        :param location_id: Identification to location(s) in CDO, defaults to None
        :type location_id: str, list, tuple, optional
        :param station_id: Identification to station(s) in CDO, defaults to None
        :type station_id: str, list, tuple, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional

        :raises TypeError: If category_id is not string or None, raises an error.

        :return: Return a object with data from response
        :rtype: dict
        """
        if not isinstance(category_id, str) and category_id is not None:
            raise TypeError("category_id should be string's")

        endpoint = "datacategories"
        if category_id is not None:
            endpoint += "/{category_id}".format(category_id=category_id)

        return self._call_api(
            endpoint=endpoint,
            dataset_id=dataset_id,
            end_date=end_date,
            limit=limit,
            location_id=location_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date,
            station_id=station_id
        )

    def get_data_types(
        self,
        type_id = None,
        dataset_id = None,
        location_id = None,
        station_id = None,
        data_category_id = None,
        start_date = None,
        end_date = None,
        sort_field = None,
        sort_order = "asc",
        limit = 25,
        offset = 0
    ):
        """Get list of available datatypes in CDO or info on a specific datatype

        :param type_id: Identification to type in CDO, defaults to None
        :type type_id: str, optional
        :param dataset_id: Identification to dataset(s) in CDO, defaults to None
        :type dataset_id: str, list, tuple, optional
        :param location_id: Identification to location(s) in CDO, defaults to None
        :type location_id: str, list, tuple, optional
        :param station_id: Identification to station(s) in CDO, defaults to None
        :type station_id: str, list, tuple, optional
        :param data_category_id: Identification to data category in CDO, defaults to None
        :type data_category_id: str, list, tuple, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional

        :raises TypeError: If type_id is not string or None, raises an error.

        :return: Return a object with data from response
        :rtype: dict
        """
        if not isinstance(type_id, str) and type_id is not None:
            raise TypeError("type_id should be string's")

        endpoint = "datatypes"
        if type_id is not None:
            endpoint += "/{type_id}".format(type_id=type_id)

        return self._call_api(
            endpoint=endpoint,
            dataset_id=dataset_id,
            end_date=end_date,
            limit=limit,
            location_id=location_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date,
            station_id=station_id,
            data_category_id=data_category_id
        )

    def get_location_categories(
        self,
        location_category_id = None,
        dataset_id = None,
        start_date = None,
        end_date = None,
        sort_field = None,
        sort_order = "asc",
        limit = 25,
        offset = 0
    ):
        """Get list of available location categories in CDO or info on a specific location category

        :param location_category_id: Identification to location category in CDO, defaults to None
        :type location_category_id: str, optional
        :param dataset_id: Identification to dataset(s) in CDO, defaults to None
        :type dataset_id: str, list, tuple, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional

        :raises TypeError: If location_category_id is not string or None, raises an error.

        :return: Return a object with data from response
        :rtype: dict
        """
        if not isinstance(location_category_id,
                          str) and location_category_id is not None:
            raise TypeError("location_category_id should be string's")

        endpoint = "locationcategories"
        if location_category_id is not None:
            endpoint += "/{location_category_id}".format(
                location_category_id=location_category_id)

        return self._call_api(
            endpoint=endpoint,
            dataset_id=dataset_id,
            end_date=end_date,
            limit=limit,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date
        )

    def get_locations(
        self,
        location_id = None,
        dataset_id = None,
        location_category_id = None,
        data_category_id = None,
        start_date = None,
        end_date = None,
        sort_field = None,
        sort_order = "asc",
        limit = 25,
        offset = 0
    ):
        """Get list of available locations in CDO or info on a specific location

        :param location_id: Identification to location in CDO, defaults to None
        :type location_id: str, optional
        :param dataset_id: Identification to dataset(s) in CDO, defaults to None
        :type dataset_id: str, list, tuple, optional
        :param location_category_id: Identification to location category in CDO, defaults to None
        :type location_category_id: str, list, tuple, optional
        :param data_category_id: Identification to data category in CDO, defaults to None
        :type data_category_id: str, list, tuple, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional

        :raises TypeError: If location_id is not string or None, raises an error.

        :return: Return a object with data from response
        :rtype: dict
        """
        if not isinstance(location_id, str) and location_id is not None:
            raise TypeError("location_id should be string's")

        endpoint = "locations"
        if location_id is not None:
            endpoint += "/{location_id}".format(location_id=location_id)

        return self._call_api(
            endpoint=endpoint,
            data_category_id=data_category_id,
            dataset_id=dataset_id,
            end_date=end_date,
            limit=limit,
            location_category_id=location_category_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date
        )

    def get_stations(
        self,
        station_id = None,
        dataset_id = None,
        location_id = None,
        data_category_id = None,
        data_type_id = None,
        extent = None,
        start_date = None,
        end_date = None,
        sort_field = None,
        sort_order = "asc",
        limit = 25,
        offset = 0
    ):
        """Get list of available stations in CDO or info on a specific station

        :param station_id: Identification to station in CDO, defaults to None
        :type station_id: str, optional
        :param dataset_id: Identification to dataset(s) in CDO, defaults to None
        :type dataset_id: str, list, tuple, optional
        :param location_id: Identification to location(s) in CDO, defaults to None
        :type location_id: str, list, tuple, optional
        :param data_category_id: Identification to data category in CDO, defaults to None
        :type data_category_id: str, list, tuple, optional
        :param data_type_id: Identification to datatype(s) in CDO, defaults to None
        :type data_type_id: str, list, tuple, optional
        :param extent: Desired geographical extent for search in CDO, defaults to None
        :type extent: str, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional

        :raises TypeError: If station_id is not string or None, raises an error.

        :return: Return a object with data from response
        :rtype: dict
        """
        if not isinstance(station_id, str) and station_id is not None:
            raise TypeError("IDs should be string's")

        endpoint = "stations"
        if station_id is not None:
            endpoint += "/{station_id}".format(station_id=station_id)

        return self._call_api(
            endpoint=endpoint,
            data_category_id=data_category_id,
            dataset_id=dataset_id,
            data_type_id=data_type_id,
            end_date=end_date,
            extent=extent,
            limit=limit,
            start_date=start_date,
            location_id=location_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order
        )

    def get_data(
        self,
        dataset_id,
        start_date,
        end_date,
        data_type_id = None,
        location_id = None,
        station_id = None,
        units = "metric",
        sort_field = None,
        sort_order = "asc",
        limit = 25,
        offset = 0,
        include_metadata = False
    ):
        """Get available data in CDO

        :param dataset_id: Identification to dataset in CDO
        :type dataset_id: str, datetime.datetime
        :param start_date: Filter from time in ISO formatted date
        :type start_date: str, datetime.datetime
        :param end_date: Filter to time in ISO formatted date
        :type end_date: str, datetime.datetime
        :param data_type_id: Identification to datatype(s) in CDO, defaults to None
        :type data_type_id: str, list, tuple, optional
        :param location_id: Identification to location(s) in CDO, defaults to None
        :type location_id: str, list, tuple, optional
        :param station_id: Identification to station(s) in CDO, defaults to None
        :type station_id: str, list, tuple, optional
        :param units: Data will be scaled and converted to the specified units, defaults to "metric"
        :type units: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional
        :param include_metadata: Include or exclude metadata from CDO, defaults to False
        :type include_metadata: bool, optional

        :return: Return a object with data from response
        :rtype: dict
        """

        return self._call_api(
            endpoint="data",
            data_type_id=data_type_id,
            dataset_id=dataset_id,
            end_date=end_date,
            include_metadata=include_metadata,
            limit=limit,
            location_id=location_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date,
            station_id=station_id,
            units=units,
            _full_time=False
        )

    def _call_api(
        self,
        endpoint,
        dataset_id = None,
        data_type_id = None,
        data_category_id = None,
        start_date = None,
        end_date = None,
        extent = None,
        include_metadata = False,
        limit = 25,
        location_id = None,
        location_category_id = None,
        offset = 0,
        sort_field = None,
        sort_order = "asc",
        station_id = None,
        units = "metric",
        _full_time = False
    ):
        _ids_1 = [
            dataset_id,
            data_type_id,
            location_id,
            station_id,
            data_category_id,
            location_category_id
        ]

        for _id in _ids_1:
            if not isinstance(_id, (str, list, tuple)) and _id is not None:
                raise TypeError("{_id} should be string or array type value".format(_id=_id))

            if isinstance(_id, (list, tuple)):
                for value in _id:
                    if not isinstance(value, str):
                        raise TypeError("All values in {_id} should be string type values".format(_id=_id))

        if not isinstance(extent, str) and extent is not None:
            raise TypeError("Extent has to be a string type value")

        if not isinstance(include_metadata, bool):
            raise TypeError("include_metadata should be a boolean type value")

        if not isinstance(limit, int):
            raise TypeError("limit should be an integer type value")

        if limit > 1000:
            raise ValueError(
                "Maximum limit is 1000. Choose a value between 0 and 1000")

        if not isinstance(offset, int):
            raise TypeError("offset should be an integer type value")

        if not isinstance(sort_field, str) and sort_field is not None:
            raise TypeError("sort_field should be an string type value")

        if sort_field not in [None, "id", "name",
                              "mindate", "maxdate", "datacoverage"]:
            raise ValueError("{sort_field} is not an accepted value".format(
                sort_field=sort_field))

        if not isinstance(sort_order, str):
            raise TypeError("sort_order should be an string type value")

        if sort_order not in ["asc", "desc"]:
            raise ValueError("{sort_field} is not an accepted value".format(
                sort_field=sort_order))

        if not isinstance(units, str):
            raise TypeError("units should be an string type value")

        if units not in ["standard", "metric"]:
            raise ValueError("{units} is not an accepted value".format(
                units=units))

        if isinstance(dataset_id, (list, tuple)):
            dataset_id = "&".join(dataset_id)

        if isinstance(data_type_id, (list, tuple)):
            data_type_id = "&".join(data_type_id)

        if isinstance(location_id, (list, tuple)):
            location_id = "&".join(location_id)

        if isinstance(station_id, (list, tuple)):
            station_id = "&".join(station_id)

        data = {
            "datacategoryid": data_category_id,
            "datasetid": dataset_id,
            "datatypeid": data_type_id,
            "enddate": end_date,
            "extent": extent,
            "includemetadata": include_metadata,
            "limit": limit,
            "locationcategoryid": location_category_id,
            "locationid": location_id,
            "offset": offset,
            "sortfield": sort_field,
            "sortorder": sort_order,
            "startdate": start_date,
            "stationid": station_id,
            "units": units
        }

        data = {key: value for key, value in data.items() if value is not None}

        url = self._host + endpoint
        params = urllib.urlencode(data)
        
        urlOpener = urllib.URLopener()
        for k, v in self._api_header.items():
            urlOpener.addheader(k, v)
            
        response = urlOpener.open("?".join([url, params]).replace("%26", "&"))
        
        return json.loads(response.read())

if __name__ == "__main__":
    noaaobj = NOAAAPI("HKuVxxFuvyCdInqZJjGnQgYSHCNZcZLv")
    
   print(noaaobj.get_data(
       dataset_id="GSOM",
       start_date="2012-01-03",
       end_date="2012-09-10")
   )
    
    sys.modules["NOAAAPI"] = NOAAAPI
    print("Successfully Initialized")