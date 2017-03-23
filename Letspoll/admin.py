from django.contrib import admin
from Letspoll.models import Question, Vote

class VoteInline(admin.TabularInline):
 model = Vote
 extra = 3


class QuestionAdmin(admin.ModelAdmin):
 fieldsets = [
  (None, {'fields': ['querry']}),
  ('Date info', {'fields':['date']}),
 ]
 inlines = [VoteInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Vote)

