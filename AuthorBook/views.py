from rest_framework.views import APIView
from rest_framework.response import responses
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from AuthorBook import serializers as author_book_serializer
from AuthorBook import models as author_book_model
from django.core.cache import cache

class AuthorCreateApi(APIView):
    serializer_class = author_book_serializer.AuthorSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            cache.delete("author")
            return responses({
                "messsage" : "",
                "data": {}
            },status = status.HTTP_201_CREATED)
           
        else:
            return responses({
                "messsage" : serializer.errors,
                "data": {}
            },status = status.HTTP_400_BAD_REQUEST)


class AuthorDelete(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        try:
            author_instance = author_book_model.Author.objects.get(id= data["id"])
            author_instance.delete()
            return responses({
                "messsage" : "",
                "data": {}
            },status = status.HTTP_200_OK)
        except Exception as err:
            return responses({
                "messsage" : str(err),
                "data": {}
            },status = status.HTTP_400_BAD_REQUEST)



class AuthorUpdateApi(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = author_book_serializer.AuthorSerializer
    def post(self, request):
        data = request.data.copy()
        author_instance = author_book_model.Author.objects.filter(id=data["id"]).first()
        if author_instance:
            serializer  = self.serializer_class(author_instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return responses({
                "messsage" : "",
                "data": {}
            },status = status.HTTP_200_OK)
            else:
                return responses({
                "messsage" : serializer.errors,
                "data": {}
            },status = status.HTTP_400_BAD_REQUEST)

        else:
            return responses({
                "messsage" : "No author found",
                "data": {}
            },status = status.HTTP_400_BAD_REQUEST)
        

class AuthorListApi(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = author_book_serializer.AuthorSerializer

    def get(self, request):
        
        if cache.get('author'):
            responses({
                "messsage" : "",
                "data": cache.get('author')
            },status = status.HTTP_200_OK)
        else:
            author_instance = author_book_model.Author.objects.all()
            serializer = self.serializer_class(author_instance, many=True)

            cache.set('author', serializer.data, timeout=3600)
            return responses({
                    "messsage" : "",
                    "data": serializer.data
                },status = status.HTTP_200_OK)



class BookCreateApi():
    serializer_class = author_book_serializer.BookSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            return responses({
                "messsage" : "",
                "data": {}
            },status = status.HTTP_201_CREATED)
        else:
            return responses({
                "messsage" : serializer.errors,
                "data": {}
            },status = status.HTTP_400_BAD_REQUEST)
        

class BookDelete(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        try:
            book_instance = author_book_model.Book.objects.get(id= data["id"])
            book_instance.delete()
            return responses({
                "messsage" : "",
                "data": {}
            },status = status.HTTP_200_OK)
        except Exception as err:
            return responses({
                "messsage" : str(err),
                "data": {}
            },status = status.HTTP_400_BAD_REQUEST)
        


class BookUpdate(APIView):
    serializer_class = author_book_serializer.BookSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        book_instance = author_book_model.Book.objects.filter(id=data["id"]).first()
        if book_instance:
            serializer  = self.serializer_class(book_instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return responses({
                "messsage" : "",
                "data": {}
            },status = status.HTTP_200_OK)
            else:
                return responses({
                "messsage" : serializer.errors,
                "data": {}
            },status = status.HTTP_400_BAD_REQUEST)

        else:
            return responses({
                "messsage" : "No book found",
                "data": {}
            },status = status.HTTP_400_BAD_REQUEST)
        

class BookListApi(APIView):
    serializer_class = author_book_serializer.BookSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        author_name = request.GET.get('author_name')
        publish_date_start = request.GET.get('start')
        publish_date_end = request.GET.get('end')
        genere = request.GET.get('genere')

        query_dict = {}
        if author_name:
            query_dict["author__name__icontains"] = author_name
        if publish_date_start:
            query_dict["publish_date__gte"] = publish_date_start
        if publish_date_end:
            query_dict["publish_date__lte"] = publish_date_end

        if genere:
            query_dict["genere"] = genere
        book_instances = author_book_model.Book.objects.select_related('author').filter(**query_dict)
        
        serializer = self.serializer_class(book_instances)
        return responses({
                "messsage" : "",
                "data": serializer.data
            },status = status.HTTP_200_OK)
        