from django.db import models

# Create your models here.
class Paciente(models.Model):
    
    name  = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Paciente")
        verbose_name_plural = ("Pacientes")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Paciente_detail", kwargs={"pk": self.pk})
    
    
class tessue(models.Model):
    
    temperature = models.FloatField(verbose_name="temperatura")
    color = models.FloatField()
    inflammation = models.FloatField(verbose_name="Inflamación")
    name = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)
    

    class Meta:
        verbose_name = "Tejido"
        verbose_name_plural = "Tejidos"

    def __str__(self):
        return 'tempreratura: '+ str(self.temperature) +' color: '+str(self.color)

    #def get_absolute_url(self):
    #    return reverse("tablaValores_detail", kwargs={"pk": self.pk})


