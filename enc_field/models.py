from django.db import models

from encrypted_fields.fields import EncryptedIntegerField, EncryptedCharField

class EncFields(models.Model):
  # enc_int = EncryptedIntegerField(default=0, blank=True)
  enc_char = EncryptedCharField(max_length=10, default='test', blank=True)