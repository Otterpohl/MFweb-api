"""users routes"""
from flask import current_app as app, jsonify, request
from flask_cors import cross_origin
from models import TrainingBehaviour, BaseObject


@app.route('/training_behaviour/<user_id>', methods=['POST', 'GET'])
@cross_origin()
def create_training_behaviour(user_id):

    content                         = request.json
    trainingbehaviour               = TrainingBehaviour()

    trainingbehaviour.UserNo                = int(user_id)
    trainingbehaviour.UserStartTime         = str(content['UserStartTime'])
    trainingbehaviour.ProlificID            = str(content['ProlificID'])
    trainingbehaviour.TrainingNo            = str(content['TrainingNo'])
    trainingbehaviour.TaskNo                = str(content['TaskNo'])
    trainingbehaviour.Date                  = str(content['Date'])
    trainingbehaviour.TrainingStartTime     = str(content['TrainingStartTime'])
    trainingbehaviour.TrainingFinishTime    = str(content['TrainingFinishTime'])
    trainingbehaviour.SumPassed             = str(content['SumPassed'])
    trainingbehaviour.InitialSamplesSize    = str(content['InitialSamplesSize'])
    trainingbehaviour.ReactionTimes         = str(content['ReactionTimes'])
    trainingbehaviour.ChoicesSize           = str(content['ChoicesSize'])
    trainingbehaviour.ChoicesCorrect        = str(content['ChoicesCorrect'])
    trainingbehaviour.Chosen                = str(content['Chosen'])
    trainingbehaviour.CorrectAns            = str(content['CorrectAns'])
    trainingbehaviour.NumTraining           = str(content['NumTraining'])


    BaseObject.check_and_save(trainingbehaviour)

    result = dict({"success": "yes"})

    return jsonify(result)
