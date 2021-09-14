from django.shortcuts import render

from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.db import models

from django.forms import inlineformset_factory

from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from basketapp.models import Basket
from newordersapp.models import Order, OrderItem
from newordersapp.forms import OrderItemForm


class OrderList(ListView):
   model = Order

   def get_queryset(self):
       return Order.objects.filter(user=self.request.user)




    
class OrderItemsCreate(CreateView):
    model = Order
    fields = []     # Список полей пустой, так как в соответствии с моделью все они, кроме пользователя «user», создаются автоматически.
    success_url = reverse_lazy('newordersapp:orders_list')
    
    
    def get_context_data(self, **kwargs):
        data = super(OrderItemsCreate, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1) #Метод «inlineformset_factory()» возвращает нам конструктор набора форм
        
        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket_items = Basket.get_items(self.request.user)
            if len(basket_items):
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=len(basket_items))
                formset = OrderFormSet()
                for num, form in enumerate(formset.forms):
                    form.inital['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
                basket_items.delete()
            else:
                formset = OrderFormSet()
        
        data['orderitems'] = formset
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()
        
        return super(OrderItemsCreate, self).form_valid(form)

class OrderItemsUpdate(UpdateView):
    model = Order
    fields = []     # Список полей пустой, так как в соответствии с моделью все они, кроме пользователя «user», создаются автоматически.
    success_url = reverse_lazy('newordersapp:orders_list')
    
    
    def get_context_data(self, **kwargs):
        data = super(OrderItemsCreate, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1) #Метод «inlineformset_factory()» возвращает нам конструктор набора форм
        
        if self.request.POST:
            data['orderitems'] = OrderFormSet(self.request.POST, instance=self.object)
        else:
            data['orderitems'] = OrderFormSet(instance=self.object)
            
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()
        
        return super(OrderItemsCreate, self).form_valid(form)
class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('newordersapp:orders_list')
class OrderRead(DetailView):
    model = Order
    def get_context_data(self, **kwargs):
        context = super(OrderRead, self).get_context_data(**kwargs)
        context['title'] = 'заказ/просмотр'
        return context

def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SENT_TO_PROCEED
    order.save()

    return HttpResponseRedirect(reverse('newordersapp:orders_list'))