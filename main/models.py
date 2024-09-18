from django.db import models
import uuid 
class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=100)       # Nama produk
    description = models.TextField()              # Deskripsi produk
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Harga produk
    stock = models.IntegerField()                 # Jumlah stok produk

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5