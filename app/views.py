from django.shortcuts import render
from jogos.models import Jogo


def home_view(request):
    jogos_destaque = Jogo.objects.all().order_by('-id')[:12]
    return render(request, 'app/home.html', {'jogos_destaque': jogos_destaque})