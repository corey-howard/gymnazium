from django import template

""" Calculates the subtotal by multiplying quantity by price """
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
