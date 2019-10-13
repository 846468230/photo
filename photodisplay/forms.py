from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label= '昵称',
        max_length=50,
        widget = forms.widgets.Input(
            attrs = {'class':'form-control rounded-0 border-top-0 border-right-0 border-left-0','placeholder':"昵称"}
        )
    )
    email = forms.CharField(
        label = 'Email',
        max_length=50,
        widget=forms.widgets.EmailInput(
            attrs={'class':'form-control rounded-0 border-top-0 border-right-0 border-left-0','placeholder':"邮箱"}
        )
    )
    content = forms.CharField(
        label='内容',
        max_length=500,
        widget = forms.widgets.Textarea(
            attrs={'rows':6,'cols':60,'class':'form-control rounded-0 border-top-0 border-right-0 border-left-0','style':'margin-top: 0px; margin-bottom: 0px; height: 182px;','placeholder':"内容"}
        )
    )
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content)<10:
            raise forms.ValidationError('内容长度怎么能这么短呢！')
        #content = mistune.markdown(content)
        return content
    
    class Meta:
        model = Comment
        fields = ['nickname','email','content']