from mmseg.datasets import BaseSegDataset
from mmseg.registry import DATASETS

@DATASETS.register_module()
class CustomDataset(BaseSegDataset):
    METAINFO = dict(classes=('background', 'base', 'base-background-layer-segmentation', 'toucan', 'wood'),
                    palette=[[199, 21, 133], [255, 69, 0], [255, 20, 147], [127, 255, 0], [0, 255, 255]])

