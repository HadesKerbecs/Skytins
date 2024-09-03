from django.db import models

class Cliente(models.Model):
    codigo = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    ip = models.CharField(max_length=15)
    cnpj = models.CharField(max_length=18)
    qt_usuarios = models.IntegerField()
    grupo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
