from django import template
register = template.Library()

@register.filter(name="addSB")
def add_sb(value):
    return "{} SB".format(value)
