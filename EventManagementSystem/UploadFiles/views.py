from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import File
from django.db.models import Q

# Create your views here.

def upload(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name,uploaded_file)
		context['url'] = fs.url(name)	
	return render(request, 'uploadfile/upload.html', context)



def file_list(request):
	query = request.GET.get("q",None)
	files = File.objects.all()
	if query is not None:
		files=files.filter(
			Q(title__icontains=query) |
			Q(file_type__icontains=query)
			)

	return render(request, 'uploadfile/file_list.html',{
			'files': files
		})

#pagination 
def  file_objects_pagination(request,PAGENO,SIZE):
	skip = SIZE *(PAGENO -1)
	files= File.objects.all() [skip:(PAGENO * SIZE)]
	dict = {
			"file":list(File.values("title","name"))
		}
	return JsonResponse(dict)	

def upload_file(request):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('file_list')

	else:
		form = FileForm()
	return render(request, 'uploadfile/upload_file.html',{'form':form})


def delete_file(request, pk):
	if request.method == 'POST':
		file = File.objects.get(pk = pk)
		file.delete()
	return redirect('file_list')


