from drf_yasg import openapi

fitbuzz_response_schema = {
    "200": openapi.Response(
        description="List of Strings",
        examples={
            "application/json": ["1", "2", "fit", "4", "..."]
        }
    )
}

stats_response_schema = {
    "200": openapi.Response(
        description="Hit count of most used parameters",
        examples={
            "application/json": {
            "request_params": {
                "int1": 3,
                "int2": 5,
                "limit": 10,
                "str1": "fit",
                "str2": "buzz"
            },
            "hits": 1
            }
        }
    )
}
