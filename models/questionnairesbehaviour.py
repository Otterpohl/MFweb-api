"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject

class QuestionnairesBehaviour(BaseObject, Model):

    id = Column(Integer, primary_key=True)
    UserNo                      = Column(Integer)
    ProlificID                  = Column(String(length=10000))
    TrainingNo                  = Column(String(length=10000))
    TaskNo                      = Column(String(length=10000))
    UserStartTime               = Column(String(length=10000))
    Date                        = Column(String(length=10000))
    Shuffle                     = Column(String(length=10000))
    QuestionnaireStartTime      = Column(String(length=10000))
    QuestionnaireFinishTime     = Column(String(length=10000))
    PageNo0                     = Column(String(length=10000))
    PageNo1                     = Column(String(length=10000))
    PageNo2                     = Column(String(length=10000))
    PageNo3                     = Column(String(length=10000))
    PageNo4                     = Column(String(length=10000))
    PageNo5                     = Column(String(length=10000))
    PageNo6                     = Column(String(length=10000))
    PageNo7                     = Column(String(length=10000))
    PageNo8                     = Column(String(length=10000))
    PageNo9                     = Column(String(length=10000))
    PageNo10                    = Column(String(length=10000))
    PageNo12                    = Column(String(length=10000))
    IQ_1                        = Column(String(length=10000))
    IQ_2                        = Column(String(length=10000))
    IQ_3                        = Column(String(length=10000))
    IQ_4                        = Column(String(length=10000))
    IQ_5                        = Column(String(length=10000))
    IQ_6                        = Column(String(length=10000))
    IQ_7                        = Column(String(length=10000))
    IQ_8                        = Column(String(length=10000))
    IQimage_1                   = Column(String(length=10000))
    IQimage_2                   = Column(String(length=10000))
    IQimage_3                   = Column(String(length=10000))
    IQimage_4                   = Column(String(length=10000))
    IQimage_5                   = Column(String(length=10000))
    IQimage_6                   = Column(String(length=10000))
    IQimage_7                   = Column(String(length=10000))
    IQimage_8                   = Column(String(length=10000))
    ASRS                        = Column(String(length=10000))
    BIS11                       = Column(String(length=10000))
    IUS                         = Column(String(length=10000))
    LSAS                        = Column(String(length=10000))
    SDS                         = Column(String(length=10000))
    STAI                        = Column(String(length=10000))
    OCIR                        = Column(String(length=10000))
    CFS                         = Column(String(length=10000))
    MEDIC                       = Column(String(length=10000))
    AQ10                        = Column(String(length=10000))

    def get_id(self):
        return str(self.id)

    def get_user_no(self):
        return str(self.UserNo)

    def get_prolific_id(self):
        return str(self.ProlificID)

    def get_task_player_id(self):
        return str(self.TaskNo)

    def get_training_player_id(self):
        return str(self.TrainingNo)

    def get_date(self):
        return str(self.Date)

    def get_shuffle(self):
        return str(self.Shuffle)

    def get_user_start_time(self):
        return str(self.UserStartTime)

    def get_start_time(self):
        return str(self.QuestionnaireStartTime)

    def get_finish_time(self):
        return str(self.QuestionnaireFinishTime)

    def get_page_no_0(self):
        return str(self.PageNo0)

    def get_page_no_1(self):
        return str(self.PageNo1)

    def get_page_no_2(self):
        return str(self.PageNo2)

    def get_page_no_3(self):
        return str(self.PageNo3)

    def get_page_no_4(self):
        return str(self.PageNo4)

    def get_page_no_5(self):
        return str(self.PageNo5)

    def get_page_no_6(self):
        return str(self.PageNo6)

    def get_page_no_7(self):
        return str(self.PageNo7)

    def get_page_no_8(self):
        return str(self.PageNo8)

    def get_page_no_9(self):
        return str(self.PageNo9)

    def get_iq_1(self):
        return str(self.IQ_1)

    def get_iq_2(self):
        return str(self.IQ_2)

    def get_iq_3(self):
        return str(self.IQ_3)

    def get_iq_4(self):
        return str(self.IQ_4)

    def get_iq_5(self):
        return str(self.IQ_5)

    def get_iq_6(self):
        return str(self.IQ_6)

    def get_iq_7(self):
        return str(self.IQ_7)

    def get_iq_8(self):
        return str(self.IQ_8)

    def get_asrs(self):
            return str(self.ASRS)

    def get_bis11(self):
            return str(self.BIS11)

    def get_ius(self):
            return str(self.IUS)

    def get_lsas(self):
            return str(self.LSAS)

    def get_ocir(self):
            return str(self.OCIR)

    def get_sds(self):
            return str(self.SDS)

    def get_stai(self):
            return str(self.STAI)

    def get_aq10(self):
            return str(self.AQ10)

    def get_medic(self):
            return str(self.MEDIC)

    def get_cfs(self):
            return str(self.CFS)

    def errors(self):
        errors = super(QuestionnairesBehaviour, self).errors()
        return errors
