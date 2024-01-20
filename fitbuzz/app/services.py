from . import models as app_models

def create_fitbuzz_request(data) -> list:
    int1, int2, limit, str1, str2 = data.values()
    
    result = [
        (f"{str1}" if num % int1 == 0 else "") +
        (f"{str2}" if num % int2 == 0 else "") +
        (str(num) if (num % int1 and num % int2) else "")
        for num in range(1, limit+1)
    ]

    fitbuzzrequest, created = app_models.FizzBuzzRequest.objects.get_or_create(int1=int1, int2=int2, limit=limit, str1=str1, str2=str2)
    
    stats, created = app_models.Stats.objects.get_or_create(request=fitbuzzrequest)
    stats.hits += 1
    stats.save()

    return result


def get_most_used_request() -> "Stats":
    return app_models.Stats.objects.first()