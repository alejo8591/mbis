from django.db import models

GENDERS = (
	('f', 'Female'),
	('m', 'Male'),
)

class Picture(models.Model):
    image = models.ImageField(upload_to='images')
    upload_to = models.DateTimeField(auto_now_add=True)

    class Meta:
		abstract = True

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

class Author(Person):
	honorific_prefix = models.CharField(max_length=6, help_text="An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.", blank=True, null=True)
	honorific_suffix = models.CharField(max_length=6, help_text="An honorific suffix preceding a Person's name such as M.D. /PhD/MSCSW.", blank=True, null=True)
	nationality = models.CharField(max_length=64, help_text="Nationality of the person.", blank=True, null=True)
	posted_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

class PicturesAuthor(Picture):
	author = models.ForeignKey(Author)

class BookFormatType(models.Model):
	""" The publication format of the book. """
	name = models.CharField(max_length=255, help_text='Enter the name of the book format type')
	slug = models.SlugField(max_length=255, unique=True, help_text='Enter the slug of the book format type')
	alternate_name = models.CharField(max_length=255, help_text='Enter the alternate name of the book format type', blank=True, null=True)
	description = models.TextField(help_text='Enter description of the book format type', blank=True, null=True)
	image = models.ImageField(upload_to='images', blank=True, null=True)
	posted_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

class Book(models.Model):
	""" Book Model """
	number_page = models.IntegerField(help_text='Enter the number page of the book')
	slug = models.SlugField(max_length=255, unique=True, help_text='Enter the slug of the book')
	title = models.CharField(max_length=255, help_text='Enter the title of the book')
	subtitle = models.CharField(max_length=255, help_text='Enter the subtitle of the book')
	awards = models.CharField(max_length=255, help_text='An award won by this person or for this creative work.')
	description = models.TextField(help_text='Enter description of the book')
	isbn = models.CharField(max_length=255, help_text='Enter the ISBN of the book', unique=True)
	book_format_type = models.ForeignKey(BookFormatType, help_text='Select of the book format type')
	pages = models.PositiveIntegerField(max_length=5, help_text='The number of pages of the book')
	authors = models.ManyToManyField(Author)
	year_publication = models.DateField(help_text='Enter the publication date (year) of the bookh', blank=True, null=True)
	download = models.URLField(help_text='The download URL of the book', blank=True, null=True)
	posted_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

class PictureBook(Picture):
	book = models.ForeignKey(Book)

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-name"]

    def __unicode__(self):
        return self.name
