from .models import Foo, Bar, Baz
from django.test import TestCase
from django.core.management import call_command

class SimpleTest(TestCase):

    def setUp(self):
        self.foo1 = Foo.objects.create(name='foo1')
        self.foo2 = Foo.objects.create(name='foo2')
        self.bar1 = Bar.objects.create(name='bar1', foo=self.foo1)
        self.bar2 = Bar.objects.create(name='bar2', foo=self.foo1)
        self.baz1 = Baz.objects.create(name='baz1')
        self.baz2 = Baz.objects.create(name='baz2')

        self.baz1.foo_set = [self.foo1, self.foo2]

        self.baz2.foo_set.add(self.foo1)

        call_command('dumpdata', indent=4)

    def testFK(self):
        self.assertIs(self.bar1.foo, self.foo1)
        self.assertIs(self.bar2.foo, self.foo1)

        self.assertSequenceEqual(self.foo1.bar_set.all(), [self.bar1, self.bar2])
        self.assertSequenceEqual(self.foo2.bar_set.all(), [])

    def testM2M1(self):
        self.assertSequenceEqual(self.foo1.baz_set.all(), [self.baz1, self.baz2])

    def testM2M2(self):
        self.assertSequenceEqual(self.baz1.foo_set.all(), [self.foo1, self.foo2])
