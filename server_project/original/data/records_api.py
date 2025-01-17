from flask import Blueprint, jsonify, request
from . import db_session
from .records import Records
from .maps import Maps

blueprint = Blueprint('records_api', __name__,
                      template_folder='templates')


@blueprint.route('/api/records')
def get_records():
    session = db_session.create_session()
    records = []
    for i in session.query(Maps):
        lst = sorted(session.query(Records).filter(Records.map_name == i.name_map),
                     key=lambda x: x.points, reverse=True)[:5]
        if lst:
            records.append(lst)
    return jsonify(
        {
            'records':
                [[item.to_dict(only=('map_name', 'points', 'user_id'))
                  for item in records[i]] for i in range(len(records))]
        }
    )


@blueprint.route('/api/records/<int:record_id>', methods=['GET'])
def get_one_record(record_id):
    session = db_session.create_session()
    record = session.query(Records).get(record_id)
    if not record:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'record': record.to_dict(only=('id', 'map_name', 'points', 'user_id'))
        }
    )


@blueprint.route('/api/records/<name>', methods=['GET'])
def get_record(name):
    session = db_session.create_session()
    records = session.query(Records).filter(Records.map_name == name)
    if not records:
        return jsonify({'records': False})
    return jsonify(
        {
            'records':
                [item.to_dict(only=('id', 'map_name', 'points', 'user_id'))
                 for item in sorted(records, key=lambda x: x.points, reverse=True)]
        }
    )


@blueprint.route('/api/records', methods=['POST'])
def create_record():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['map_name', 'points', 'user_id']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    record = Records(
        map_name=request.json['map_name'],
        points=request.json['points'],
        user_id=request.json['user_id']
    )
    session.add(record)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/records/<int:record_id>', methods=['GET', 'POST'])
def transform_one_record(record_id):
    session = db_session.create_session()
    record = session.query(Records).get(record_id)
    if not record:
        return jsonify({'error': 'Not found'})
    for key in ['map_name', 'points', 'user_id']:
        if key in request.json.keys():
            exec('record.{}={}'.format(key, request.json[key]))
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/records/<int:job_id>', methods=['DELETE'])
def delete_record(record_id):
    session = db_session.create_session()
    record = session.query(Records).get(record_id)
    if not record:
        return jsonify({'error': 'Not found'})
    session.delete(record)
    session.commit()
    return jsonify({'success': 'OK'})
