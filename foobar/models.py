from django.db import models

class Foo(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

class Bar(models.Model):
    name = models.CharField(max_length=40)
    foo = models.ForeignKey(Foo)

    def __unicode__(self):
        return self.name

class Baz(models.Model):
    name = models.CharField(max_length=40)
    foo_set = models.ManyToManyField(Foo)

    def __unicode__(self):
        return self.name
