from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
import json


# Create your views here.



VOWELS = ['a', 'e', 'i', 'o', 'u']

# home........
def home(request):
	return render(request, 'LatinPig/home.html', {})


def translate(word):
	firstChar = word[0]
	if not word:
		return ''
	elif firstChar in VOWELS:
		return word + 'way'
	else:
		return word[1:] + word[0] + 'ay'


def translation(request):
	if request.method == 'POST':
		text = request.POST['inputword']
		response_data = {}
		response_data['translation'] = translate(text)
		response_data['result'] = 'Create post successful!'

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
			)
	else:
		return HttpResponse()
		


