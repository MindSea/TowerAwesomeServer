from tower.models import Account, World
from django.contrib import admin


class AccountAdmin(admin.ModelAdmin):
    pass

class WorldAdmin(admin.ModelAdmin):
    pass


admin.site.register(Account, AccountAdmin)
admin.site.register(World, WorldAdmin)
