from flask import jsonify, request
from ctps.analytics import analytics
from ctps import socketio


@analytics.route('/analytics', methods=['POST'])
def fetch_analytics():
    resp = jsonify({'success': True})
    socketio.emit('event', {'data': request.get_json(force=True)})
    resp.status_code = 201
    return resp
