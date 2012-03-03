from tower.models import Account
from django.contrib import admin


class AccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(Account, AccountAdmin)

