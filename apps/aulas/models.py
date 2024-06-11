from django.db import models
from django.conf import settings
from apps.authentication.models import CustomUser

class Aula(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    grupos = models.ManyToManyField('auth.Group', related_name='aulas')

    def __str__(self):
        return self.nombre

class Notificacion(models.Model):
    DIARIA = 'D'
    SEMANAL = 'S'
    MENSUAL = 'M'
    NINGUNA = 'N'
    
    PREFERENCIAS_NOTIFICACION = [
        (DIARIA, 'Diariamente'),
        (SEMANAL, 'Semanalmente'),
        (MENSUAL, 'Mensualmente'),
        (NINGUNA, 'No notificar')
    ]
    
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    preferencia = models.CharField(
        max_length=1,
        choices=PREFERENCIAS_NOTIFICACION,
        default=NINGUNA
    )

    def __str__(self):
        return f'Notificación de {self.usuario} para {self.aula}: {self.get_preferencia_display()}'