from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, User, Student, Note

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# -------------------- AUTH --------------------

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Nom d'utilisateur déjà pris"}), 400
    user = User(username=data['username'], role=data.get('role', 'user'))
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Utilisateur créé"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        return jsonify({"message": "Connexion réussie", "username": user.username, "role": user.role}), 200
    return jsonify({"message": "Nom d'utilisateur ou mot de passe incorrect"}), 401

# -------------------- ROUTES STUDENTS --------------------

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': s.id, 'name': s.name} for s in students])

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    student = Student(name=data['name'])
    db.session.add(student)
    db.session.commit()
    return jsonify({'id': student.id, 'name': student.name}), 201

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Étudiant supprimé'}), 200

# -------------------- ROUTES NOTES --------------------

@app.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return jsonify([
        {'id': n.id, 'score': n.score, 'student_id': n.student_id, 'student_name': n.student.name}
        for n in notes
    ])

@app.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    note = Note(score=data['score'], student_id=data['student_id'])
    db.session.add(note)
    db.session.commit()
    return jsonify({'id': note.id, 'score': note.score, 'student_id': note.student_id}), 201

@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({'message': 'Note supprimée'}), 200

# -------------------- ROUTE MOYENNES --------------------

@app.route('/averages', methods=['GET'])
def get_averages():
    students = Student.query.all()
    averages = {}
    for s in students:
        if s.notes:
            avg = sum(n.score for n in s.notes)/len(s.notes)
        else:
            avg = 0
        averages[s.name] = round(avg, 2)
    return jsonify(averages)

# -------------------- LANCEMENT --------------------

if __name__ == '__main__':
    app.run(debug=True)
