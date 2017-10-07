from inbot.models import oper_para
aa = oper_para.objects.all()
aa.delete()
s1 = oper_para(name = 'shtkey',content = '1HZxWpTK2i3OsQz_xSYmyn92yf6LNZG406Vav-Kn9E5w')
s1.save()
s2 = oper_para(name = 'webhookparser',content = 'de37de5d2ea219a9a45de09b55b0729c')
s2.save()
s3 = oper_para(name = 'strapi',content = 'qzQbZczY8BaDBFUUMAKaznB9XIgkSZFkCHHX7V6dAayn5q2SzH39KbSGomm7qCwJWGUarAnHFrRV2ijZYl/vPq3AGqEY0s89hZRPQODfrf74JgCL5eVpMm8Fce5CkUZQ02jCDkoVCzC9lPF4yz27xgdB04t89/1O/w1cDnyilFU=')
s3.save()
s4 = oper_para(name = 'MerchantID',content = 'MS12338986')
s4.save()
s5 = oper_para(name = 'HashKey',content = 'NM9pCGBH6cekcJg1738DyoEEAhBqrSle')
s5.save()
s6 = oper_para(name = 'HashIV',content = 'FvDhbfZisdCEWSG3')
s6.save()
s7 = oper_para(name = 'HookBackURL',content = 'https://invoicebot.herokuapp.com')
s7.save()
s8 = oper_para(name = 'customer_service',content = 'https://line.me/R/ti/p/%40wxv3641e')
s8.save()
s9 = oper_para(name = 'invoicego_get_id',content = '49004171_bot')
s9.save()
s10 = oper_para(name = 'invoicego_get_pw',content = 'invoicegobot')
s10.save()
s11 = oper_para(name = 'InvoiceSumUrl',content = 'http://uat.invoicego.tw/carriermgt/')
s11.save()
s12 = oper_para(name = 'GoogleShortUrlApiKey',content = 'AIzaSyACoNg4LMDkhh59vojAYZ03fP2hqcbdX7o')
s12.save()
s13 = oper_para(name = 'DebugMode',content = 'N')
s13.save()


s1 = oper_para.objects.get(name = 'DebugMode')
s1.content = 'Y'
s1.save()



from inbot.models import TemplateSendMessageCtrl,CarouselTemplateCtrl,ButtonsTemplateCtrl,CarouselColumnCtrl,ImageCarouselTemplateCtrl
from inbot.models import MessageTemplateActionCtrl,URITemplateActionCtrl,PostbackTemplateActionCtrl,TextSendMessageCtrl
from inbot.models import StickerSendMessageCtrl,ImageSendMessageCtrl

#TemplateSendMessage
TSMCtrl = TemplateSendMessageCtrl.objects.all()
TSMCtrl.delete()
t1 =TemplateSendMessageCtrl(
    pid = 'start',
    description = 'start',
    alt_text = u'開始功能',
    templateclass = 'CarouselTemplate',
    templateid = 'cstart'
	)
t1.save()

#CarouselTemplate
CTCtrl = CarouselTemplateCtrl.objects.all()
CTCtrl.delete()
ct1 = CarouselTemplateCtrl(
	pid = 'cstart',
    description = 'cstart',
    CarouselColumn1id = 'invoice',
    CarouselColumn2id = 'order'
	)
ct1.save()


CCCtrl = CarouselColumnCtrl.objects.all()
CCCtrl.delete()
cc1 = CarouselColumnCtrl(
	pid = 'invoice',
    description = 'invoice',
    title = u'你好!',
    text = u'請選擇功能',
    thumbnail_image_url = 'https://i.imgur.com/3kix7D3.jpg',
    action1class = 'MessageTemplateAction',
    action1id = 'blank',
    action2class = 'PostbackTemplateAction',  #領取發票
    action2id = 'getinvoice',
    action3class = 'URITemplateAction',    #人工客服
    action3id = 'cusservice'
    )
cc1.save()

cc2 = CarouselColumnCtrl(
	pid = 'order',
    description = 'order',
    title = u'你好!',
    text = u'請選擇功能',
    thumbnail_image_url = 'https://i.imgur.com/3kix7D3.jpg',
    action1class = 'MessageTemplateAction',  
    action1id = 'blank',
    action2class = 'PostbackTemplateAction',  #商品列表
    action2id = 'prodlist',
    action3class = 'MessageTemplateAction',  #測試功能
    action3id = 'test'
	)
cc2.save()

PTACtrl = PostbackTemplateActionCtrl.objects.all()
PTACtrl.delete()
pta1 = PostbackTemplateActionCtrl(
	pid = 'getinvoice',
    description = 'getinvoice',
    label = u'領取發票',
    text = u'[領取發票]',
    data = 'move=TextSendMessageCtrl&id=invkey'
	)
pta1.save()


TSMCtrl= TextSendMessageCtrl.objects.all()
TSMCtrl.delete()
tsm1 = TextSendMessageCtrl(
    pid = 'error',
    description = 'error',
    text = u'我無法辨識您的輸入，建議您從下方選單選擇開始流程'
    )
tsm1.save()

tsm2 = TextSendMessageCtrl(
    pid = 'invkey',
    description = 'invkey',
    text = u'請點擊下方的鍵盤，輸入您的正確4碼英文數字領取金鑰'
    )
tsm2.save()


tsm3 = TextSendMessageCtrl(
    pid = 'invamt',
    description = 'invamt',
    text = u'請輸入本次消費金額'
    )
tsm3.save()


tsm4 = TextSendMessageCtrl(
    pid = 'email1',
    description = 'email1',
    text = u'請點擊下方的鍵盤，輸入您的正確email，以利中獎時我們能通知到您'
    )
tsm4.save()


tsm5 = TextSendMessageCtrl(
    pid = 'email1',
    description = 'email1',
    text = u'請點擊下方的鍵盤，輸入您的正確email，以利能通知您交易相關資訊'
    )
tsm5.save()

tsm6 = TextSendMessageCtrl(
    pid = 'emailok',
    description = 'emailok',
    text = u'您的email輸入成功，請選擇開始使用來使用此機器人'
    )
tsm6.save()


tsm7 = TextSendMessageCtrl(
    pid = 'getinvok1',
    description = 'getinvok1',
    text = u'您的發票已經順利成立，\n' + u'發票號碼：{}\n' + u'金額：{}\n' + u'隨機碼：{}'
    )
tsm7.save()

tsm8 = TextSendMessageCtrl(
    pid = 'getinvok2',
    description = 'getinvok2',
    text = u'如果發票中獎，本公司將寄信通知您，並於開獎翌日起十日內，將中獎發票寄信通知您做兌獎使用'
    )
tsm8.save()

tsm9 = TextSendMessageCtrl(
    pid = 'getinvok3',
    description = 'getinvok3',
    text = u'建議您完成歸戶，您即可在財政部電子發票整合服務平台查詢您所有的電子發票'
    )
tsm9.save()

tsm10 = TextSendMessageCtrl(
    pid = 'getinvok4',
    description = 'getinvok4',
    text = u'可點選以下連結完成歸戶作業,{}'
    )
tsm10.save()

tsm11 = TextSendMessageCtrl(
    pid = 'emailok',
    description = 'emailok',
    text = u'您的email輸入成功，請選擇開始使用來使用此機器人'
    )
tsm11.save()

tsm12 = TextSendMessageCtrl(
    pid = 'underbuild',
    description = 'underbuild',
    text = u'此功能還在開發中'
    )
tsm12.save()










