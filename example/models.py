from django.db import models

class Ice_cream(models.Model):
    ice_cream_name = models.CharField(max_length=255)
    ice_cream_type = models.CharField(max_length=255)
    ice_cream_price = models.CharField(max_length=15)

    def __str__(self):
        return f"We have {self.ice_cream_name} from {self.ice_cream_type} and priced at GHS {self.ice_cream_price}"