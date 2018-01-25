from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Lens(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.CharField(_('description'), max_length=255, blank=True)
    full = models.ImageField(_('full'), upload_to='lens/%Y/%m/%d/')
    thumb = ImageSpecField(source='full',
                           processors=[ResizeToFill(360,225)],
                           format='JPEG',
                           options={'quality': 90})
    created = models.DateTimeField(_('creation time'),auto_now_add=True)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.name 