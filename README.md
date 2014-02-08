Django-rest-demo
================

step_1 Simple api for OriginationPoint model.
----------------


get: curl http://127.0.0.1:8000/op/ <br>
create: curl -X POST http://127.0.0.1:8000/op/ -d '{"name": "op1", "login": "1111", "password": "2222"}' -H "Content-Type: application/json" <br>
retrieve: curl http://127.0.0.1:8000/op/1 <br>
update: curl -X PUT http://127.0.0.1:8000/op/1 -d '{"name": "op1", "login": "newlogin", "password": "newpass"}' -H "Content-Type: application/json" <br>


step_2 Use APIView class from django-rest-framework
----------------
