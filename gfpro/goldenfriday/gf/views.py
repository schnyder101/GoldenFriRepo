from django.shortcuts import render
from django.conf import settings
# Create your views here.
def home(request):
	title="Subscribe below"
	# form =SignUpForm(request.POST or None)
	# if request.user.is_authenticated():
	# 	title='My Title %s' %(request.user)
	# 	form =SignUpForm(request.POST or None)
		
	# 	if form.is_valid():
	# 		#form.save()
	# 		print "bbbbbb"
	# 		instance=form.save(commit=False)
	# 		name=form.cleaned_data.get('full_name')
	# 		if not name:
	# 			name="Kenshin"
	# 			print name
	# 		instance.full_name=name
	# 		instance.save()
	context ={
		"template_title": title,
		# "form":form,
	}
	return render(request,"home.html",context)