from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name' : 'komal vaishnav' , 'age' : 21},
        {'name' : 'ayush suthar' , 'age' : 22},
        {'name' : 'chanchal vaishnav' , 'age' : 20},
        {'name' : 'phool' , 'age' : 2}
    ]

    for people in peoples:
        if people['age']:
            print('yes')

#     text = """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero doloremque quisquam nihil. Fugiat optio voluptatem dolor maxime et laborum itaque assumenda ipsum, voluptatibus dolores reiciendis, at quo enim. Accusamus, unde nihil esse dicta molestias ullam, placeat ex odio, vero illum ratione quia repudiandae. Sequi impedit consequatur nesciunt, distinctio, enim voluptates amet odit voluptatum obcaecati tempore laboriosam reprehenderit vero, magni pariatur. Saepe aperiam qui soluta libero corporis, voluptatem recusandae nemo neque iste ullam voluptates delectus doloribus deleniti illum deserunt cum nam. Maiores vitae suscipit ipsam minima sapiente deserunt non dolorum cupiditate voluptas! Atque nostrum rem totam! Minima ad quia ut consequatur?
# """
    vegetables = ['tomato','pumpkin','potato']

    # for people in peoples:
    #     print(people)
    return render(request, "home/index.html", context = {'page' : 'django 2026 tutorial', 'peoples' : peoples})

def about(request):
   context = {'page' : 'about'}
   return render(request, "home/about.html",context)

def contact(request):
   context = {'page' : 'contact'}
   return render(request, "home/contact.html", context)



def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>hey this is success page.</h1>")