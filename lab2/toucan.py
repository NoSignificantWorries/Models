from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class ToucanDataset(BaseSegDataset):

    METAINFO = dict(
        classes=('background', 'base', 'base-background-layer-segmentation', 'toucan', 'wood'),
        palette=[[199, 21, 133], [255, 69, 0], [255, 20, 147], [127, 255, 0], [0, 255, 255]])

    def __init__(self, arg1, arg2):
        pass
