from django.db import models
from django.urls import reverse


class Products(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Опсание')
    price = models.IntegerField(verbose_name='Цена', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновленно')
    photo = models.ImageField(blank=True, upload_to='photos/photos_products/%Y/%m/%d', verbose_name='Иконка')
    is_published = models.BooleanField(default=False, verbose_name='Опубликованно')
    age = models.DateField(verbose_name='Возраст')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Катекогрия')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']


class ImageProducts(models.Model):
    photos = models.ImageField(blank=True, upload_to='photos/photos_products/%Y/%m/%d', null=True, verbose_name='Фотография')
    photosmin = models.ImageField(blank=True, upload_to='photos/photos_products/%Y/%m/%d', null=True, verbose_name='Мини фотография')
    contact = models.ForeignKey('Products', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = "Фотография товара"
        verbose_name_plural = "Фотографии товаров"

    def __str__(self):
        return self.contact.title


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование катекогрии')
    photo = models.ImageField(blank=True, upload_to='photos/interface/%Y/%m/%d')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Evaluations(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    contact = models.CharField(max_length=150, verbose_name='Контакт')
    description = models.TextField(verbose_name='Опсание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар клиента'
        verbose_name_plural = 'Товары клиентов'
        ordering = ['-created_at']


class ImageUsers(models.Model):
    photo = models.ImageField(blank=True, upload_to='photos/photos_users/%Y/%m/%d', null=True, verbose_name='Фотография')
    contact = models.ForeignKey('Evaluations', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фотография пользователя"
        verbose_name_plural = "Фотографии пользователей"

    def __str__(self):
        return self.photo.name


class TextSite(models.Model):
    header = models.CharField(max_length=150, verbose_name='Загаловок')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Текста на сайта'
        verbose_name_plural = 'Текст на сайте'
        ordering = ['header']