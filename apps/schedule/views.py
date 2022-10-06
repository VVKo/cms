from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.
def schedule_index(request):
    # URL = 'https://script.google.com/macros/s/AKfycbyZuhJulQl97bYMUWYOzOXjy8MsuRtj4d_FkiJe8tcPpBxhl_HcrpTRnzY8RQ1aOA/exec?action=GET'
    context = {}
    # try:
    #     response = requests.get(URL)
    #     if response.status_code == 200:
    #         context['resp'] = response.json()
    # except requests.RequestException as exc:
    #     print(f"An error occurred while requesting {exc.request.url!r}.")

    return render(request, 'schedule/index.html', context)

def schedule_get(request):
    URL = 'https://script.google.com/macros/s/AKfycbyZuhJulQl97bYMUWYOzOXjy8MsuRtj4d_FkiJe8tcPpBxhl_HcrpTRnzY8RQ1aOA/exec?action=GET'
    response = requests.get(URL)
    return JsonResponse(response.json(), safe=False)