from django.db import models
from django.urls import reverse


class Category(models.Model):
        cat_id=models.AutoField(primary_key=True)
        title=models.CharField(max_length=64)
        description = models.CharField(max_length=100)
        url_slug=models.CharField(max_length=255)
        thumbnail=models.FileField()
        created_at=models.DateTimeField(auto_now_add=True)

        @staticmethod
        def get_all_category(self):
                return Category.objects.all()
        
        def __str__(self):
                return self.title
        
class SubCategories(models.Model):
        id=models.AutoField(primary_key=True)
        category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
        title=models.CharField(max_length=255)
        url_slug=models.CharField(max_length=255)
        thumbnail=models.FileField()
        description=models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)

        def get_absolute_url(self):
                return reverse("sub_category_list")

class Product(models.Model):
        id=models.AutoField(primary_key=True)
        url_slug=models.CharField(max_length=255)
        subcategories_id=models.ForeignKey(SubCategories,on_delete=models.CASCADE)
        product_name=models.CharField(max_length=255)
        brand=models.CharField(max_length=255)
        product_max_price=models.CharField(max_length=255)
        product_discount_price=models.CharField(max_length=255)
        product_description=models.TextField()
        product_long_description=models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)
        in_stock_total=models.IntegerField(default=1)
   
    

