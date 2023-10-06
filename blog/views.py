from datetime import date
from django.shortcuts import render

posts =[
    {
        "slug":"hike-in-the-mountains",
        "image": "Purnendu.png",
        "author": "Purnendu",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Obcaecati, omnis nesciunt. Tenetur eius fugiat, culpa recusandae provident placeat in laborum.",
        "content": """
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Obcaecati, omnis nesciunt. Tenetur eius fugiat, culpa recusandae provident placeat in laborum.

Lorem ipsum dolor sit amet consectetur, adipisicing elit. Obcaecati, omnis nesciunt. Tenetur eius fugiat, culpa recusandae provident placeat in laborum.

Lorem ipsum dolor sit amet consectetur, adipisicing elit. Obcaecati, omnis nesciunt. Tenetur eius fugiat, culpa recusandae provident placeat in laborum.
"""

    }
]

# Create your views here.
def starting_page(request):
    return render (request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")