from django.shortcuts import render
from django.http import HttpResponse
from .models import Report
from .tools import build

# Create your views here.
def index(request):
    #query

    Report.objects.create(title="AXR", entityID=2000, creator="Harry", is_Current=False)
    Report.objects.create(title="RRR", entityID=1011, creator="Nicole", is_Current=False) 

    result = Report.objects.all()
    print(type(result))
    build()

    return HttpResponse(f"""<h1>Welcome to Revera Scripts</h1>
        <div>{result}
        <p>Project Listing App</p>
        </div>


    """)