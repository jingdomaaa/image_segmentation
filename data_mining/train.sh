source activate
conda deactivate
conda activate tensorflow
mkdir -p logs/
now=$(date +"%Y%m%d_%H%M%S")
python ../../../../train.py \
    --logtostderr \
    --train_split="train" \
    --model_variant="xception_65" \
    --atrous_rates=12 \
    --atrous_rates=24 \
    --atrous_rates=36 \
    --output_stride=8 \
    --decoder_output_stride=4 \
    --train_crop_size=513,513 \
    --train_batch_size=1 \
    --training_number_of_steps=10 \
    --fine_tune_batch_norm=false \
    --tf_initial_checkpoint="../../init_models/deeplabv3_pascal_train_aug/model.ckpt" \
    --train_logdir="train/" \
    --dataset_dir="../../tfrecord/" 2>&1 | tee logs/train_$now.txt &