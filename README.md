# async-django

This repo is for exploring the capabilities of gevent with gunicorn and django. 
Example 1 shows a simple sleep example, while example 2 shows an example of accessing
DB models cooperatively. To run the application:
```
docker-compose up
```

And you can visit 
```
localhost:8000/example1/
localhost:8000/example2/
```
in multiple tabs to watch the endpoints run simultaneously even with only 1 worker.  