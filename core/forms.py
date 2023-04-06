from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto


# criando a classe do formulario contato
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, min_length=2)
    email = forms.EmailField(label='email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = (f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMenssagem: {mensagem}')

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema Django_mysql',
            body=conteudo,
            from_email='email@empresarial.com',
            to=['contato@dominio.com'],
            headers={'Reply to': email}
        )
        mail.send()

#criando  um Model form
#usa as informaçoes no banco de dados
class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model=Produto
        fields=['nome','preco','estoque','imagem']

