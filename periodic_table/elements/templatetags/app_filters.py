from django import template
import re

register = template.Library()


@register.filter(name="get_pos_string")
def get_pos_string(value):
    coordinatePos = str(value * 60)
    return coordinatePos


@register.filter(name="classify_category")
def classify_category(value):
    str = re.sub(r'\s+', '-', value)
    str = str.lower()
    return str


@register.filter(name="check_empty")
def check_empty(value):
    if not value:
        value = "Unknown"
    return value
