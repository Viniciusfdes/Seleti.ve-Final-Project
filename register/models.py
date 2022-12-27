from django.db import models

class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia

class Nichos(models.Model):
    nicho = models.CharField(max_length=40)

    def __str__(self):
        return self.nicho

class Empresa(models.Model):
    logo = models.ImageField(upload_to="logo_empresa")
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=18)
    tecnologias = models.ManyToManyField(Tecnologias)
    endereco = models.CharField(max_length=60)
    nicho_mercado = models.ForeignKey(Nichos, null=True , on_delete=models.SET_NULL)
    caracteristica_empresa = models.TextField()

    def __str__(self) -> str:
        return self.nome

    def qtd_vagas(self):
        return Vagas.objects.filter(empresa__id=self.id).count()

class Vagas(models.Model):
    choices_experiencia = (
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )
    
    empresa = models.ForeignKey(Empresa, null=True , on_delete=models.SET_NULL)
    email = models.EmailField(null=True)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(Tecnologias, related_name='estudar')

    def __str__(self):
        return self.titulo