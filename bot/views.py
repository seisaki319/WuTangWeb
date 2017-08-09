from django.shortcuts import render
from bot.forms import LyricForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, HttpResponse
from bot.WuTangBot.all_writers import AllWriters

# Create your views here.

class LyricView(FormView):
    template_name = 'bot/contact.html'
    form_class = LyricForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)

def index(request):
    form_class = LyricForm
    if request.method == 'POST':
        lyric = request.POST.get(
                'lyric'
            , '')
        lines = request.POST.get('lines', '')
        return render(request, 'bot/form.html', {
            'form': form_class,
            'lyrics': AllWriters.wutang.generate_song(lyric, int(lines), 2)
        })
    return render(request, 'bot/form.html', {
        'form': form_class,
    })
