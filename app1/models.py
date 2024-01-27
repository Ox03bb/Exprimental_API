from django.db import models


class book(models.Model):
    
    title  = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price  = models.DecimalField(max_digits=5,decimal_places=2)
    inv    = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    

    
class category(models.Model):
    name   = models.CharField(max_length=30)
    symbol = models.CharField(max_length=3)
    bk_ctg = models.ManyToManyField(book, through="book_ctgr")

    def __str__(self):
        return self.name

class book_ctgr(models.Model):
    b_id   = models.ForeignKey(book, on_delete=models.PROTECT)
    b_ctgr = models.ForeignKey(category, on_delete=models.PROTECT)
    
    # def __str__(self):
    #     return self.id #functritenr "book_ctgr"