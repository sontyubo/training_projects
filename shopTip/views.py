from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, CreateView, DeleteView, DetailView

from .models import ShopTipModel, RecordedTask
from .forms import AddForm, RecordedForm

# Create your views here.
class shopTipList(View):
    def get(self, request, *args, **kwargs):
        all_objects = ShopTipModel.objects.all()

        context = {
            'tasks':all_objects, 
            'form':AddForm()
            }

        return render(request, 'shopTipIndex.html', context)

    def post(self, request, *args, **kwargs):
        form = AddForm(request.POST)

        # バリデーション違反なら
        if not form.is_valid():
            return redirect(reverse('shopTip:index'))
        
        form.save()

        return redirect(reverse('shopTip:index'))

class ShopTipDetail(DetailView):
    template_name = 'detail.html'
    model = ShopTipModel

class detailDelete(DeleteView):
    template_name = 'delete.html'
    model = ShopTipModel
    success_url = reverse_lazy('shopTip:index')

class ChoiceTasks(View):
    def get(self, request, *args, **kwargs):
        all_objects = ShopTipModel.objects.all()
        context = {
            'tasks':all_objects, 
            }
        return render(request, 'index_choice.html', context)
    
    def post(self, request, *args, **kwargs):
        delete_pks = request.POST.getlist('delete')

        # pksのオブジェクトを取得してレコードに保存
        objects = ShopTipModel.objects.filter(pk__in=delete_pks)

        # 個別に保存
        for object in objects:
            model = RecordedTask(title=object.title, memo=object.memo)
            model.save()
            # objectの削除
            object.delete()
        return redirect(reverse('shopTip:index'))

class RecordView(View):
    def get(self, request, *args, **kwargs):
        all_objects = RecordedTask.objects.all()
        context = {
            'tasks':all_objects, 
            }
        return render(request, 'record_index.html', context)
    

    def post(self, request, *args, **kwargs):
        delete_pks = request.POST.getlist('delete')

        # pksのオブジェクトを取得してレコードに保存
        objects = RecordedTask.objects.filter(pk__in=delete_pks)
        objects.delete()
        return redirect(reverse('shopTip:index'))

