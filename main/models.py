from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)       # Nama produk
    description = models.TextField()              # Deskripsi produk
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Harga produk
    stock = models.IntegerField()                 # Jumlah stok produk

    def __str__(self):
        return self.name
