from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	#return HttpResponse('Hello')
	return render(request, 'home.html')

# ------------------------------------------------------------------------------------------------------------------------

def eggs(request):
	return HttpResponse('<h1>Eggs</h1>')

# ------------------------------------------------------------------------------------------------------------------------

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split() # convert string to list
	
	wordcountdict={}
	for i in wordlist:
		if i in wordcountdict:
			wordcountdict[i] += 1
		else:
			wordcountdict[i]=1

	sortedWords = sorted(wordcountdict.items(), key=operator.itemgetter(1), reverse=True)
	# .items() helps distinguish between keys and values
	# key determines what to sort (in this case, values), reverse sorts it from greatest to least

	return render(request,'count.html',{'fulltext':fulltext,'totalcount':len(wordlist),'sortedWords':sortedWords})

# ------------------------------------------------------------------------------------------------------------------------

def about(request):
	return render(request,'about.html')