from django.shortcuts import render, redirect, get_object_or_404
from .models import WatchItem
from .forms import WatchItemForm

def item_list(request):
    items = WatchItem.objects.all().order_by('-created_at')
    return render(request, 'watchlist/item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = WatchItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = WatchItemForm()
    return render(request, 'watchlist/item_form.html', {'form': form, 'title': 'Add New Item'})

def item_edit(request, pk):
    item = get_object_or_404(WatchItem, pk=pk)
    if request.method == 'POST':
        form = WatchItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = WatchItemForm(instance=item)
    return render(request, 'watchlist/item_form.html', {'form': form, 'title': 'Edit Item'})

def mark_done(request, pk):
    item = get_object_or_404(WatchItem, pk=pk)
    item.status = 'done'
    item.save()
    return redirect('item_list')