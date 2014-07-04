# Abstrac Class Picture

```python
class Picture(models.Model):
    image = models.ImageField(upload_to='images')
    upload_to = models.DateTimeField(auto_now_add=True)

    class Meta:
		abstract = True

```
