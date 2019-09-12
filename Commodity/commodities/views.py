from django.shortcuts import render, HttpResponse, redirect
from commodities.models import Picture
from commodities import models
from decimal import *

# Create your views here.
def pageA1(request):
    # 图片上传
    if request.method == 'POST':
        try:
            img = Picture(img_url=request.FILES.get('img'), AX=Decimal(request.POST.get('AX')), HL=Decimal(request.POST.get('HL')),
                          WL=Decimal(request.POST.get('WL')), ct1=Decimal(request.POST.get('ct1')), c01=Decimal(request.POST.get('c01')),
                          ct2=Decimal(request.POST.get('ct2')), c02=Decimal(request.POST.get('c02')), ct3=Decimal(request.POST.get('c03')),
                          c03=Decimal(request.POST.get('c03')), ct4=Decimal(request.POST.get('ct4')), c04=Decimal(request.POST.get('c04')),
                          ct5=Decimal(request.POST.get('ct5')), c05=Decimal(request.POST.get('c05')), ct6=Decimal(request.POST.get('ct6')),
                          c06=Decimal(request.POST.get('c06')), ct7=Decimal(request.POST.get('ct7')), c07=Decimal(request.POST.get('c07')),
                          ct8=Decimal(request.POST.get('ct8')), c08=Decimal(request.POST.get('c08')), pt=Decimal(request.POST.get('pt')),
                          p01=Decimal(request.POST.get('p01')), p02=Decimal(request.POST.get('p02')), p03=Decimal(request.POST.get('p03')),
                          p04=Decimal(request.POST.get('p04')), p05=Decimal(request.POST.get('p05')), p06=Decimal(request.POST.get('p06')),
                          AT=Decimal(request.POST.get('AT')), QW=Decimal(request.POST.get('QW')), QP=Decimal(request.POST.get('QP')),
                          QC=Decimal(request.POST.get('QC')), HT=Decimal(request.POST.get('HT')), AW=Decimal(request.POST.get('AW')),
                          AH=Decimal(request.POST.get('AH')), QW1=Decimal(request.POST.get('QW1')),
                          )
        except Exception as e:
            return HttpResponse("<script>alert('您输入的信息有误，请输入数字！');window.location='/pageA1/';</script>")
            # return redirect("/pageA1/")
        img.save()
    picture = models.Picture.objects.all()
    choose_img = models.Picture.objects.all().first()
    return render(request, 'pageA1.html', {'picture': picture, 'choose_img': choose_img})

def pageA11(request):
    picture = models.Picture.objects.all()
    choose_img = models.Picture.objects.all().first()
    return render(request, 'pageA11.html', {'picture': picture, 'choose_img': choose_img})

def pageA2(request):
    if request.method == 'POST':
        img_id = request.POST.get('img_id')
        img_ = models.Picture.objects.filter(p_id=img_id).first()
        img_.number += 1
        Y1 = (Decimal(request.POST.get('Y1')) + img_.Y1) / img_.number
        Y2 = (Decimal(request.POST.get('Y2')) + img_.Y2) / img_.number
        Y3 = (Decimal(request.POST.get('Y3')) + img_.Y3) / img_.number
        Y4 = (Decimal(request.POST.get('Y4')) + img_.Y4) / img_.number
        Y5 = (Decimal(request.POST.get('Y5')) + img_.Y5) / img_.number
        Y6 = (Decimal(request.POST.get('Y6')) + img_.Y6) / img_.number
        Y7 = (Decimal(request.POST.get('Y7')) + img_.Y7) / img_.number
        Y8 = (Decimal(request.POST.get('Y8')) + img_.Y8) / img_.number
        Y9 = (Decimal(request.POST.get('Y9')) + img_.Y9) / img_.number
        Y10 = (Decimal(request.POST.get('Y10')) + img_.Y10) / img_.number
        Y11 = (Decimal(request.POST.get('Y11')) + img_.Y11) / img_.number
        Y12 = (Decimal(request.POST.get('Y12')) + img_.Y12) / img_.number
        models.Picture.objects.filter(p_id=img_id).update(Y1=Y1, Y2=Y2, Y3=Y3, Y4=Y4, Y5=Y5, Y6=Y6,
                                                          Y7=Y7, Y8=Y8, Y9=Y9, Y10=Y10, Y11=Y11, Y12=Y12,
                                                          number=img_.number)

    img = models.Picture.objects.all()
    choose_img = models.Picture.objects.all().first()

    return render(request, "pageA2.html", {"picture": img, "choose_img": choose_img})

def pageA3(request):
    if request.method == 'POST':
        # 保存问卷
        questionnaire = models.Questionnaire(Q1=int(request.POST.get('Q1')), Q2=int(request.POST.get('Q2')),
                                             Q3=int(request.POST.get('Q3')), Q4=int(request.POST.get('Q4')),
                                             Q5=int(request.POST.get('Q5')), Q6=int(request.POST.get('Q6')),
                                             Q7=int(request.POST.get('Q7')),
                                             )
        questionnaire.save()

        # 取得试卷编号
        question = models.Questionnaire.objects.all().last()

        # 保存满意度
        img_ = models.Picture.objects.all()
        for row in img_:
            # 外键属性值，必须要传实例
            satisfaction = models.Satisfaction(answer=question, picture=row,
                                               degree=int(request.POST.get(str(row.p_id))))
            satisfaction.save()

    img = models.Picture.objects.all()
    return render(request, "pageA3.html", {"picture": img})

def pageB(request):

    # picture = models.Picture.objects.all()[0:5]
    category = models.Category.objects.all()
    choose_category = models.Category.objects.all().first()
    return render(request, "pageB.html", {"category": category, "choose_category":choose_category})

def pageC(request):
    return render(request, "pageC.html")

def find(request, page_id, img_id):
    choose_img = models.Picture.objects.filter(p_id=int(img_id)).first()
    picture = models.Picture.objects.all()
    if int(page_id) == 1:
        return render(request, "pageA11.html", {"choose_img": choose_img, "picture": picture})
    elif int(page_id) == 2:
        return render(request, "pageA2.html", {"choose_img": choose_img, "picture": picture})

def find_category(request, category_id):
    choose_category = models.Category.objects.filter(c_id=category_id).first()
    category = models.Category.objects.all()
    return render(request, "pageB.html", {"choose_category": choose_category, "category": category})