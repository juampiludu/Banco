from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CuentaManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, born_date, phone, dni, direction, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have an first name")
        if not last_name:
            raise ValueError("User must have an last name")
        if not born_date:
            raise ValueError("User must have an born date")
        if not phone:
            raise ValueError("User must have an phone")
        if not dni:
            raise ValueError("User must have an dni")
        if not direction:
            raise ValueError("User must have an direction")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            born_date = born_date,
            phone = phone,
            dni = dni,
            direction = direction,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, born_date, phone, dni, direction, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            born_date = born_date,
            phone = phone,
            dni = dni,
            direction = direction,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class Cuenta(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, unique=True)
    born_date = models.DateField(auto_now=False)
    phone = models.CharField(max_length=14)
    dni = models.CharField(max_length=8)
    direction = models.CharField(max_length=140)
    date_joined = models.DateField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'born_date', 'phone', 'dni', 'direction',]

    objects = CuentaManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
