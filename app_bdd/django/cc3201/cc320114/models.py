# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppKpop(models.Model):
    id = models.IntegerField(primary_key=True)
    id_parent = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    kname = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    name_aka = models.CharField(max_length=255)
    vtype = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    vlink = models.CharField(max_length=255)
    id_artist = models.IntegerField()
    id_original_artist = models.IntegerField()
    releasedate = models.DateField()
    publishedon = models.DateTimeField()
    views = models.BigIntegerField()
    likes = models.BigIntegerField()
    dislikes = models.BigIntegerField()
    lastupdate = models.DateField()
    recentviews = models.BigIntegerField()
    recentlikes = models.BigIntegerField()
    awards = models.IntegerField()
    regionlocked = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'app_kpop'


class AppKpopCompany(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_kpop_company'


class AppKpopGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    is_collab = models.CharField(max_length=1)
    name = models.CharField(max_length=255)
    kname = models.CharField(max_length=255)
    previous_name = models.CharField(max_length=255)
    previous_kname = models.CharField(max_length=255)
    fname = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    id_company = models.IntegerField()
    members = models.CharField(max_length=6)
    issolo = models.CharField(max_length=1)
    id_parentgroup = models.IntegerField()
    formation = models.IntegerField(blank=True, null=True)
    disband = models.IntegerField(blank=True, null=True)
    social = models.CharField(max_length=512, blank=True, null=True)
    id_debut = models.IntegerField(blank=True, null=True)
    debut_date = models.DateField(blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    fanclub = models.CharField(max_length=255, blank=True, null=True)
    miak = models.IntegerField()
    miak_level = models.CharField(max_length=8)
    sales = models.IntegerField()
    gaondigital_times = models.IntegerField()
    gaondigital_firsts = models.IntegerField()
    yawards = models.CharField(max_length=255, blank=True, null=True)
    yawards_total = models.IntegerField()
    yt_followers = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_kpop_group'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Prueba1(models.Model):
    dato1 = models.CharField(max_length=255, blank=True, null=True)
    dato2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prueba1'


class Prueba2(models.Model):
    dato1 = models.CharField(max_length=255, blank=True, null=True)
    dato2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prueba2'
