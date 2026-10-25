from django.db import models

class WatchItem(models.Model):
    TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('book', 'Book'),
    ]

    STATUS_CHOICES = [
        ('want', 'Want to Watch/Read'),
        ('done', 'Watched/Read'),
    ]

    title = models.CharField(max_length=200)
    item_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='want')
    rating = models.PositiveSmallIntegerField(null=True, blank=True)  # 1-5
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_item_type_display()})"