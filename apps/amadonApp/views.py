from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    return render(request, "amadonApp/index.html")

def buy(request):
    items = {
    '1001': 19.99,
    '1002': 29.99,
    '1003': 4.99,
    '1004': 49.99
    }
    number = request.POST['product_id']
    name = request.POST['product_name']
    if request.method == "POST" and 'product_id' and 'product_name' and 'purchase' in request.session:
        request.session['product_name'] = name
    if 'purchase' and 'product' and 'total' and 'numbers' not in request.session:

        request.session['products'] = []
        request.session['total'] = 0
        request.session['numbers'] = 0
    else:
        request.session['purchase']=items[number] * int(request.POST['quantity'])
        productlist = request.session['products']
        request.session['total']  += (request.session['purchase'])
        request.session['numbers']  += int(request.POST['quantity'])

        productlist.append({
        'name': name,
        'price': request.session['purchase'],
        'total':request.session['total'],
        'numbers':request.session['numbers']

        })
        # print(request.session['purchase'] , name)


    productlist = []

    return redirect("/amadon")
def checkout(request):
    return render(request, "amadonApp/result.html")
def back(request):
    return redirect("/amadon")
def reset(request):
    request.session.clear()
    return redirect("/amadon")
