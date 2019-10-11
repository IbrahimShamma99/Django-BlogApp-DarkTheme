from .models import Post
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions
from .models import Post



# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post

#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.layout.append(
#             FormActions(
#                 HTML("""<a role="button" class="btn btn-default"
#                         href="{% url "some_cancel_url" %}">Cancel</a>"""),
#                 Submit('save', 'Submit'),
#         ))

