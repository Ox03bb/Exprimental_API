from django.http      import HttpResponse,JsonResponse
from django.shortcuts import render

from rest_framework.response    import Response
from rest_framework.views       import APIView
from rest_framework.decorators  import api_view
from rest_framework             import status

from .models import book

from .serializers   import BookSrlz
from rest_framework import generics

#? use To get data from the body of rqst request.data.get("xxxx")

#? requestd.GET


@api_view(['GET', 'POST'])
def books(rqst):
    from .models import book
    if rqst.method == 'GET':
    
        books = book.objects.all()
        sr   = BookSrlz(books,many=True)
        
        name = rqst.query_params.get("name")
        ord = rqst.query_params.get("ord") # ordring by
        
        prc  = rqst.query_params.get("prc")
        
        min_prc = rqst.query_params.get("min_prc")
        max_prc = rqst.query_params.get("max_prc")
        
        if min_prc and max_prc:
            bk = books.filter(price__gte=min_prc, price__lte=max_prc)
            sr = BookSrlz(bk,many=True) 
        
        if prc:
            bk = books.filter(price=prc)
            sr = BookSrlz(bk,many=True) 
        if name:
            bk = books.filter(title__contains=name)
            sr = BookSrlz(bk,many=True) 
            
        if ord:
            bk = books.order_by(ord)   #to search dejust add "-" befor the val ex: ?ord=-price
            sr = BookSrlz(bk,many=True) 
          
        return Response({"Books":sr.data},200)
        
    if rqst.method == 'POST':
        books = rqst.data
        sr = BookSrlz(data = books)
        
        
        if sr.is_valid():
            book.objects.create(**books)
            return Response({"msg":"Created"},201)
        
        return Response({"msg":"Erorr"},status.HTTP_400_BAD_REQUEST)
        
    
def hello(self):
    return HttpResponse("<h1>Hello User</h1>")
    



class BookView(APIView):

    def get(self, request,inp=None): 
        try:
            try:        
            
                inp   = int(inp)
                books = book.objects.get(id=inp)
                srlr  = BookSrlz(books) 
                    
                return Response({"Book":srlr.data},200)

            except:

                books = book.objects.get(title=inp)
                srlr =  BookSrlz(books)
           
                return Response({f"book":srlr.data},200) #({f"book_{books.id}":srlr.data},200) OUT Book_ID{...}
            
        except:
            return Response({"Erorr":"Book not found"},status.HTTP_404_NOT_FOUND)
            
    def put(self, request,inp): #update 
        data = request.data 
        
        try:
            bk = book.objects.get(id=inp)
            srlr =  BookSrlz(data = data)

            if srlr.is_valid():
                book.objects.filter(id=inp).update(**data)
                #srlr.save()  # OR book.objects.filter(id=inp).update(**data)
                
                return Response({"msg": "Updated" }, status.HTTP_202_ACCEPTED )
   
        except:
            
            return Response({"msg": "book Note found" }, status.HTTP_404_NOT_FOUND )
    
    def delete(self, request,inp): #delete
        data = request.data
        
        try:
            try:
                inp =inp(int)
                bk = book.objects.get(id=inp)
                book.objects.filter(id=inp).delete()
            except:
                bk = book.objects.get(title=inp)
                book.objects.filter(title=inp).delete()
                
     
            return Response({"msg": "Deleted" }, status.HTTP_202_ACCEPTED )
   
        except:
            
            return Response({"msg": "book Note found" }, status.HTTP_404_NOT_FOUND )
   

