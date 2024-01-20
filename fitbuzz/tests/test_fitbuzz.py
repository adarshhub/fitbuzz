import pytest

from rest_framework.test import APIClient

client = APIClient()

# {"int1": 3, "int2": 5, "limit": 10, "str1": "fit", "str2": "buzz"}

@pytest.mark.django_db
def test_fitbuzz_request():
    payload = dict(
        int1 = 3,
        int2 = 5,
        limit = 10,
        str1 = "fit",
        str2 = "buzz"
    )

    response = client.post("/api/v1/fitbuzz", payload)

    assert response.status_code == 200

    data = response.data

    assert data.get("result") == ["1", "2", "fit", "4", "buzz", "fit", "7", "8", "fit", "buzz"]

    