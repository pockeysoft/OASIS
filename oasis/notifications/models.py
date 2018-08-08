from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from oasis.users import models as user_models
from oasis.images import models as image_models

# Create your models here.
@python_2_unicode_compatible
class Notification(image_models.TimeStampedModel):
    
    TYPE_CHOICE = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow')
    )

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='creator')
    to = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='to')
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICE)
    image = models.ForeignKey(image_models.Image, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '[TYPE]: {} From: {} - To: {} Comment: {}'.format(self.notification_type, self.creator, self.to, self.comment)