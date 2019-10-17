# coding=UTF-8

from __future__ import unicode_literals

from django.db import models

from django.contrib import staticfiles

PROD_TYPE = (
        ('plant', 'растение'),
        ('liquid', 'жидкость'),
        ('item', 'предмет'),
    )

class Order(models.Model):
    name = models.CharField(u'имя', max_length=25)
    surname = models.CharField(u'фамилия', max_length=25)
    patronymic = models.CharField(u'отчество', max_length=25)
    email = models.EmailField(u'email', max_length=30)
    adress = models.CharField(u'адрес', max_length=2000)
    index = models.IntegerField(u'индекс')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class Product(models.Model):
    name = models.CharField(u'название', max_length=50)
    description = models.CharField(u'описание', max_length=400)
    prise = models.IntegerField(u'стоимость')
    amount = models.IntegerField(u'количество')
    product_type = models.CharField(max_length=8, choices=PROD_TYPE, verbose_name = 'тип товара')
    imgsrc_min = models.ImageField(upload_to='img/',  blank=True, verbose_name='мини изобранжение')
    imgsrc_full = models.ImageField(upload_to='img/',   blank=True, verbose_name='полное изобранжение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Ordered_Product(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name = 'заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name = 'товар')
    order_prise = models.IntegerField(u'оплаченная стоимость')
    order_amount = models.IntegerField(u'заказанное количество')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'



