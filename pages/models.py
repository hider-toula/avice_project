from django.db import models

# Create your models here.
class Project(models.Model):
    
    

    choices= (
            ('Équipements', 'Équipements'),
             ('Logements', 'Logements'),
             ('Urbanisme', 'Urbanisme'),
             ('Tertiaire', 'Tertiaire'),
             ('Autre', 'Autre'),
             )
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    adresse = models.CharField(max_length=200)
    
    project_type = models.CharField(max_length=200, choices=choices,default='Équipements')
    
    
    
    info_1 = models.CharField(max_length=200,blank=True)
    info_2 = models.CharField(max_length=200,blank=True)
    info_3 = models.CharField(max_length=200,blank=True)
    info_4 = models.CharField(max_length=200,blank=True)
    info_5 = models.CharField(max_length=200,blank=True)
    info_6 = models.CharField(max_length=200,blank=True)
    info_7 = models.CharField(max_length=200,blank=True)
    info_8 = models.CharField(max_length=200,blank=True)
    info_9 = models.CharField(max_length=200,blank=True)
    info_10 = models.CharField(max_length=200,blank=True)
    info_11 = models.CharField(max_length=200,blank=True)
    info_12 = models.CharField(max_length=200,blank=True)
    info_13 = models.CharField(max_length=200,blank=True)
    info_14 =models.CharField(max_length=200,blank=True)
    info_16 = models.CharField(max_length=200,blank=True)
    
    classement = models.IntegerField()
  
    
    
    main_image = models.ImageField(upload_to='images/')
    main_big_image = models.ImageField(upload_to='images/',default='images/defaut.jpg')
    
    
    image_1 = models.ImageField(upload_to='images/', blank=True)
    image_2 = models.ImageField(upload_to='images/', blank=True)
    image_3 = models.ImageField(upload_to='images/', blank=True)
    image_4 = models.ImageField(upload_to='images/', blank=True)
    image_5 = models.ImageField(upload_to='images/', blank=True)
    image_6 = models.ImageField(upload_to='images/', blank=True)
    image_7 = models.ImageField(upload_to='images/', blank=True)
    image_8 = models.ImageField(upload_to='images/', blank=True)
    image_9 = models.ImageField(upload_to='images/', blank=True)
    image_10 = models.ImageField(upload_to='images/', blank=True)
    image_11 = models.ImageField(upload_to='images/', blank=True)
    image_12 = models.ImageField(upload_to='images/', blank=True)
    image_13 = models.ImageField(upload_to='images/', blank=True)
    image_14 = models.ImageField(upload_to='images/', blank=True)
    image_15 = models.ImageField(upload_to='images/', blank=True)
    image_16 = models.ImageField(upload_to='images/', blank=True)
    image_17 = models.ImageField(upload_to='images/', blank=True)
    image_18 = models.ImageField(upload_to='images/', blank=True)
    image_19 = models.ImageField(upload_to='images/', blank=True)
    image_20 = models.ImageField(upload_to='images/', blank=True)
    image_21 =  models.ImageField(upload_to='images/', blank=True)
    image_22 = models.ImageField(upload_to='images/', blank=True)
    image_23 = models.ImageField(upload_to='images/', blank=True)
    image_24 = models.ImageField(upload_to='images/', blank=True)
    image_25 = models.ImageField(upload_to='images/', blank=True)
    
    is_puplished = models.BooleanField(default=True)
     
    

    def __str__(self):
        return self.title
    
    
    
    
    
class Actu(models.Model):
    
    


    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    main_image = models.ImageField(upload_to='images/')



    def __str__(self):
        return self.title
    


class About(models.Model):
    
    title_1 = models.CharField(max_length=200)
    description_1 = models.TextField(blank=True)
    
    
    
    def __str__(self):
        return self.title_1