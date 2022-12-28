from django.db import models
#from django.core.exceptions import ValidationError
from django.forms import ValidationError
from django.core import validators

'''

def check_id(value):
    if len(str(value))!=4:
        raise ValidationError('the maximum lenth value 4')
    

def check_n(value):
    if str(value)[0]!='5':
        raise ValidationError('it will be start with only 5 ')
    '''
'''def check_mail(value):
    e=Student.s_mail
    r=Student.s_reemail
    if e!=r:
        raise forms.ValidationError('both are not matched ')
        '''
class Student(models.Model):
    s_id=models.IntegerField(primary_key=True,validators=[validators.MaxLengthValidator(5)])
    s_name=models.CharField(max_length=100,validators=[])
    s_mail=models.EmailField()
    s_reemail=models.EmailField()
    s_moblie=models.CharField(max_length=10, validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)],default='1234567890')
    
    
    def clean(self):
        e=self.s_mail
        r=self.s_reemail
        if e!=r:
            raise ValidationError('both are not matched ')
