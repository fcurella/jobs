from django.db import models
from sortedm2m.fields import SortedManyToManyField
import datetime
import uuid
import hmac

try:
    from hashlib import sha1
except ImportError:
    import sha
    sha1 = sha.sha


class NamedModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class ContentModel(NamedModel):
    content = models.TextField()

    class Meta:
        abstract = True


class Employer(NamedModel):
    pass


class ApplicationPage(ContentModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    attachment = models.FileField(upload_to="attachments/pages/", blank=True)

    def __unicode__(self):
        return self.name


class Application(NamedModel):
    title = models.CharField(max_length=255)
    employer = models.ForeignKey(Employer)
    pages = SortedManyToManyField(ApplicationPage)
    key = models.CharField(max_length=256, blank=True)
    attachment = models.FileField(upload_to="attachments/applications/", blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('application_detail', (), {
                'key': self.key
            })

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()

        return super(Application, self).save(*args, **kwargs)

    def generate_key(self):
        # Get a random UUID.
        new_uuid = uuid.uuid4()
        # Hmac that beast.
        return hmac.new(str(new_uuid), digestmod=sha1).hexdigest()


class GenericContent(ContentModel):
    pass


class WorkExperience(ContentModel):
    start_date = models.DateField(default=datetime.datetime.today)
    end_date = models.DateField(blank=True, null=True, default=datetime.datetime.today)

    class Meta:
        ordering = ('-start_date',)

    def __unicode__(self):
        return "%s - %s: %s" % (self.start_date.strftime("%Y"), (self.end_date and self.end_date.strftime("%Y") or u"present"), self.content)


class Study(ContentModel):
    completed = models.DateField(default=datetime.datetime.today)

    class Meta:
        verbose_name_plural = 'studies'
        ordering = ('-completed',)


class Reference(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __unicode__(self):
        return self.full_name


class Skill(ContentModel):
    pass


class Link(NamedModel):
    url = models.URLField(blank=True)
    text = models.CharField(max_length=100)
    network = models.CharField(blank=True, max_length=100)

    def __unicode__(self):
        return self.url
