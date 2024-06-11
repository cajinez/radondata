from django import forms

from apps.aulas.models import Aula, Notificacion


class PreferenciaNotificacionesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario')
        super(PreferenciaNotificacionesForm, self).__init__(*args, **kwargs)
        grupos_usuario = usuario.groups.all()
        aulas = Aula.objects.filter(grupos__in=grupos_usuario).distinct()
        for aula in aulas:
            self.fields[f'preferencia_{aula.id}'] = forms.ChoiceField(
                label=f'Preferencia para {aula.nombre}',
                choices=Notificacion.PREFERENCIAS_NOTIFICACION,
                widget=forms.Select(attrs={'class': 'form-control'}),
                initial=Notificacion.objects.filter(usuario=usuario, aula=aula).first().preferencia if Notificacion.objects.filter(usuario=usuario, aula=aula).exists() else Notificacion.NINGUNA
            )
        