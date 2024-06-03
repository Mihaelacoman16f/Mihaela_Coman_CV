from django.db import models


class SkinType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    dry_skin = models.BooleanField(default=False)
    oily_t_zone = models.BooleanField(default=False)
    large_pores = models.BooleanField(default=False)
    cold_feel_tight = models.BooleanField(default=False)
    cold_feel_normal = models.BooleanField(default=False)
    cream_absorption_fast = models.BooleanField(default=False)
    cream_absorption_slow = models.BooleanField(default=False)
    acne_no = models.BooleanField(default=False)
    acne_few = models.BooleanField(default=False)
    acne_many = models.BooleanField(default=False)
    acne_lot = models.BooleanField(default=False)
    irritated_skin = models.BooleanField(default=False)

    @property
    def result(self):
        return "{} {}".format(self.name, self.description)

    def __str__(self):
        return self.result
    
class SkincareRoutine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    skin_types = models.ManyToManyField(SkinType, through='RoutineSkinType')

    def __str__(self):
        return self.name

class SkincareProduct(models.Model):
    name = models.CharField(max_length=100)
    description_product = models.TextField(max_length=500, default=None)
    image_url = models.URLField(max_length=500)
    product_url = models.URLField(max_length=500)
    routine = models.ForeignKey(SkincareRoutine, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


class RoutineSkinType(models.Model):
    routine = models.ForeignKey(SkincareRoutine, on_delete=models.CASCADE)
    skin_type = models.ForeignKey(SkinType, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.routine.name} for {self.skin_type.name}"

class AboutSkinTypes(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    advantages = models.TextField()
    disadvantages = models.TextField()

    def __str__(self):
        return self.name