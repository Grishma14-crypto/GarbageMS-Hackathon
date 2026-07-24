from django.db import models

class WasteReport(models.Model):
    WASTE_TYPES = [
        ('plastic', 'Plastic'),
        ('paper', 'Paper'),
        ('glass', 'Glass'),
        ('metal', 'Metal'),
        ('organic', 'Organic'),
        ('mixed', 'Mixed Waste'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPES)
    quantity = models.PositiveIntegerField(help_text="Estimated quantity in kilograms")
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    image = models.ImageField(upload_to="waste_reports/")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CleanupTask(models.Model):
    report = models.ForeignKey(WasteReport, on_delete=models.CASCADE)
    supervisor_name = models.CharField(max_length=100)
    scheduled_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task for {self.report.title}"