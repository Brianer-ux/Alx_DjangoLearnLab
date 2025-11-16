# LibraryProject/bookshelf/signals.py
from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission

APP_LABEL = "bookshelf"  # app label that contains the Book model
PERM_CODENAMES = ["can_view", "can_create", "can_edit", "can_delete"]

@receiver(post_migrate)
def create_groups_and_assign_perms(sender, **kwargs):
    # We run globally after migrations — only act when our app's permissions exist
    # (This avoids creating groups before migrations ran)
    # Check whether the Book model content type and permissions are present
    try:
        # get Permission objects for our app by codename
        perms = Permission.objects.filter(content_type__app_label=APP_LABEL, codename__in=PERM_CODENAMES)
        if not perms.exists():
            return  # permissions not yet ready for this app
    except Exception:
        return

    # Create groups
    editors, _ = Group.objects.get_or_create(name="Editors")
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    admins, _ = Group.objects.get_or_create(name="Admins")

    # Map codename -> Permission object
    perm_map = {p.codename: p for p in perms}

    # Assign permissions:
    # Viewers -> can_view
    if "can_view" in perm_map:
        viewers.permissions.add(perm_map["can_view"])

    # Editors -> can_create, can_edit, can_view
    for cname in ("can_create", "can_edit", "can_view"):
        if cname in perm_map:
            editors.permissions.add(perm_map[cname])

    # Admins -> all perms
    for p in perm_map.values():
        admins.permissions.add(p)
