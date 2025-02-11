""" 
@author: Jun Wang
@date: 20201019
@contact: jun21wangustc@gmail.com   
""" 

import sys
import yaml
sys.path.append('../../')
from head.AdaCos import AdaCos
from head.AdaM_Softmax import Adam_Softmax
from head.AM_Softmax import AM_Softmax
from head.ArcFace import ArcFace
from head.CircleLoss import CircleLoss
from head.CurricularFace import CurricularFace
from head.MV_Softmax import MV_Softmax
from head.NPCFace import NPCFace
from head.SST_Prototype import SST_Prototype

class HeadFactory:
    """Factory to produce head according to the head_conf.yaml
    
    Attributes:
        head_type(str): which head will be produce.
        head_param(dict): parsed params and it's value.
    """
    def __init__(self, head_type, head_conf_file):
        self.head_type = head_type
        with open(head_conf_file) as f:
            head_conf = yaml.load(f)
            self.head_param = head_conf[head_type]
        print('head param:')
        print(self.head_param)
    def get_head(self):
        if self.head_type == 'AdaCos':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in the training set.
            head = AdaCos(feat_dim, num_class)
        elif self.head_type == 'AdaM-Softmax':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in training set.
            scale = self.head_param['scale']
            lamda = self.head_param['lamda']
            head = Adam_Softmax(feat_dim, num_class, scale, lamda)
        elif self.head_type == 'AM-Softmax':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in the training set.
            margin = self.head_param['margin']
            scale = self.head_param['scale']
            head = AM_Softmax(feat_dim, num_class, margin, scale)
        elif self.head_type == 'ArcFace':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in the training set.
            margin_arc = self.head_param['margin_arc']
            margin_am = self.head_param['margin_am']
            scale = self.head_param['scale'] 
            head = ArcFace(feat_dim, num_class, margin_arc, margin_am, scale)
        elif self.head_type == 'CircleLoss':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in the training set.
            margin = self.head_param['margin']
            gamma = self.head_param['gamma']
            head = CircleLoss(feat_dim, num_class, margin, gamma)
        elif self.head_type == 'CurricularFace':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in the training set.
            margin = self.head_param['margin']
            scale = self.head_param['scale']
            head = CurricularFace(feat_dim, num_class, margin, scale)
        elif self.head_type == 'MV-Softmax':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in the training set.
            is_am = self.head_param['is_am']
            margin = self.head_param['margin']
            mv_weight = self.head_param['mv_weight']
            scale = self.head_param['scale']
            head = MV_Softmax(feat_dim, num_class, is_am, margin, mv_weight, scale)
        elif self.head_type == 'NPCFace':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in the training set.
            margin = self.head_param['margin']
            scale = self.head_param['scale']
            head = NPCFace(feat_dim, num_class, margin, scale)
        elif self.head_type == 'SST_Prototype':
            feat_dim = self.head_param['feat_dim']
            queue_size = self.head_param['queue_size']
            scale = self.head_param['scale']
            loss_type = self.head_param['loss_type']
            margin = self.head_param['margin']
            head = SST_Prototype(feat_dim, queue_size, scale, loss_type, margin)
        else:
            pass
        return head
