import app
import app.tools.lessons.service as s
from flask import request
import json

logger = app.logHelper.getToolLogger()


bp = app.bpHelper.newBlueprint()

@bp.route('/savesheet', methods=['POST'])
def savesheet():
    req_body = json.loads(request.get_data(as_text=True))
    username = req_body['username']
    password = req_body['password']
    notice = req_body['notice']
    logger.log(2,username+" "+password+" "+notice)
    print (username,password,notice)
    return app.result.ok_json(s.savesheet(username, password,notice))

@bp.route('/getstudents', methods=['POST'])
def getstudents():
    req_body = json.loads(request.get_data(as_text=True))
    department = req_body['department']
    return app.result.ok_json(s.getstudents(department))

@bp.route('/getfree', methods=['POST'])
def getfree():
    req_body = json.loads(request.get_data(as_text=True))
    week = req_body['week']
    day = req_body['day']
    lesson = req_body['lesson']
    return app.result.ok_json(s.getfree(week, day, lesson))