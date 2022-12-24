from django.shortcuts import render

from . import util
import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display(request,title):
    # retreive title
    markdowny = util.get_entry(title)

    if markdowny is None:
        html='<h1>Error - Page not found</h1>'
    else:
        html=markdown.markdown(markdowny)

    return render(request,'encyclopedia/display.html',{
        "title":title,"content":html
    })
    

