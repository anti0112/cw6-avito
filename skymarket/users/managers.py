from django.contrib.auth.models import (
    BaseUserManager
)
# TODO здесь должен быть менеджер для модели Юзера.
# TODO Поищите эту информацию в рекомендациях к проекту
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password, last_login=None, role='user', image=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            role = 'user',
            image = image,
            last_login = last_login,          
        )
        
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, first_name, last_name, phone, password, role):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            password = password,
            role = 'admin'
        )
        user.save(using=self._db)
        return user
    