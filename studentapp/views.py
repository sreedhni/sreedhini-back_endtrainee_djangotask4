from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView

from studentapp.models import School,Students


# Create list view using function based view to show list of items from the first model
def school_list(request):
    school=School.objects.all()
    return render(request,"school_list.html",{"schools":school})

# Create list view using class based view to show list of items from the second model
class StudentListView(ListView):
    model=Students
    template_name="student_list.html"
    context_object_name="students"

# Create detail view using function based view to show detail view of an item
def school_detail(request, pk):
    school = get_object_or_404(School, pk=pk)
    return render(request, "school_detail.html", {"school": school})

# Create detail view using class based view to show detail view of an item

class StudentDetailView(DetailView):
    model = Students
    template_name = 'student_detail.html'  
    context_object_name = 'student' 