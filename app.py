from flask import Flask, request
from flask_restplus import Api, fields, Resource

app = Flask(__name__)
api = Api(app)

todos = []

todo_model = api.model('Todo', {
    'todo': fields.String(required=True, description='todo content')     
})

@api.route('/todos')
class Todos(Resource):
    """Add a new todo and view current todos"""
    
    @api.doc('get a list of all the todos')
    @api.marshal_list_with(todo_model, code=201)
    def get(self):
        """This is the get method for this endpoint"""
        return todos

    @api.doc('add a new todo to the list')
    @api.expect(todo_model)
    def post(self):
        """This is the post method for this endpoint"""
        todos.append(api.payload)
        return {
            'message': 'todo added'
        }, 201

@api.route('/todo/<int:id>')
@api.param('id', 'todo index')
class Todo(Resource):
    """Get or delete a todo from the list by position"""

    @api.doc('get a todo by list position')
    def get(self, id):
        rv = {'message': 'got the todo at index: %d' % id}
        rv.update(todos[id])
        return rv

    @api.doc('delete an element from todo list and return it')
    def delete(self, id):
        return {
            'message': 'the following todo was deleted',
            'todo': todos.pop(id)
        }, 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
