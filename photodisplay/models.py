from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chinese_name = models.CharField(max_length=128,default='',verbose_name="中文名")
    image = models.ImageField(upload_to='photos/%Y/%m/%d/',default='',verbose_name="头像")
    isauthor = models.BooleanField(default=False,verbose_name="是否作者")
    school = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name="学校")
    college = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name="学院")
    major = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name="专业")
    email = models.EmailField(default='',verbose_name="电子邮箱")
    phone = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="电话")
    qq = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="qq")
    wechat = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="微信")
    content = models.TextField(verbose_name="自我介绍",default='')
    class Meta:
        verbose_name = verbose_name_plural = "用户信息"
    def __str__(self):
        return self.user.username
    @classmethod
    def author(self):
        return UserProfile.objects.get(isauthor=True)

    def info(self):
        return Honor.objects.filter(owner_id=self.id).filter(status=Honor.STATUS_NORMAL).get(info_catogory=Honor.STATUS_INFO)

    def desc(self):
        return Honor.objects.filter(owner_id=self.id).filter(status=Honor.STATUS_NORMAL).filter(info_catogory=Honor.STATUS_DESC)

    def honor(self):
        return Honor.objects.filter(owner_id=self.id).filter(status=Honor.STATUS_NORMAL).filter(info_catogory=Honor.STATUS_HONOR)

    def picture(self):
        return HomePhoto.objects.filter(owner_id=self.id).filter(status=HomePhoto.STATUS_NORMAL)

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name = models.CharField(max_length=50,verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    owner = models.ForeignKey(User,verbose_name="作者",on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    def pictures(self):
        return Picture.objects.filter(category=self).filter(status=Picture.STATUS_HOME)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = verbose_name_plural = "分类"

class Picture(models.Model):
    STATUS_HOME = 1
    STATUS_CATEGORY = 2
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_HOME,'主页显示'),
        (STATUS_CATEGORY,'分类页面显示'),
        (STATUS_DELETE,'不显示'),
    )
    owner = models.ForeignKey(User,verbose_name="用户",default='',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name="名称")
    category = models.ForeignKey(Category,verbose_name="分类",on_delete=models.CASCADE)
    content = models.TextField(verbose_name="正文")
    content_html = models.TextField(verbose_name="正文html代码",blank=True,editable=False)
    camera = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="相机及型号")
    focus = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="对焦参数")
    aperture = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="光圈参数")
    shutter_time = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="快门时间")
    sensitive = models.CharField(max_length=100, null=True, blank=True, default='',verbose_name="感光参数")
    status = models.PositiveIntegerField(default=STATUS_HOME,choices=STATUS_ITEMS,verbose_name="展示状态")
    image = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name="图片")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        verbose_name = verbose_name_plural = "照片"
        ordering = ['-created_time']

    def comments(self):
        return Comment.objects.filter(target=str(self.id)).filter(status=Comment.STATUS_NORMAL).order_by('-created_time')
    def __str__(self):
        return self.name


class HomePhoto(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'显示'),
        (STATUS_DELETE,'不显示'),
    )
    owner = models.ForeignKey(UserProfile,verbose_name="用户",default='',on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name="标题",default='')
    subtitle = models.CharField(max_length=100,verbose_name="子标题",default='')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="展示状态")
    image = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name="图片")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        verbose_name = verbose_name_plural = "主页个人照片"
    def __str__(self):
        return self.title

class Honor(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'显示'),
        (STATUS_DELETE,'不显示'),
    )
    STATUS_INFO = 2
    STATUS_DESC = 1
    STATUS_HONOR = 0 
    STATUS_CONTENT = (
        (STATUS_INFO ,'主页超长介绍'),
        (STATUS_DESC ,'主页中间短事迹描述'),
        (STATUS_HONOR,'荣誉'),
    )
    owner = models.ForeignKey(UserProfile,verbose_name="用户",default='',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name="名字",default='')
    content = models.TextField(verbose_name="正文内容")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="展示状态")
    info_catogory = models.PositiveIntegerField(default=STATUS_DESC,choices=STATUS_CONTENT,verbose_name="分类")
    class Meta:
        verbose_name = verbose_name_plural = "主页文字信息"
    def __str__(self):
        if self.name!="":
            return self.name
        else:
            if len(self.content)>15:
                return self.content[:15]
            else:
                self.content

class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0 
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    target = models.CharField(max_length = 100 ,verbose_name="评论目标")
    content = models.CharField(max_length = 2000,verbose_name="内容")
    nickname = models.CharField(max_length=50,verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "评论"
    
    def __str__(self):
        if len(self.content)>15:
            return self.nickname+" 内容："+self.content[:15]
        else:
            return self.nickname+" 内容："+self.content
    @classmethod        
    def get_by_target(cls,target):
        return cls.objects.filter(target=target,status=cls.STATUS_NORMAL)