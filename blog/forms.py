from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'email',
        ]

        widgets={
            'title': forms.TextInput(
                attrs= {
                    'class' : 'form',
                    'placeholder':'Masukkan Judul',
                }
            )
        }

    # alamatc = forms.CharField(
    #     label = 'Alamat',
    #     widget = forms.TextInput(
    #         attrs={
    #             'class':'field padding-bottom--24',
    #             'type':'alamat',
    #             'placeholder':'Masukkan Alamat',
    #         }
    #     )
    # )
    # tgl_lahirc = forms.CharField(
    #     label = 'Tanggal Lahir',
    #     widget = forms.TextInput(
    #         attrs={
    #             'class':'field padding-bottom--24',
    #             'type':'tgl_lahir',
    #             'placeholder':'Masukkan Tanggal Lahir',
    #         }
    #     )
    # )
    # emailc = forms.EmailField(
    #     label = 'Email',
    #     widget = forms.TextInput(
    #         attrs={
    #             'class':'field padding-bottom--24',
    #             'type':'email',
    #             'placeholder':'Masukkan Email',
    #         }
    #     )
    # )
   