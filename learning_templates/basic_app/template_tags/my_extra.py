from django import template

register =template.Library()
@register.filter(name='decoy')
def cut(value,arg):
    """
THis cuts value of args from string
    """
    return value.replace(arg,'')

# register.filter('decoy',cut)
