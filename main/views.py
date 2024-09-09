from django.shortcuts import render
def show_main(request):
    context = {
        'namaAplikasi' : 'tokopakdika',
        'name': 'Philip Halomoan Sampenta Manurung',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
# Create your views here.
