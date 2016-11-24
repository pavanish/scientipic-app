from django import forms


from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text', 'sender')

class GeneExpForm(forms.Form):
	test_file = forms.CharField(max_length=1000,required=False,widget=forms.Textarea)
	input_file = forms.CharField(max_length=1000,required=False,widget=forms.Textarea)
	fastq1 = forms.CharField(max_length=1000,required=False,widget=forms.Textarea)
	fastq2 = forms.CharField(max_length=1000,required=False,widget=forms.Textarea)
	bam = forms.CharField(max_length=1000,required=False,widget=forms.Textarea)
	Bawtie=forms.BooleanField(required=False)
	MACS=forms.BooleanField(required=False)
	#file = forms.FileField()


class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()

class Upload_d3_FileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()
	
	
