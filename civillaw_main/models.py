from django.db import models

class Cliente(models.Model):
    """ Cadastro de clientes """
    # clie_id = models.AutoField(int)
    clie_datacad = models.DateField(auto_now_add=True)
    clie_nome = models.CharField(max_length=150)
    clie_cpf = models.IntegerField

    def __str__(self):
        """ devolve uma representançao em string """
        return self.text
    
