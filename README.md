step 1:
python3 -m venv venv
source venv/bin/activate

step : 2
pip install -r requirements.txt

step 3: python manage.py runserver

step 4: celery -A core.celery worker -l info


Api

1 . Author create : author/create
    request type : post
    body : {
          "name" : "mr x",
          "date_of_birth": "1990-01-02" 
    }
2.Author delele: author/delete
    request type : post
        body : {
              "id" : 1
        }
3. Author update: author/update
   request type : post
    body : {
          "id": 1,
          "name" : "mr x",
          "date_of_birth": "1990-01-02" 
    }

4. Author list: author/list
   request type : get


5 . Book create : book/create
    request type : post
    body : {
          "author" : 1,
          "title": "this is title",
          "publish_date": "1990-01-02" ,
          "genre": "genre"
    }

6 . Book delete : book/delete
      request type : post
      body : {
            "author" : 1
      }

7 . Book create : book/update
    request type : post
    body : {
           "id" : 1,
          "author" : 1,
          "title": "this is title",
          "publish_date": "1990-01-02" ,
          "genre": "genre"
    }

7 . Book list : book/list
    request type : get
