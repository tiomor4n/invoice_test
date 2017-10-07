from django.db import models

class oper_para(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
	

class TemplateSendMessageCtrl(models.Model):
    pid = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    alt_text = models.CharField(max_length=20)
    templateclass = models.CharField(max_length=30)
    templateid = models.CharField(max_length=10)
	
class CarouselTemplateCtrl(models.Model):
    pid = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    CarouselColumn1id = models.CharField(max_length=10)
    CarouselColumn2id = models.CharField(max_length=10)
    CarouselColumn3id = models.CharField(max_length=10)
    CarouselColumn4id = models.CharField(max_length=10)
    CarouselColumn5id = models.CharField(max_length=10)
	
		
class ButtonsTemplateCtrl(models.Model):
    pid = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=30)
    action1class = models.CharField(max_length=30)
    action1id = models.CharField(max_length=10)
    action2class = models.CharField(max_length=30)
    action2id = models.CharField(max_length=10)
    action3class = models.CharField(max_length=30)
    action3id = models.CharField(max_length=10)
	
class CarouselColumnCtrl(models.Model):
    pid = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=30)
    thumbnail_image_url = models.CharField(max_length=50)
    action1class = models.CharField(max_length=30)
    action1id = models.CharField(max_length=10)
    action2class = models.CharField(max_length=30)
    action2id = models.CharField(max_length=10)
    action3class = models.CharField(max_length=30)
    action3id = models.CharField(max_length=10)
	
	
class ImageCarouselTemplateCtrl(models.Model):
    pid = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    image_url = models.CharField(max_length=50)
    action1class = models.CharField(max_length=30)
    action1id = models.CharField(max_length=10)
	
class MessageTemplateActionCtrl(models.Model):
    pid = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    label = models.CharField(max_length=10)
    text = models.CharField(max_length=30)
	
class URITemplateActionCtrl(models.Model):
    pid = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    label = models.CharField(max_length=10)
    url = models.CharField(max_length=50)
	
class PostbackTemplateActionCtrl(models.Model):
    pid = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    label = models.CharField(max_length=10)
    text = models.CharField(max_length=100)
    data = models.CharField(max_length=50)
	

class TextSendMessageCtrl(models.Model):
    pid = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    text = models.CharField(max_length=100)

class StickerSendMessageCtrl(models.Model):
    pid = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    package_id = models.IntegerField()
    sticker_id = models.IntegerField()

class ImageSendMessageCtrl(models.Model):
    pid = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    original_content_url = models.CharField(max_length=50)
    preview_image_url = models.CharField(max_length=50)

	
	

	

	
    
	
	
	
	
	

# Create your models here.
