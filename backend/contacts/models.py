from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# TASK_VARIABLES = (
#     ('LP', 'Landing page'),
#     ('BC', 'Business card site'),
#     ('OS', 'Online store'),
#     ('EP', 'Enterprise portal'),
#     ('P', 'Portal'),
#     ('PP', 'Promo page'),
#     ('L', 'Logo creation'),
#     ('S', 'SEO'),
# )

# TASK_VARIABLES = (
#     ('LP', 'Лендинг'),
#     ('BC', 'Сайт визитка'),
#     ('OS', 'Интернет-магазин'),
#     ('EP', 'Корпоративный сайт'),
#     ('P', 'Портал'),
#     ('PP', 'Промо сайт'),
#     ('L', 'Создание логотипа'),
#     ('S', 'SEO'),
# )


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.created_at}"
