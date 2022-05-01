from django.test import TestCase

from .models import EncFields


class Test_EncFields(TestCase):
  def setUp(self):
    enc_obj = EncFields.objects.create()

  def test_nothing(self):
      self.assertEqual(1,1)