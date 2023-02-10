from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class MatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source = 'curso.descricao')
    turno = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = 'curso', 'turno'
    def get_turno(self, obj):
        return obj.get_turno_display()

class AlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source = 'aluno.nome')
    turno = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['aluno', 'turno']
    def get_turno(self, obj):
        return obj.get_turno_display()
        

