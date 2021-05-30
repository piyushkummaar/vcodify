from django.db import models
    

# Create your models here.
class Contact(models.Model):
    '''
    This is the contact model that for storing and getting data form the tbl_contact in db.
    '''
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=400)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = "Contact Form Data"
        verbose_name_plural = "Contact Form Data"
        managed = True
        db_table = "tbl_contact"

class Portfolio(models.Model):
    '''
    This is the Portfolio model that for storing and getting data form the tbl_portfolio in db.
    '''
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    imageorvideo = models.FileField(upload_to='portfolio/',default='logo.png',verbose_name="Image or Video")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.description[:50] + '...'
    
    def get_image_video(self):
        return str(self.imageorvideo).split('.')[1]


    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"
        managed = True
        db_table = "tbl_portfolio"
