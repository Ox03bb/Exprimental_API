from rest_framework import serializers
from .models import book,category,book_ctgr

from django.contrib.auth.models import User

class UserSrlz(serializers.Serializer):
    id       = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    
    password = serializers.CharField(write_only=True)
    # email = serializers.EmailField(NULL=True)
    


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class book_ctgrSrlz(serializers.ModelSerializer):
    class Meta:
        model = book_ctgr
        fields = '__all__'

class BookSrlz(serializers.Serializer):
    id      = serializers.IntegerField()
    title   = serializers.CharField(max_length=255)
    author  = serializers.CharField(max_length=255)
    price   = serializers.DecimalField(max_digits=5,decimal_places=2)
    inv     = serializers.BooleanField(default=False,write_only=True) #icant read this part kyn wci #?read_only
    tax     = serializers.SerializerMethodField(method_name = "get_tax") #method_name = "get_tax"
    #? price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')

    # category = serializers.HyperlinkedRelatedField(
    #     queryset = category.objects.all(),
    #     view_name='category-detail'
    # )       
    #! Category= CategorySerializer(many=True,read_only=True)
    # bk_cg_id= serializers.SerializerMethodField()
   
    
    # def get_ctgr(self,obj): 
    #     bk_cg_id = book_ctgr.objects.get(id=self.id)
    #     print(bk_cg_id)
    
    
    def get_tax(self,obj):  #Must be name the func get_xxx
        tax:float
        prc:float
        
        try:    
            
            # prc = obj.get('price') # hadi sa3at ysraw fiha problems tweli ma t getsh e data so ==> plan B
            prc = getattr(obj, 'price', None)
            
            if prc:
                tax = prc/10
                return tax
            return None
        except :
            return None  # Return None if t

# class BookSrlz(serializers.ModelSerializer):
#     class Meta:
#         model = book
#         fields = "__all__"