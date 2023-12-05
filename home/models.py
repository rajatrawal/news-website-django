from django.db import models
from uuid import uuid4
from django.utils.text import slugify


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['updated_at']


class Category(BaseModel):
    text = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.text
    


class Hashtag(BaseModel):
    text = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.text


class News(BaseModel):
    heading = models.CharField(
        max_length=150, null=False, blank=False, unique=True)
    is_breaking = models.BooleanField(default=False)
    slug = models.SlugField(default='',null= True,blank = True,max_length=200)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    def __str__(self):
        return self.heading
    
    def get_short_para(self):
        obj = Element.objects.filter(news=self,type='paragraph')
        if obj.exists():
            obj = obj.order_by('order_no')
            obj = obj[0]
            return obj.text
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super(News, self).save(*args, **kwargs)


class NewsHashtag(BaseModel):
    hashtag = models.ForeignKey(
        Hashtag, on_delete=models.CASCADE, null=False, blank=False, related_name='news_hashtag')
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, null=False, blank=False, related_name='news_hashtag')
    
    def __str__(self):
        return f'{self.hashtag} {self.news}'

class NewsCategory(BaseModel):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False, related_name='news_category')
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, null=False, blank=False, related_name='news_category')
    
    def __str__(self):
        return f'{self.category} {self.news}'


class Element(BaseModel):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, null=True, blank=True, related_name='element')
    order_no = models.IntegerField( blank=False, null=False)
    choices = (('paragraph', 'paragraph'), ('title', 'title'),
               ('image', 'image'), ('subtext', 'subtext'))
    type = models.CharField(
        choices=choices, max_length=9, null=False, blank=False)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.order_no} {self.news}'

# class NewsElement(BaseModel):
    
#     element = models.ForeignKey(
#         Element, on_delete=models.CASCADE, null=False, blank=False, related_name='news_element')
    
#     def __str__(self):
#         return f'{self.element} {self.news}'
    
class NewsThumbnill(BaseModel):
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=False, blank=False, related_name='news_thumbnill')
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    def __str__(self):
        return f'{self.image} {self.news}'

