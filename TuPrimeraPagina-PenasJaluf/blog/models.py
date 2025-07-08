from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo