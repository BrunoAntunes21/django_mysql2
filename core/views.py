from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
#importando o formulario de contato
from .forms import ContatoForm,ProdutoModelForm
#importando o modelo de dados da tabela produto para exibição
from .models import Produto

# Create your views here.
def index(request):
    #criando a impostação dos dados
    context={'produtos':Produto.objects.all()}
    return render(request,'index.html',context)
def contato(request):
    form=ContatoForm(request.POST or None)
    #se o metodo for POST
    if str(request.method=='POST'):
        #imprimindo o post

        #se o formulario for valido
        if form.is_valid():
            form.send_mail()
            messages.success(request,'Email Enviado com sucesso')
            form=ContatoForm()
        else:
            messages.error(request,'ERRO AO ENVIAR OS DADOS')




    context={'form':form}
    return render(request,'contato.html',context)

def produto(request):
   #validando o usuario
   if str(request.user) !=  'AnonymousUser':
        if str(request.method)=='POST':
            form=ProdutoModelForm(request.POST,request.FILES)
            if form.is_valid():
                #SALVANDO O FOM(FORMULARIO)
                form.save()


                messages.success(request,'Produto salvo com sucesso.')
                form=ProdutoModelForm()
            else:
                messages.error(request,'Ops...Algun erro ocorreu desculpe o transtorno')
        else:
            form=ProdutoModelForm()
            context={ 'form':form
            }
        return render(request,'produto.html',context)
   else:
       return redirect('index')

