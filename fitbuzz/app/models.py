from django.db import models

class FizzBuzzRequest(models.Model):
    int1 = models.IntegerField()
    int2 = models.IntegerField()
    limit = models.IntegerField()
    str1 = models.CharField(max_length=50)
    str2 = models.CharField(max_length=50)

    def get_params_dict(self):
        return {
            "int1": self.int1,
            "int2": self.int2,
            "limit": self.limit,
            "str1": self.str1,
            "str2": self.str2
        }


class Stats(models.Model):
    request = models.OneToOneField(FizzBuzzRequest, on_delete=models.CASCADE)
    hits = models.PositiveIntegerField(default=0)
