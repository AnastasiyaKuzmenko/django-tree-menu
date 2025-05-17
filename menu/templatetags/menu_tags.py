from menu.models import MenuItem, Menu
from django import template

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def show_top_menu(context):
    try:
        menu = Menu.objects.get(name="органы")
        menu_items = menu.items.filter(parent=None)
    except Menu.DoesNotExist:
        menu_items = []
 #   menu = Menu.objects.get(name="Органы")
  #  menu_items = MenuItem.objects.all()
    return {
        "menu_items": menu_items,
    }

