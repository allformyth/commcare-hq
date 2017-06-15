from django.db import models

COUCH_UUID_MAX_LEN = 50


class DeviceReportEntry(models.Model):
    xform_id = models.CharField(max_length=COUCH_UUID_MAX_LEN, db_index=True)
    i = models.IntegerField()
    msg = models.TextField()
    type = models.CharField(max_length=32)
    date = models.DateTimeField()
    server_date = models.DateTimeField(null=True, db_index=True)
    domain = models.CharField(max_length=100)
    device_id = models.CharField(max_length=COUCH_UUID_MAX_LEN, null=True)
    app_version = models.TextField(null=True)
    username = models.CharField(max_length=100, null=True)
    user_id = models.CharField(max_length=COUCH_UUID_MAX_LEN, null=True)

    class Meta:
        app_label = 'phonelog'
        unique_together = [('xform_id', 'i')]
        index_together = [
            ("domain", "date"),
            ("domain", "device_id"),
            ("domain", "username"),
            ("domain", "type"),
        ]

    def __repr__(self):
        return u"DeviceReportEntry(domain='{}', msg='{}')".format(self.domain, self.msg)


class UserErrorEntry(models.Model):
    # Information about the device log this came from
    domain = models.CharField(max_length=100, db_index=True)
    xform_id = models.CharField(max_length=COUCH_UUID_MAX_LEN, db_index=True)
    i = models.IntegerField()

    # The context around when/how this happened
    app_id = models.CharField(max_length=COUCH_UUID_MAX_LEN)
    version_number = models.IntegerField()
    date = models.DateTimeField()
    server_date = models.DateTimeField(null=True, db_index=True)
    user_id = models.CharField(max_length=COUCH_UUID_MAX_LEN, db_index=True)

    # Information about the specific error
    context_node = models.CharField(max_length=255, blank=True)
    expr = models.TextField()
    msg = models.TextField()
    session = models.TextField()
    type = models.CharField(max_length=32, db_index=True)

    class Meta:
        app_label = 'phonelog'
        unique_together = [('xform_id', 'i')]
        index_together = [
            ("domain", "app_id", "version_number"),
        ]

    def __repr__(self):
        return u"UserErrorEntry(domain='{}', msg='{}')".format(self.domain, self.msg)


class UserEntry(models.Model):
    xform_id = models.CharField(max_length=COUCH_UUID_MAX_LEN, db_index=True)
    i = models.IntegerField()
    user_id = models.CharField(max_length=COUCH_UUID_MAX_LEN)
    sync_token = models.CharField(max_length=COUCH_UUID_MAX_LEN)
    username = models.CharField(max_length=100, db_index=True)
    server_date = models.DateTimeField(null=True, db_index=True)

    class Meta:
        app_label = 'phonelog'
        unique_together = [('xform_id', 'i')]

    def __repr__(self):
        return u"UserEntry(username='{}')".format(self.username)


class ForceCloseEntry(models.Model):
    # Information about the device log this came from
    domain = models.CharField(max_length=100, db_index=True)
    xform_id = models.CharField(max_length=COUCH_UUID_MAX_LEN)

    # The context around when/how this happened
    app_id = models.CharField(max_length=COUCH_UUID_MAX_LEN, null=True)
    version_number = models.IntegerField()
    date = models.DateTimeField()
    server_date = models.DateTimeField(null=True)
    user_id = models.CharField(max_length=COUCH_UUID_MAX_LEN, null=True)

    # Information about the specific error
    type = models.CharField(max_length=32)
    msg = models.TextField()
    android_version = models.CharField(max_length=32)
    device_model = models.CharField(max_length=32)
    session_readable = models.TextField()
    session_serialized = models.TextField()

    class Meta:
        app_label = 'phonelog'
        index_together = [
            ("domain", "server_date"),
        ]

    def __repr__(self):
        return u"ForceCloseEntry(domain='{}', msg='{}')".format(self.domain, self.msg)
