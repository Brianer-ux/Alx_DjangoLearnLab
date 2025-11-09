CREATE



from bookshelf.models import Book



book = Book.objects.create(

title="1984",

author="George Orwell",

publication\_year=1949

)



book



Output:

<Book: 1984 by George Orwell>



RETRIEVE



Book.objects.all()



Output:

<QuerySet \[<Book: 1984 by George Orwell>]>



book = Book.objects.get(title="1984")

book.title, book.author, book.publication\_year



Output:

('1984', 'George Orwell', 1949)



UPDATE



book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four"

book.save()



book



Output:

<Book: Nineteen Eighty-Four by George Orwell>



DELETE



book = Book.objects.get(title="Nineteen Eighty-Four")

book.delete()



Output:

<QuerySet \[]>

