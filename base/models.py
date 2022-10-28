from django.db import models
# Create your models here.

class Doctor(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  password = models.CharField(max_length=20)
  
  created_at = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{}'.format(self.name) 

class Patient(models.Model):
  name = models.CharField(max_length=200)
  phone = models.CharField(max_length=13)
  address = models.CharField(max_length=200)
  number = models.CharField(max_length=4)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2)
  country = models.CharField(max_length=50)
  cep = models.CharField(max_length=9)

  created_at = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{}'.format(self.name) 

class Consultations(models.Model):
  date = models.DateTimeField(null=False)
  description = models.TextField(max_length=500)
  
  PROGRESS_STATUS = (
    ('A Confirmar','A Confirmar'),
    ('Confirmado', 'Confirmado'),
    ('Finalizado','Finalizado')
  )
  
  status = models.CharField(max_length=15, choices=PROGRESS_STATUS, default='A Confirmar')
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

  created = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(auto_now=True)

  def __str__(self):
        id_pretty = "Consulta para {} em {} com o medico {}".format(
            self.patient, self.date, self.doctor)
        return id_pretty