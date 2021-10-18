import unittest
from django.forms.fields import CharField, EmailField
from contactdetails import views 
from contactdetails.forms import contact_details
class unittesting(unittest.TestCase):
    def emailfield(self):
        result=contact_details.Email_id=EmailField
        self.assertEqual(result,EmailField)  
    def firstname(self):
        result=contact_details.first_name=str
        self.assertEqual(result,str)
    def lastname(self):
        result=contact_details.last_name=str
        self.assertEqual(result,str)
    def job_description(self):
        result=contact_details=str
        self.assertEqual(result,str)
if __name__=='__main__'():
    unittest.main()