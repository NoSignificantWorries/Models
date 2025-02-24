_base_ = [
        '/mmsegmentation/configs/_base_/models/fast_scnn.py' #, '/mmsegmentation/configs/_base_/datasets/cityscapes.py',
        # '/mmsegmentation/configs/_base_/default_runtime.py', '/mmsegmentation/configs/_base_/schedules/schedule_160k.py'
        ]

dataset_type = 'CustomDataset'
data_root = '/workspace/toucan2'

img_norm_cfg = dict(
        mean=[90.21497949957848, 100.5998982489109, 60.338090881705284],
        std=[55.05881376564503, 51.532454788684845, 46.08421593904495],
        to_rgb=True)
train_pipeline = [
        dict(type='LoadImageFromFile'),
        dict(type='LoadAnnotations'),
        dict(type='Resize', img_scale=(512, 512), keep_ratio=True),
        dict(type='RandomCrop', crop_size=(256, 256), cat_max_ratio=0.75),
        dict(type='RandomFlip', flip_ratio=0.5),
        dict(type='PhotoMetricDistortion'),
        dict(type='Normalize', **img_norm_cfg),
        dict(type='Pad', size=(256, 256), pad_val=0, seg_pad_val=255),
        dict(type='DefaultFormatBundle'),
        dict(type='Collect', keys=['img', 'gt_semantic_seg'])
        ]
test_pipeline = [
        dict(type='LoadImageFromFile'),
        dict(
            type='MultiScaleFlipAug',
            img_scale=(512, 512),
            flip=False,
            transforms=[
                dict(type='Resize', keep_ratio=True),
                dict(type='RandomFlip'),
                dict(type='Normalize', **img_norm_cfg),
                dict(type='ImageToTensor', keys=['img']),
                dict(type='Collect', keys=['img'])
                ])
            ]

data = dict(
        samples_per_gpu=4,
        workers_per_gpu=4,
        train=dict(
            type=dataset_type,
            data_root=data_root,
            img_dir='images/train',
            ann_dir='annotations/train',
            pipeline=train_pipeline),
        val=dict(
            type=dataset_type,
            data_root=data_root,
            img_dir='images/valid',
            ann_dir='annotations/valid',
            pipeline=test_pipeline),
        test=dict(
            type=dataset_type,
            data_root=data_root,
            img_dir='images/test',
            ann_dir='annotations/test',
            pipeline=test_pipeline))

classes = ('background', 'base', 'base-background-layer-segmentation', 'toucan', 'wood')
palette = [[199, 21, 133], [255, 69, 0], [255, 20, 147], [127, 255, 0], [0, 255, 255]]

optimizer = dict(type='SGD', lr=0.12, momentum=0.9, weight_decay=4e-5)

load_from = 'fast_scnn_lr0.12_8x4_160k_cityscapes_20210630_164853-0cec9937.pth'
work_dir = 'work'



