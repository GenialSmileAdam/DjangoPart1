from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem

# def say_hello(request):
    # query set is lazy , it is evaluated at a later time 
    # try:
    #     product = Product.objects.get(pk=2000)
    # except ObjectDoesNotExist as e:
    #     return JsonResponse({
    #         'Response':'404', 
    #         'error':f'exception {e}',
    #     })

    # filtering objects
    # query_set = Product.objects.filter(unit_price__gt=91)

    # getting a range of objects
    # query_set = Product.objects.filter(unit_price__range= (20, 100))
    # result = [product.title for product in query_set]
    # result = {product.title:product.unit_price for product in query_set}

    # looking up objects based on relationships 
    # query_set =  Product.objects.filter(collection__id__lt=6)

    # looking up objects based on attribute value,
    #  Usually, A lookup that starts with 'i' is the case-insensitive version
    # query_set =  Product.objects.filter(title__icontains ='coffee')

    # looking up objects base on what that attribute value starts with 
    # query_set =  Product.objects.filter(title__istartswith ='coffee')

    # looking up based on year
    # query_set =  Product.objects.filter(l ast_update__year = 2020)

    # # Chaining filters using Additional Kwargs
    # query_set =  Product.objects.filter(inventory__lt= 10, unit_price__lt =20)
     
     
    # # Chaining filters using Additional filters
    # query_set =  Product.objects.filter(inventory__lt= 10).filter(unit_price__lt =20)
     
    # Looking up objects based on one or more operations (OR operation)
    # query_set = Product.objects.filter(Q(inventory__lt =10) & ~Q(unit_price__lt=20 ))
    # query_set = Product.objects.filter(Q(inventory__lt =10) | Q(unit_price__lt=20 ))

    # How to reference another field 
    # query_set =  Product.objects.filter(inventory= F('unit_price')) 
    # query_set =  Product.objects.filter(inventory= F('collection__id')) #referencing another field in a related record

    # sorting a query by a field 
    # query_set =  Product.objects.order_by('title') #ascending order
    # query_set =  Product.objects.order_by('-title') #descending order
    # query_set =  Product.objects.order_by('-unit_price', 'title').reverse()
    # query_set =  Product.objects.order_by('-unit_price', 'title')
    # query_set =  Product.objects.order_by('unit_price')

    # query_set = Product.objects.filter(collection__id = 6).order_by('unit_price').reverse()

    # Getting an object based on an order, earliest and latest do not return a query set
    # product = Product.objects.latest('-unit_price')
    # product = Product.objects.earliest('-unit_price')


    

    # return render(request, 'home.html',
    #               {'result':list(query_set),
    #                'name':'Jason'})
    # return render(request, 'home.html',
    #               {'result':product.title,
    #                'name':'Jason'})




def data_query(request):
    # limiting objects 
    # query_set = Product.objects.all()[:5]

    #getting an object with specified columns, returns a dictionary
    query_set = Product.objects.values('id', 'title', 'collection__title')

    #getting an object with specified columns, returns a list
    query_set = Product.objects.values_list('id', 'title', 'collection__title')

    return render(request, 'home.html',
                  {'result':list(query_set),
                   'name':'Jason'})

# def ordered_items(request):
#     """Returns an ordered collection of Products 
#     that have been ordered """
#     query_set = Product.objects.filter(orderitem__isnull = False).distinct()
#     ordered_set = query_set.order_by('title')
    
#     return render(request, 'query.html',
#                   {'result':list(ordered_set),
#                    'name':'Jason'})
# def ordered_items(request):
#     """Returns an ordered collection of Products 
#     that have been ordered """
#     query_set = OrderItem.objects.filter(product__isnull = False)
#     ordered_set = query_set.order_by('product__title')
    
#     return render(request, 'query.html',
#                   {'result':list(ordered_set),
#                    'name':'Jason'})

# solution
def ordered_items(request):
    """Returns an ordered collection of Products 
    that have been ordered """
    
    query_set = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')
    
    
    
    return render(request, 'query.html',
                  {'result':list(query_set),
                   'name':'Jason'})