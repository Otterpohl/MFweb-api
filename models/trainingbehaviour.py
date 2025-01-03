"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY

from models.db import Model
from models.base_object import BaseObject


class TrainingBehaviour(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    UserNo              = Column(Integer)
    ProlificID          = Column(String(length=10000))
    TrainingNo          = Column(String(length=10000))
    TaskNo              = Column(String(length=10000))
    Date                = Column(String(length=10000))
    UserStartTime       = Column(String(length=10000))
    TrainingStartTime   = Column(String(length=10000))
    TrainingFinishTime  = Column(String(length=10000))
    SumPassed           = Column(String(length=10000))
    ChoicesSize         = Column(String(length=10000))
    InitialSamplesSize  = Column(String(length=10000))
    ReactionTimes       = Column(String(length=10000))
    ChoicesCorrect      = Column(String(length=10000))
    Chosen              = Column(String(length=10000))
    CorrectAns          = Column(String(length=10000))
    NumTraining         = Column(String(length=10000))


    def get_id(self):
        return str(self.id)

    def get_prolific_id(self):
        return str(self.ProlificID)

    def get_task_player_id(self):
        return str(self.TaskNo)

    def get_training_player_id(self):
        return str(self.TrainingNo)

    def get_date(self):
        return str(self.Date)

    def get_user_start_time(self):
        return str(self.UserStartTime)

    def get_user_no(self):
        return str(self.UserNo)

    def get_training_start_time(self):
        return str(self.TrainingStartTime)

    def get_training_finish_time(self):
        return str(self.TrainingFinishTime)

    def get_sum_passed(self):
        return str(self.SumPassed)

    def get_choices_size(self):
        return str(self.ChoicesSize)

    def get_choices_correct(self):
        return str(self.ChoicesCorrect)

    def get_reaction_times(self):
        return str(self.ReactionTimes)

    def get_initial_samples_size(self):
        return str(self.InitialSamplesSize)

    def get_chosen(self):
        return str(self.Chosen)

    def get_correct_ans(self):
        return str(self.CorrectAns)

    def get_num_training(self):
        return str(self.NumTraining)

    def errors(self):
        errors = super(TrainingBehaviour, self).errors()
        return errors
