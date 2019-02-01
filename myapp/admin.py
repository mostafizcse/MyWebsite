from django.contrib import admin
from .models import author, category, article, Logo, Team, Reviewlist, slider, Featuretitle, Featurelist, Contact, Reviewstitle, Post, Events, Requirments, Create_menu, Example, TeamTital, About_us, Email_stor, Address
# Register your models her
class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","details"]
    class Meta:
        Model=author
admin.site.register(author, authorModel)

admin.site.register(article)

#class categoryModel(admin.ModelAdmin):
#  list_display = ["__str__"]
#   search_fields = ["__str__"]
#    list_per_page = 10
 #   class Meta:
 #       Model=category
admin.site.register(category)

admin.site.register(Logo)
admin.site.register(Team)
admin.site.register(Reviewlist)
admin.site.register(Reviewstitle)
admin.site.register(slider)
admin.site.register(Featuretitle)
admin.site.register(Featurelist)
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Events)
admin.site.register(Requirments)
admin.site.register(Create_menu)
admin.site.register(Example)
admin.site.register(TeamTital)
admin.site.register(About_us)
admin.site.register(Email_stor)
admin.site.register(Address)









