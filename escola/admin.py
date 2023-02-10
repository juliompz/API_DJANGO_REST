from django.contrib import admin
from .models import Aluno, Curso, Matricula

class ListandoAlunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_per_page = 20

admin.site.register(Aluno, ListandoAlunos)


class ListandoCursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo_curso', 'descricao')
    search_fields = ('codigo_curso', 'descricao')
    list_per_page = 20

admin.site.register(Curso, ListandoCursos)

class ListandoMatricula(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'turno')
    list_display_links = ('id',)
    list_per_page = 20

admin.site.register(Matricula, ListandoMatricula)