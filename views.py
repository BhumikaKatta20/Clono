from django.shortcuts import redirect,render, HttpResponse
from Clono.forms import RegistrationForm
from django.contrib.auth.models import User
from Clono.models import UserProfile
marks=0

# Create your views here.
def index(request):
	return render(request,'index.html')

def register(request):
	if request.method =='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_redirect')
	else:
		form=RegistrationForm()
		args= {'form':form}
		return render(request,'Clono/register.html',args)

def myAccount(request):
	  	
	return render(request,'Clono/myAccount.html',{'user':request.user})

def to_apply(request):
	args={'user':request.user}
	return render(request,'Clono/to_apply.html',args)	    

	

def customerMain(request):
	args={'user':request.user}
	return render(request,'Clono/home.html',args)

def calculate(request):
	Ans=request.GET['answer']
	marks=0
	if Ans=='b':
		marks=10
	return render(request,'Clono/to_apply.html',{'Marks':marks})

def cloudcomputing(request):
	Quest=open('Clono/QuizQuestions.txt')
	count=0
	for line in Quest:
	    a.append(line)
	    count=count+1
	    Q=line.find('CloudQues:')
	    E=line.find('?')
	    A=line.find('Cloudans:')
	    o1=line.find('a)')
	    o2=line.find('b)')
	    o3=line.find('c)')
	    Quiz_Question=(line[Q+10:E+1])
	    Quiz_Answer=(line[A+9:A+11])
	    option1=(line[o1:o2-1])
	    option2=(line[o2:o3-1])
	    option3=(line[o3:A])
	return render(request,'Clono/quiz/cloudcomputing.html',{
		'user':request.user,'Question':Quiz_Question,'Answer':Quiz_Answer,
		'option_1':option1,'option_2':option2,'option_3':option3}
	)

def Pythonpart(request):
	Quest=open('Clono/QuizQuestions.txt')
	a=[]
	for line in Quest:
	    a.append(line)
	    
	    Q=line.find('pyQues:')
	    E=line.find('?')
	    A=line.find('Pyans:')
	    o1=line.find('a)')
	    o2=line.find('b)')
	    o3=line.find('c)')
	    Quiz_Question=(line[Q+7:E+1])
	    Quiz_Answer=(line[A+10:A+11])
	    option1=(line[o1:o2-1])
	    option2=(line[o2:o3-1])
	    option3=(line[o3:A])
	return render(request,'Clono/quiz/Pythonpart.html',{
		'user':request.user,'Question':Quiz_Question,'Answer':Quiz_Answer,
		'option_1':option1,'option_2':option2,'option_3':option3}
	)
def Webdevelopment(request):
	Quest=open('Clono/QuizQuestions.txt')
	a=[]
	for line in Quest:
	    a.append(line)
	    
	    Q=line.find('WEBQUES101:')
	    E=line.find('?')
	    A=line.find('WEBANS101:')
	    o1=line.find('a)')
	    o2=line.find('b)')
	    o3=line.find('c)')
	    Quiz_Question=(line[Q+12:E+1])
	    Quiz_Answer=(line[A+10:A+11])
	    option1=(line[o1:o2-1])
	    option2=(line[o2:o3-1])
	    option3=(line[o3:A])
	return render(request,'Clono/quiz/Webdevelopment.html',{
		'user':request.user,'Question':Quiz_Question,'Answer':Quiz_Answer,
		'option_1':option1,'option_2':option2,'option_3':option3}
	)