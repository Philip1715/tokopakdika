from django.db import models
import uuid 
from django.contrib.auth.models import User

class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=100)       # Nama produk
    description = models.TextField()              # Deskripsi produk
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Harga produk
    stock = models.IntegerField()                 # Jumlah stok produk

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5