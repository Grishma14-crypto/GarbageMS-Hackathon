STATUS_CHOICES = [
    ("pending", "Pending"),
    ("assigned", "Assigned"),
    ("completed", "Completed"),
]

status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default="pending"
)