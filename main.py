import datetime
import json
import jwt
from flask import Flask, jsonify, request, abort
from blockchain import Blockchain, Block
from functools import wraps
from voting import Voting

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my-secret-key'

users = [
    {
        'id': 12,
        'tc': '123456789',
        'password': 'password1',
        'votingList': [1, 3]
    },
    {
        'id': 15,
        'tc': '987654321',
        'password': 'password2',
        'votingList': [2, 4]
    }
]

votings = [
    Voting(1, "Seçim 1", "12-12-2012", "12-01-2013", ["Enes", "Muhammed", "Derya Arda"], Blockchain()),
    Voting(2, "Seçim 2", "12-12-2012", "12-01-2013", ["Enes", "Muhammed", "Derya Arda"], Blockchain()),
    Voting(3, "Seçim 3", "12-12-2012", "12-01-2013", ["Enes", "Muhammed", "Derya Arda"], Blockchain()),
    Voting(4, "Seçim 4", "12-12-2012", "12-01-2013", ["Enes", "Muhammed", "Derya Arda"], Blockchain()),
]


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(jwt=token, key=app.config['SECRET_KEY'], algorithms=['HS256', ])
            current_user = data['user']
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/api/login', methods=['POST'])
def login():
    tc = request.form.get('tc')
    password = request.form.get('password')
    for user in users:
        if user['tc'] == tc and user['password'] == password:
            token = jwt.encode({"user": user}, app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'token': token}), 200

    return jsonify({'error': 'Invalid username or password'}), 401


@app.route('/api/lastBlock/<int:votingId>', methods=['GET'])
@token_required
def get_last_block(current_user, votingId):
    global temp
    for voting in votings:
        if voting.id == votingId:
            temp = voting
    return jsonify(temp.blockchain.getLastBlock().toJson())


@app.route('/api/addBlock', methods=['POST'])
@token_required
def add_block(current_user):
    for voting in votings:
        if voting.id == int(request.form.get("votingId")):
            voting.blockchain.add_block(request.form.get("vote"))

    return jsonify({"response": True})


@app.route('/api/getVotingList', methods=['GET'])
@token_required
def get_voting_list(current_user):
    filteredVoting = []
    for voting in votings:
        if voting.id in current_user['votingList']:
            filteredVoting.append(voting.toJson())
    return jsonify({'voting': filteredVoting})


if __name__ == '__main__':
    app.run(host="192.168.0.14")
