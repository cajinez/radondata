from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from apps.aulas.models import Aula, Notificacion
from .forms import PreferenciaNotificacionesForm

# Create your views here.
@login_required(login_url="login/")
def preferences(request):
    if request.method == 'POST':
        form = PreferenciaNotificacionesForm(request.POST, usuario=request.user)
        if form.is_valid():
            grupos_usuario = request.user.groups.all()
            aulas = Aula.objects.filter(grupos__in=grupos_usuario).distinct()
            for aula in aulas:
                preferencia = form.cleaned_data[f'preferencia_{aula.id}']
                notificacion, created = Notificacion.objects.get_or_create(usuario=request.user, aula=aula)
                notificacion.preferencia = preferencia
                notificacion.save()
            messages.success(request, "¡Su perfil ha sido actualizado correctamente!")    
            return redirect('preferences')
        else:
            form = PreferenciaNotificacionesForm(usuario=request.user)
    
    return render(request, 'accounts/preferences.html', {'form': form})