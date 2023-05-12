from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def _str_(self):
        return self.descricao

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50)

    def _str_(self):
        return self.nome.upper()

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def _str_(self):
        return self.descricao

class Cor(models.Model):
    descricao = models.CharField(max_length=100)
    
    def _str_(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Cores"


class Modelo(models.Model):
    descricao = models.CharField(max_length=100)
    
    def _str_(self):
        return f"{self.descricao} ({self.id})"

    class Meta:
        verbose_name_plural = "Modelos"

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    ano = models.IntegerField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10,decimal_places=2, null=True, default=0)
    modelo= models.CharField(max_length=50)

    def _str_(self):
        return f"{self.marca.nome},  {self.ano}, {self.cor.descricao},  {self.modelo}"
