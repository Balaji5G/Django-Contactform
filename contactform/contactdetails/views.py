"""View file we ll render our form with send email function"""
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from contactdetails.forms import contact_details
# Create your views here.
def contact(request):
    """this function will chech the request method and return the form upon it"""
    if request.method=='GET':
        form=contact_details()
    else:
        form = contact_details(request.POST,request.FILES)
        file=request.FILES['Uploadfile']
        if form.is_valid():
            subject='Contact Details'
            body={
                'firstname':form.cleaned_data['first_name'],
                'lastname':form.cleaned_data['last_name'],
                'jobdescription':form.cleaned_data['Job_description'],
            }
            message='\n'.join(body.values())
            email=form.cleaned_data['Email_id']
            mail=EmailMessage(subject,message,email,['balajichandran54@gmail.com'])
            mail.attach(file.name,file.read(),file.content_type)
            mail.send()
            return HttpResponse('Successfully Submitted')    
    return render(request,'contactpage.html',{'form':form})
#if __name__=='__main__':
