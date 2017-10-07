from .models import oper_para,TemplateSendMessageCtrl,CarouselTemplateCtrl,ButtonsTemplateCtrl,CarouselColumnCtrl,ImageCarouselTemplateCtrl,MessageTemplateActionCtrl,URITemplateActionCtrl,PostbackTemplateActionCtrl,TextSendMessageCtrl,StickerSendMessageCtrl,ImageSendMessageCtrl
from linebot import LineBotApi, WebhookHandler,WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

class LineTempFlow:
    def __init__(self,purporse,purporseid,username=''):
        self.purporse = purporse
        self.purporseid = purporseid
        self.username = username
        
        
    def getResponse(self):
        def getButtonsTemplate(pid,showusername = False):
            BTCtrl = ButtonsTemplateCtrl.objects.get(pid=pid)
            if showusername == True:
                title = self.username + BTCtrl.title
            else:
                title = BTCtrl.title
            text = BTCtrl.text
            ac1class = BTCtrl.action1class
            print ('action1class:' + ac1class)
            ac2class = BTCtrl.action2class
            ac3class = BTCtrl.action3class
            ac1id = BTCtrl.action1id
            print ('ac1id:' + ac1id)
            ac2id = BTCtrl.action2id
            ac3id = BTCtrl.action3id
            BTActionArr = []

            if ac1class == 'MessageTemplateAction':
                BTActionArr.append(getMessageTemplateActionCtrl(ac1id))
            if ac1class == 'URITemplateAction':
                BTActionArr.append(getURITemplateActionCtrl(ac1id))
            if ac1class == 'PostbackTemplateAction':
                BTActionArr.append(getPostbackTemplateActionCtrl(ac1id))

            if ac2class == 'MessageTemplateAction':
                BTActionArr.append(getMessageTemplateActionCtrl(ac2id))
            if ac2class == 'URITemplateAction':
                BTActionArr.append(getURITemplateActionCtrl(ac2id))
            if ac2class == 'PostbackTemplateAction':
                BTActionArr.append(getPostbackTemplateActionCtrl(ac2id))

            if ac3class == 'MessageTemplateAction':
                BTActionArr.append(getMessageTemplateActionCtrl(ac3id))
            if ac3class == 'URITemplateAction':
                BTActionArr.append(getURITemplateActionCtrl(ac3id))
            if ac3class == 'PostbackTemplateAction':
                BTActionArr.append(getPostbackTemplateActionCtrl(ac3id))
             
            print  (len(BTActionArr)) 
            return ButtonsTemplate(title = title,text = text,actions = BTActionArr)
        
        def getCarouselTemplate(pid):
            CColumnCtrl = CarouselTemplateCtrl.objects.get(pid=pid)
            CColumnArr = []
            CColumn1id = CColumnCtrl.CarouselColumn1id
            CColumn2id = CColumnCtrl.CarouselColumn2id
            CColumn3id = CColumnCtrl.CarouselColumn3id
            CColumn4id = CColumnCtrl.CarouselColumn4id
            CColumn5id = CColumnCtrl.CarouselColumn5id

            if CColumn1id != None:
                CColumnArr.append(getCarouselColumn(CColumn1id))
            if CColumn2id != None:
                CColumnArr.append(getCarouselColumn(CColumn2id))
            if CColumn3id != None:
                CColumnArr.append(getCarouselColumn(CColumn3id))
            if CColumn4id != None:
                CColumnArr.append(getCarouselColumn(CColumn4id))
            if CColumn5id != None:
                CColumnArr.append(getCarouselColumn(CColumn5id))

            return CarouselTemplate(columns = CColumnArr)
        
        def getMessageTemplateActionCtrl(pid):
            MTActionCtrl = MessageTemplateActionCtrl.objects.get(pid=pid)
            label = MTActionCtrl.label
            text = MTActionCtrl.text
            return MessageTemplateAction(label=label,text=text)
            
        def getURITemplateActionCtrl(pid):
            UTActionCtrl = URITemplateActionCtrl.objects.get(pid=pid)
            label = UTActionCtrl.label
            url = UTActionCtrl.url
            return URITemplateAction(label=label,url=url)
            
        def getPostbackTemplateActionCtrl(pid):
            PTACtrl = PostbackTemplateActionCtrl.objects.get(pid=pid)
            label = PTACtrl.label
            text = PTACtrl.text
            data = PTACtrl.data
            print ('data:'+data)
            return PostbackTemplateAction(label=label,text=text,data=data)
        
        def getCarouselColumn(pid,showusername = False):
            CCtrl = CarouselColumnCtrl.objects.get(pid=pid)
            if showusername == True:
                title = self.username + CCtrl.title
            else:
                title = CCtrl.title
            text = CCtrl.text
            ac1class = CCtrl.action1class
            ac2class = CCtrl.action2class
            ac3class = CCtrl.action3class
            ac1id = CCtrl.action1id
            print ('ac1id:' + ac1id)
            ac2id = CCtrl.action2id
            ac3id = CCtrl.action3id
            thumbnail_image_url = CCtrl.thumbnail_image_url
            CCActionArr = []

            if ac1class == 'MessageTemplateAction':
                CCActionArr.append(getMessageTemplateActionCtrl(ac1id))
            if ac1class == 'URITemplateAction':
                CCActionArr.append(getURITemplateActionCtrl(ac1id))
            if ac1class == 'PostbackTemplateAction':
                CCActionArr.append(getPostbackTemplateActionCtrl(ac1id))

            if ac2class == 'MessageTemplateAction':
                CCActionArr.append(getMessageTemplateActionCtrl(ac2id))
            if ac2class == 'URITemplateAction':
                CCActionArr.append(getURITemplateActionCtrl(ac2id))
            if ac2class == 'PostbackTemplateAction':
                CCActionArr.append(getPostbackTemplateActionCtrl(ac2id))

            if ac3class == 'MessageTemplateAction':
                CCActionArr.append(getMessageTemplateActionCtrl(ac3id))
            if ac3class == 'URITemplateAction':
                CCActionArr.append(getURITemplateActionCtrl(ac3id))
            if ac3class == 'PostbackTemplateAction':
                CCActionArr.append(getPostbackTemplateActionCtrl(ac3id))
                
            return CarouselColumn(title = title,text = text,thumbnail_image_url = thumbnail_image_url,actions = CCActionArr)
        
        
    
        if self.purporse == 'TemplateSendMessage':
            TSMCtrl = TemplateSendMessageCtrl.objects.get(pid=self.purporseid)
            alt_text = TSMCtrl.alt_text
            templateid = TSMCtrl.templateid
            templateclass = TSMCtrl.templateclass
            
            if templateclass == 'ButtonsTemplate':
                template = getButtonsTemplate(templateid,bool(self.username != ''))
                return TemplateSendMessage(alt_text=alt_text,template=template)
            if templateclass == 'CarouselTemplate':
                template = getCarouselTemplate(templateid,bool(self.username != ''))
                return TemplateSendMessage(alt_text=alt_text,template=template)

        if self.purporse == 'ButtonsTemplate':
            BtnCtrl = ButtonsTemplateCtrl.objects.get(pid = self.purporseid)
            templateid = self.purporseid
            template = getButtonsTemplate(templateid)
            return template

        if self.purporse == 'PostbackTemplateAction':
            PoAct = getPostbackTemplateActionCtrl(self.purporseid)
            return PoAct


        
        if self.purporse == 'TextSendMessage':
            TextCtrl = TextSendMessageCtrl.objects.get(pid=self.purporseid)
            text = TextCtrl.text
            return TextSendMessage(text=text)
        
        if self.purporse == 'ImageSendMessage':
            ImageCtrl = ImageSendMessageCtrl.objects.get(pid=self.purporseid)
            original_content_url = ImageCtrl.original_content_url
            preview_image_url = ImageCtrl.preview_image_url
            return ImageSendMessage(original_content_url=original_content_url,preview_image_url=preview_image_url)

        if self.purporse == 'StickerSendMessage':
            StickCtrl = StickerSendMessageCtrl.objects.get(pid=self.purporseid)
            package_id = StickCtrl.package_id
            sticker_id = StickCtrl.sticker_id
            return StickerSendMessage(package_id=package_id,sticker_id=sticker_id)