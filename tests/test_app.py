import pytest
from app import app
from flask import Flask, jsonify, request 

@pytest.fixture
def client(): 
  app.config ['TESTING'] = True
  with app.test_client() as client: 
    yield client

def test_home(client):
  #STEP 2: ACT = Faire la requête
  response = client.get('/') #Tester endpoint GET / 
  #STEP 3: ASSERT = Verifier resultat 
  assert response.status_code == 200  #verifier le statut code 
  data = response.get_json() # Récupérer le JSON
  assert data['message'] == 'Task Manager API'
  assert data['status'] == 'running'

def test_health(client):
  response = client.get('/health')
  assert response.status_code == 200
  data = response.get_json()
  assert data['status'] == 'healthy'

def test_get_task_empty(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert data['tasks'] == []

def test_add_task(client):
   response = client.post('/tasks', json={'task': 'Test Jenkins'})
   data = response.get_json()
   assert data['message'] == 'Task added'

