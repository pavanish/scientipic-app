from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# from .models import Post
from .models import Comment
from .forms import CommentForm
from .forms import GeneExpForm
from .forms import UploadFileForm
from .forms import Upload_d3_FileForm


from .filescript import handle_uploaded_file, handle_csv_file

#import pandas as pd


def Index(request):
	comments = Comment.objects.all()
	return render(request,'blog/index.html',{'comments':comments})

def Chip_seq(request):
	return render(request,'blog/blogChip.html',{})
# def post_list(request):
# 	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# 	return render(request, 'blog/post_list.html', {'posts':posts})
#
# def post_detail(request,pk):
# 	post=get_object_or_404(Post,pk=pk)
# 	comments=Comment.objects.filter(pk=pk)
# 	return render(request, 'blog/post_detail.html',{'post':post, 'comments':comments})
# '''
# def post_comment(request):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             post.save()
#             return redirect('blog.views.post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/post_detail.html', {'form': form})
# '''
#

# Create your views here.
# view for geneExp
def add_comment(request):
    #post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            #comment.post = post
            comment.save()
            return render(request,'blog/show_comment.html')
            
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})
def GeneExp_view(request):
	if request.method== 'POST':
		form= GeneExpForm(request.POST)
		if form.is_valid():
			f1=form.cleaned_data['fastq1']
			f1=f1.split()
			f2=form.cleaned_data['fastq2']
			f2=f2.split()
			f3=form.cleaned_data['bam']
			f3=f3.split()
			flist=zip(f1,f2,f3)
			f4=form.cleaned_data['test_file']
			f4=f4.split()
			f5=form.cleaned_data['input_file']
			f5=f5.split()
			macslist=zip(f4,f5)
			files_sort=list(set([e for l in macslist for e in l]))
			
			Bawtie=form.cleaned_data['Bawtie']
			MACS=form.cleaned_data['MACS']
			
			bawtie=[('bowtie2 -p 2 -N 1 -q ~/Genomes/hg19/hg19 -1'+' ' + ' ' +'~/Desktop/chip_seq_proj/'+ f[0]+' '+  '-2'+' ' + ' '+ '~/Desktop/chip_seq_proj/' + f[1] + '|samtools view -bS - > /bamfiles/'+f[2]) for f in flist]
			sort=[('samtools sort ~/Desktop/chip_seq_proj/bamfiles/' + f + ' ' +'~/Desktop/chip_seq_proj/sorted_files/sort_' +f.split('.')[0] ) for f in files_sort]
			rmdup=[('samtools rmdup ~/Desktop/chip_seq_proj/sorted_files/sort_'  +f + ' ' +'~/Desktop/chip_seq_proj/rmdup_index_files/rmdup_sort_' + f ) for f in files_sort]
			index=[('samtools index ~/Desktop/chip_seq_proj/rmdup_index_files/rmdup_sort_' + f ) for f in files_sort]
			macs=[('MACS2' +' ' + 'callpeak' + ' ' + '-t' + ' ' + '~/Desktop/chip_seq_proj/rmdup_index_files/rmdup_sort_' + item[0] + ' ' + '-c' + ' ' + '~/Desktop/chip_seq_proj/rmdup_index_files/rmdup_sort_' + item[1] + ' ' + '-f BAMPE -g hs --outdir ~/Desktop/chip_seq_proj/MACS_results -n' + ' ' +  item[0].split('.')[0] + '_vs_' + item[1].split('.')[0] + ' ' + '-B -q 0.05') for item in macslist]

			
			
			
			
			#macs_list=MACS.split()
			#datalist=handle_uploaded_file(request.FILES['file'])
			if Bawtie==True and MACS==False:
				script= bawtie
			elif MACS==True and Bawtie==False:
				script= sort+rmdup+index+macs
			elif MACS==True and Bawtie ==True:
				script= bawtie+sort+rmdup+index+macs
			else:
				script="Fill the form correctly and choose one or both"
			return render(request, 'blog/script.html',{'script':script})
	else:
		form=GeneExpForm()
		return render(request, 'blog/script_form.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
			f=request.FILES['file']
			geneName = handle_csv_file(f)
			Name,Length=geneName
			mm=Length.mean()
			return render(request, 'blog/file_data.html',{'Name':Name,'mm':mm})

    else:
        form = UploadFileForm()
        return render(request, 'blog/upload_form.html', {'form': form})

# d3_file_data is not working yet, trying to get csv file from upload and pass to d3
def d3_file_data(request):
    if request.method == 'POST':
        form = Upload_d3_FileForm(request.POST, request.FILES)

        if form.is_valid():
			file=request.FILES['file']
			return render(request, 'blog/d3_data.html',{'f':file})
    else:
    	form=Upload_d3_FileForm()
    	return render(request,'blog/upload_d3_form.html', {'form': form})

def file_data(request):
    datalist=handle_uploaded_file(request.FILES['file'])
    return render(request, 'blog/file_data.html',{'datalist':datalist})

def d3_data(request):
    return render(request, 'blog/d3_data.html',{'file':'/static/data/flare.csv'})
