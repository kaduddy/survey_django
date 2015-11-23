from django.shortcuts import render, redirect

def index(request):
	try:
		request.session['submit'] += 1
	except:
		request.session['submit'] = 0
	return render(request, 'surveys/index.html')

def process_form(request):
	print request.POST
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	return redirect('result') 

def result(request):
	context = {
		"name": request.session["name"],
		"location": request.session["location"],
		"language": request.session["language"],
		"comment": request.session["comment"]
	}
	return render(request, 'surveys/result.html', context)
