from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = [
  {'todo': 'make a post endpoint'}
]

@api.route('/todo')
class Todo(Resource):

    @api.doc(responses={201: "Content created"})
    def post(self):
        todos.append(api.payload)
        return 'todo added', 201

@api.route('/todo/<int:id>')
class TodoID(Resource):
    def get(self, id):
        return todos[id]

@api.route('/todos')
class Todos(Resource):
    def get(self):
        return todos

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
