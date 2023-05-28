from .models import Anuncio

def latest_anuncio(request):
    last_anuncio = Anuncio.objects.last()
    return {'last_anuncio': last_anuncio}