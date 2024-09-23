from flask import Blueprint, jsonify, request
from .config import get_db
from bson.objectid import ObjectId

task_routes = Blueprint('tasks', __name__)

db = get_db()
tasks_collection = db['tasks']

@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(tasks_collection.find())
    for task in tasks:
        task['_id'] = str(task['_id'])  # Converte o ObjectId para string
    return jsonify(tasks)

@task_routes.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = {
        'name': data['name'],
        'deadline': data.get('deadline', None),
        'completed': False
    }
    result = tasks_collection.insert_one(task)
    task['_id'] = str(result.inserted_id)
    return jsonify(task), 201

@task_routes.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = tasks_collection.delete_one({'_id': ObjectId(task_id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'Task deleted successfully'}), 200
    else:
        return jsonify({'message': 'Task not found'}), 404
