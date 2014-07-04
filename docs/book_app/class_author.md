# Class Author

```python
class Author(Person):
	honorific_prefix = models.CharField(max_length=6, help_text="An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.", blank=True, null=True)
	honorific_suffix = models.CharField(max_length=6, help_text="An honorific suffix preceding a Person's name such as M.D. /PhD/MSCSW.", blank=True, null=True)
	nationality = models.CharField(max_length=64, help_text="Nationality of the person.", blank=True, null=True)
	posted_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name
```
