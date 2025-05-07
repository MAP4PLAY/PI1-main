from django.db import models

class Quadra(models.Model): 
    nome = models.CharField( 
        max_length=200, 
        verbose_name="Nome da quadra" 
    ) 
    endereco = models.TextField( 
        verbose_name="Localidade", 
        help_text="Informe o endereço no formato: Logradouro, endereço, Bairro, Cidade, Estado" 
    ) 
    estrutura_fisica = models.TextField( 
        verbose_name="Estrutura física da quadra",
         
        help_text="Descreva a estrutura física da quadra",
        blank=True,  # Permite que o campo seja deixado em branco no formulário
        null=True    # Permite que o valor seja NULL no banco de dados

    ) 
    informacoes_jogos = models.TextField( 
        verbose_name="Informações sobre os jogos", 
        help_text="Descreva os dias e horários dos jogos",
        blank=True,  # Permite que o campo seja deixado em branco no formulário
        null=True    # Permite que o valor seja NULL no banco de dados

    ) 
 
    def __str__(self): 
        return self.nome 

