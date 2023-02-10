from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, MatriculasAlunoSerializer, AlunosMatriculadosSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset =  Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    '''Exibindo todos cursos'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class MatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    serializer_class = MatriculasAlunoSerializer

class AlunosMatriculados(generics.ListAPIView):
    """Listando alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = AlunosMatriculadosSerializer