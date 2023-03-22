import json

from flask import Flask, jsonify, request, abort
from blockchain import Blockchain, Block


app = Flask(__name__)

chain = Blockchain()


@app.route('/api/lastBlock', methods=['GET'])
def get_chain():
    return jsonify(chain.getLastBlock())


@app.route('/api/addBlock', methods=['POST'])
def add_block():
    chain.add_block('data')
    return jsonify({'chain': chain.chain}), 201


if __name__ == '__main__':
    app.run(debug=True)
