from menu.models import MenuItem, Menu
from django import template
import logging

register = template.Library()
logger = logging.getLogger(__name__)


def set_active_branch_flags(root_menu_items, active_ids):
    def annotate(item):
        item.is_in_active_branch = item.id in active_ids
        for child in item.children_list:
            annotate(child)
    for item in root_menu_items:
        annotate(item)


def get_active_branch(item):
    branch = []
    while item:
        branch.insert(0, item)
        item = item.parent
    return branch


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    active_item = None
    active_branch = []
    current_path = context['request'].path
    root_menu_items = []
    active_ids = []

    try:
        all_items = list(MenuItem.objects.select_related('parent', 'menu').filter(menu__name=menu_name))

        items_by_parent = {}
        for item in all_items:
            if item.parent_id not in items_by_parent:
                items_by_parent[item.parent_id] = []
            items_by_parent[item.parent_id].append(item)

        for item in all_items:
            item.children_list = items_by_parent.get(item.id, [])

        root_menu_items = items_by_parent.get(None, [])

        for item in all_items:
            print(f"[DEBUG] {item.name} → {item.get_absolute_url()} vs {current_path}")
            if item.get_absolute_url() == current_path:
                print(f"[MATCH] Active item: {item.name}")
                active_item = item
                break

        if active_item:
            active_branch = get_active_branch(active_item)
            active_ids = [item.id for item in active_branch]
        set_active_branch_flags(root_menu_items, active_ids)

    except Menu.DoesNotExist as e:
        logger.error(f"Menu with name '{menu_name}' does not exist: {e}")
        raise

    return {
        "root_menu_items": root_menu_items,
        "active_branch": [item.id for item in active_branch],
        "current_path": current_path,
        "menu_name": menu_name,
    }
