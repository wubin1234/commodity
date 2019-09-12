from django.db import models

# Create your models here.

class Questionnaire(models.Model):
    """调查问卷表"""

    q_id = models.AutoField(primary_key=True)
    Q1 = models.IntegerField(default=0)
    Q2 = models.IntegerField(default=0)
    Q3 = models.IntegerField(default=0)
    Q4 = models.IntegerField(default=0)
    Q5 = models.IntegerField(default=0)
    Q6 = models.IntegerField(default=0)
    Q7 = models.IntegerField(default=0)
    Q8 = models.IntegerField(default=0)
    Q9 = models.IntegerField(default=0)
    Q10 = models.IntegerField(default=0)
    Q11 = models.IntegerField(default=0)
    Q12 = models.IntegerField(default=0)
    Q13 = models.IntegerField(default=0)
    Q14 = models.IntegerField(default=0)
    Q15 = models.IntegerField(default=0)
    Q16 = models.IntegerField(default=0)
    Q17 = models.IntegerField(default=0)
    Q18 = models.IntegerField(default=0)
    Q19 = models.IntegerField(default=0)
    Q20 = models.IntegerField(default=0)
    Q21 = models.IntegerField(default=0)
    Q22 = models.IntegerField(default=0)
    Q23 = models.IntegerField(default=0)
    Q24 = models.IntegerField(default=0)
    Q25 = models.IntegerField(default=0)
    Q26 = models.IntegerField(default=0)
    Q27 = models.IntegerField(default=0)
    Q28 = models.IntegerField(default=0)
    Q29 = models.IntegerField(default=0)
    Q30 = models.IntegerField(default=0)
    Q31 = models.IntegerField(default=0)
    Q32 = models.IntegerField(default=0)
    Q33 = models.IntegerField(default=0)
    Q34 = models.IntegerField(default=0)
    Q35 = models.IntegerField(default=0)

class Picture(models.Model):
    """图片表"""

    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=32)
    img_url = models.ImageField(upload_to='img/', blank=True, null=True)
    AX = models.DecimalField(max_digits=6, decimal_places=3)
    HL = models.DecimalField(max_digits=6, decimal_places=3)
    WL = models.DecimalField(max_digits=6, decimal_places=3)
    ct1 = models.DecimalField(max_digits=6, decimal_places=3)
    c01 = models.DecimalField(max_digits=6, decimal_places=3)
    ct2 = models.DecimalField(max_digits=6, decimal_places=3)
    c02 = models.DecimalField(max_digits=6, decimal_places=3)
    ct3 = models.DecimalField(max_digits=6, decimal_places=3)
    c03 = models.DecimalField(max_digits=6, decimal_places=3)
    ct4 = models.DecimalField(max_digits=6, decimal_places=3)
    c04 = models.DecimalField(max_digits=6, decimal_places=3)
    ct5 = models.DecimalField(max_digits=6, decimal_places=3)
    c05 = models.DecimalField(max_digits=6, decimal_places=3)
    ct6 = models.DecimalField(max_digits=6, decimal_places=3)
    c06 = models.DecimalField(max_digits=6, decimal_places=3)
    ct7 = models.DecimalField(max_digits=6, decimal_places=3)
    c07 = models.DecimalField(max_digits=6, decimal_places=3)
    ct8 = models.DecimalField(max_digits=6, decimal_places=3)
    c08 = models.DecimalField(max_digits=6, decimal_places=3)
    pt = models.DecimalField(max_digits=6, decimal_places=3)
    p01 = models.DecimalField(max_digits=6, decimal_places=3)
    p02 = models.DecimalField(max_digits=6, decimal_places=3)
    p03 = models.DecimalField(max_digits=6, decimal_places=3)
    p04 = models.DecimalField(max_digits=6, decimal_places=3)
    p05 = models.DecimalField(max_digits=6, decimal_places=3)
    p06 = models.DecimalField(max_digits=6, decimal_places=3)
    AT = models.DecimalField(max_digits=6, decimal_places=3)
    QW = models.DecimalField(max_digits=6, decimal_places=3)
    QP = models.DecimalField(max_digits=6, decimal_places=3)
    QC = models.DecimalField(max_digits=6, decimal_places=3)
    HT = models.DecimalField(max_digits=6, decimal_places=3)
    AW = models.DecimalField(max_digits=6, decimal_places=3)
    AH = models.DecimalField(max_digits=6, decimal_places=3)
    QW1 = models.DecimalField(max_digits=6, decimal_places=3)
    Y1 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    Y2 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    Y3 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    Y4 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    Y5 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    Y6 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    Y7 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    Y8 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    Y9 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    Y10 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    Y11 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    Y12 = models.DecimalField(max_digits=6, decimal_places=3, default=0.0)
    number = models.IntegerField(default=0)

class Satisfaction(models.Model):
    """喜好程度表"""

    s_id = models.AutoField(primary_key=True)
    answer = models.ForeignKey("Questionnaire", on_delete=models.CASCADE, to_field="q_id")
    picture = models.ForeignKey("Picture", on_delete=models.CASCADE, to_field="p_id")
    degree = models.IntegerField(default=0)

class Category(models.Model):
    """偏好类别表"""

    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=32)
    describe = models.TextField(max_length=512)
    preference1 = models.TextField(max_length=32)
    preference2 = models.TextField(max_length=32)
    preference3 = models.TextField(max_length=32)
    preference4 = models.TextField(max_length=32)
    preference5 = models.TextField(max_length=32)
    preference6 = models.TextField(max_length=32)
    p_img1 = models.CharField(max_length=64, default="../static/img/013-瑞士风-U700-p.jpg")
    p_img2 = models.CharField(max_length=64, default="../static/img/013-瑞士风-U700-p.jpg")
    p_img3 = models.CharField(max_length=64, default="../static/img/013-瑞士风-U700-p.jpg")
    p_img4 = models.CharField(max_length=64, default="../static/img/013-瑞士风-U700-p.jpg")
    p_img5 = models.CharField(max_length=64, default="../static/img/013-瑞士风-U700-p.jpg")