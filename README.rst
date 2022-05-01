 
==========
ENC_FIELD
==========

This is a test project to simulate problem with EncryptedIntegerField from Django Fernet Encrypted Fields

As error message made by tox shows :

`
  ".tox/py310-dj40/lib/python3.10/site-packages/django/db/backends/base/operations.py", line 673, in integer_field_range
      return self.integer_field_ranges[internal_type]
  KeyError: 'TextField'
`
