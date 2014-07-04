# Abstrac Class Person

``` python
class Person(models.Model):
	name = models.CharField(max_length=200, help_text='Enter the name')
	address = models.CharField(max_length=200, help_text='Address for Person')
	phone = models.CharField(max_length=200, help_text='Phone number for Person')
	email = models.EmailField(help_text='Enter the contact email')
	headshot = models.ImageField(upload_to='images', blank=True, null=True)
	birth_date = models.DateField(help_text='Enter the date of birth', blank=True, null=True)
	death_date = models.DateField(help_text='Enter the date of death', blank=True, null=True)
	job_title = models.CharField(max_length=200, help_text='Enter the job title of the person (for example, Financial Manager).', blank=True, null=True)
	gender = models.CharField(max_length=1, help_text='Gender of the person.', choices=GENDERS)

	class Meta:
		abstract = True
```
