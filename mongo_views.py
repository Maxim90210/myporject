import string
import random
from django.shortcuts import render, redirect
from .forms import URLForm
from .mongo_storage import URLStorage
import asyncio

storage = URLStorage()

def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

async def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_id = generate_short_id()
            await storage.save_url(short_id, original_url)
            return render(request, 'shortener/success.html', {'short_id': short_id})
    else:
        form = URLForm()

    return render(request, 'shortener/index.html', {'form': form})

async def redirect_url(request, short_id):
    document = await storage.get_url(short_id)
    if document:
        await storage.increment_clicks(short_id)
        return redirect(document['original_url'])
    else:
        return render(request, 'shortener/404.html', status=404)
