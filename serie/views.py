from django.shortcuts import render
from django.http import HttpResponseNotAllowed

from . import models
from . import forms

def cadastro(request):
    form= forms.SerieForm()
    if request.method == 'POST':
        print('vou salvar os dados!!')
        form=forms.SerieForm(request.POST)
        print(form)
        if form.is_valid():
            form.save(commit=True)
        else:
            print('ERROR')
    series_list=models.Serie.objects.order_by('nome')
    data_dict = {'serie_records':series_list , 'form':form}
    return render(request, 'serie/serie.html', data_dict)

def delete(request, id):
    try:
        models.Serie.objects.filter(id=id).delete()
        form=forms.SerieForm(); 
        series_list=models.Serie.objects.order_by('nome')
        data_dict={'form':form, 'serie_records':series_list}
        return render(request, 'serie/serie.html', data_dict)
    except:
        return HttpResponseNotAllowed() 

def update(request, id):
    item= models.Serie.objects.get(id=id)
    if request.method=='GET':
        form=forms.SerieForm(initial={'nome':item.nome, 'idGenero':item.idGenero})
        data_dict={'form':form} 
        return render(request,'serie/serie_upd.html', data_dict)
    else:
        form=forms.SerieForm(request.POST)
        item.nome=form.data['nome']
        item.idGenero_id=form.data['idGenero'] # COLOQUEI O  _id  PQ SE NAO ELE NAO VAI PEGAR REALMENTE O id, E SIM A DESCRICAO DO GENERO
        item.save() 
        form = forms.SerieForm()   
        series_list=models.Serie.objects.order_by('nome')
        data_dict={'form':form, 'serie_records':series_list}
        return render(request, 'serie/serie.html', data_dict)