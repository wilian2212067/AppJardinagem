from django.db import models



class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Servico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    tipo_servico = models.CharField(max_length=100)
    fotos = models.ImageField(upload_to='servico_fotos/', blank=True, null=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.tipo_servico}"