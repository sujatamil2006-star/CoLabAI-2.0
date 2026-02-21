from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import json

app = Flask(__name__)

# In-memory storage for projects
projects = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/create-project', methods=['POST'])
def create_project():
    data = request.json
    project_id = str(len(projects) + 1)
    
    projects[project_id] = {
        'id': project_id,
        'name': data['projectName'],
        'deadline': data['deadline'],
        'members': data['members'],
        'status': 'planning',
        'created_at': datetime.now().isoformat(),
        'tasks': [],
        'milestones': []
    }
    
    return jsonify({'project_id': project_id, 'message': 'Project created'})

@app.route('/api/assign-tasks/<project_id>', methods=['POST'])
def assign_tasks(project_id):
    if project_id not in projects:
        return jsonify({'error': 'Project not found'}), 404
    
    project = projects[project_id]
    members = project['members']
    
    tasks = [
        {'name': 'Requirements & Planning', 'duration': 3, 'skills': ['planning', 'analysis']},
        {'name': 'Design & Architecture', 'duration': 5, 'skills': ['design', 'architecture']},
        {'name': 'Frontend Development', 'duration': 10, 'skills': ['frontend', 'javascript']},
        {'name': 'Backend Development', 'duration': 10, 'skills': ['backend', 'database']},
        {'name': 'Testing & QA', 'duration': 5, 'skills': ['testing', 'qa']},
        {'name': 'Documentation', 'duration': 3, 'skills': ['documentation', 'writing']},
    ]
    
    assigned_tasks = []
    member_workload = {m['name']: 0 for m in members}
    
    for task in tasks:
        best_member = min(member_workload, key=member_workload.get)
        assigned_tasks.append({
            'name': task['name'],
            'assigned_to': best_member,
            'duration_days': task['duration'],
            'status': 'pending',
            'skills_required': task['skills']
        })
        member_workload[best_member] += task['duration']
    
    project['tasks'] = assigned_tasks
    project['status'] = 'planning'
    
    return jsonify({'tasks': assigned_tasks, 'workload': member_workload})

@app.route('/api/create-timeline/<project_id>', methods=['POST'])
def create_timeline(project_id):
    if project_id not in projects:
        return jsonify({'error': 'Project not found'}), 404
    
    project = projects[project_id]
    deadline = datetime.fromisoformat(project['deadline'])
    start_date = datetime.now()
    
    milestones = [
        {'name': '📋 Planning Complete', 'date': (start_date + timedelta(days=3)).isoformat()},
        {'name': '🎨 Design Complete', 'date': (start_date + timedelta(days=8)).isoformat()},
        {'name': '💻 Development Phase 1', 'date': (start_date + timedelta(days=18)).isoformat()},
        {'name': '✅ Testing Complete', 'date': (start_date + timedelta(days=23)).isoformat()},
        {'name': '📚 Documentation & Delivery', 'date': deadline.isoformat()},
    ]
    
    project['milestones'] = milestones
    
    return jsonify({'milestones': milestones})

@app.route('/api/project/<project_id>', methods=['GET'])
def get_project(project_id):
    if project_id not in projects:
        return jsonify({'error': 'Project not found'}), 404
    return jsonify(projects[project_id])

@app.route('/api/update-task-status/<project_id>/<task_name>', methods=['POST'])
def update_task_status(project_id, task_name):
    if project_id not in projects:
        return jsonify({'error': 'Project not found'}), 404
    
    data = request.json
    project = projects[project_id]
    
    for task in project['tasks']:
        if task['name'] == task_name:
            task['status'] = data['status']
            task['progress'] = data.get('progress', 0)
            break
    
    return jsonify({'message': 'Task updated'})

if __name__ == '__main__':
    print("🚀 Starting Flask app on http://localhost:5000")
    app.run(debug=True)
    
