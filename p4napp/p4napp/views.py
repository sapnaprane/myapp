# import Http Response from django
from django.http import HttpResponse
# get datetime
import datetime

# create a function
def p4n_view(request):
	# fetch date and time
	now = datetime.datetime.now()
	# convert to string
	html = "Time is {}".format(now)
	# return response
	return HttpResponse("Welcome to p4n")