_base_ = [
        '/home/dmitry/mmsegmentation/configs/_base_/models/fast_scnn.py', '/home/dmitry/mmsegmentation/configs/_base_/datasets/cityscapes.py',
        '/home/dmitry/mmsegmentation/configs/_base_/default_runtime.py', '/home/dmitry/mmsegmentation/configs/_base_/schedules/schedule_160k.py'
        ]

# classes = ('background', 'base', 'base-background-layer-segmentation', 'toucan', 'wood')
# palette = [[199, 21, 133], [255, 69, 0], [255, 20, 147], [127, 255, 0], [0, 255, 255]]

crop_size = (512, 1024)
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor)
# Re-config the data sampler.
train_dataloader = dict(batch_size=4, num_workers=4)
val_dataloader = dict(batch_size=1, num_workers=4)
test_dataloader = val_dataloader

# Re-config the optimizer.
optimizer = dict(type='SGD', lr=0.12, momentum=0.9, weight_decay=4e-5)
optim_wrapper = dict(type='OptimWrapper', optimizer=optimizer)

load_from = 'fast_scnn_lr0.12_8x4_160k_cityscapes_20210630_164853-0cec9937.pth'
work_dir = 'work'



